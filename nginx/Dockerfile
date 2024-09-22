FROM nginx:latest

RUN apt update

RUN rm /etc/nginx/nginx.conf
COPY ./nginx.conf.template /etc/nginx/nginx.conf.template
COPY ./entrypoint.sh /docker-entrypoint.d/entrypoint.sh
RUN chmod +x /docker-entrypoint.d/entrypoint.sh

CMD ["nginx", "-g", "daemon off;"]