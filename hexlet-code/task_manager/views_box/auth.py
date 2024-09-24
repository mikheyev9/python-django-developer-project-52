from django.contrib.auth.models import User
from django.views.generic import ListView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "User created successfully!")
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'user_form.html'  # Используем этот шаблон для редактирования пользователя

    def test_func(self):
        # Проверяем, что текущий пользователь может редактировать свой профиль
        user = self.get_object()
        return self.request.user == user

    def form_valid(self, form):
        # Если данные формы валидны, сохраняем изменения
        form.save()
        messages.success(self.request, "Profile updated successfully!")
        return redirect('user_list')  # Перенаправляем на список пользователей

    def form_invalid(self, form):
        # Если форма невалидна, выводим сообщение об ошибке и остаемся на текущей странице
        messages.error(self.request, "There was an error updating the profile.")
        return self.render_to_response(self.get_context_data(form=form))

    def handle_no_permission(self):
        # Если у пользователя нет прав, выводим сообщение об ошибке и не передаем объект в контекст
        messages.error(self.request, "You do not have permission to edit this profile.")
        return redirect('user_list')

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user_list')

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.test_func():
            self.object = self.get_object()
            self.object.delete()
            return JsonResponse({"success": True, "message": "User deleted successfully!"})
        else:
            return JsonResponse({"success": False, "message": "You do not have permission to delete this user."},
                                status=403)

    def handle_no_permission(self):
        return JsonResponse({"success": False, "message": "You do not have permission to delete this user."},
                            status=403)
