FROM nginx:1.22
ADD nginx.conf /nginx/
CMD nginx -c /nginx/nginx.conf
