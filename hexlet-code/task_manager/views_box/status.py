from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models.status import Status


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return Status.objects.filter(user=self.request.user)


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'status/status_form.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Привязываем статус к текущему пользователю
        messages.success(self.request, "Status created successfully!")
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'status/status_form.html'
    success_url = reverse_lazy('status_list')

    def get_queryset(self):
        # Ограничиваем редактирование только своими статусами
        return Status.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Status updated successfully!")
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status/status_confirm_delete.html'
    success_url = reverse_lazy('status_list')

    def get_queryset(self):
        return Status.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        status = self.get_object()
        if status.task_set.exists():  # Проверяем, есть ли связанные задачи
            messages.error(self.request, "Cannot delete this status as it is associated with tasks.")
            return redirect('status_list')
        messages.success(self.request, "Status deleted successfully!")
        return super().delete(request, *args, **kwargs)
