FROM nginx:latest

WORKDIR /

COPY ./nginx-configs/ /etc/nginx
RUN sed -i 's#nginx:x:101:101:nginx#nginx:x:1000:1000:nginx#g' /etc/passwd
