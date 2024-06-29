application.properties

```
swagger.basic.enable=true
swagger.basic.username=anghfdmadin
swagger.basic.password=DdontHacakMePlss

file.path=/opt/apache-tomcat-8.5.87/webapps/zhtcpt/upload/
```


default
```
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name localhost;

        location /zhtcpt {
            proxy_pass http://127.0.0.1:8080/zhtcpt;

        }
        location /zhtcpt/images {
            root /home/test;
            sendfile on;
            autoindex on;
        }
        location /zhtcpt/upload {
            root /home/test;
            sendfile on;
            autoindex on;
        }
        location /imageservice {
            proxy_pass http://127.0.0.1:8080/imageservice;
        }

        location / {
            proxy_pass http://127.0.0.1:8080/home/;
        }   
}
```

update.sh
```
update.sh

#!/bin/sh
mv application.properties /opt/apache-tomcat-8.5.87/webapps/imageservice/WEB-INF/classes/application.properties
chmod 777 /opt/apache-tomcat-8.5.87/webapps/imageservice/WEB-INF/classes/application.properties

mv default /etc/nginx/sites-enabled/default
chmod 777 /etc/nginx/sites-enabled/default

mkdir -p /home/test/zhtcpt/images
mkdir -p /home/test/zhtcpt/upload
cp /opt/apache-tomcat-8.5.87/webapps/zhtcpt/images/* /home/test/zhtcpt/images
mv /opt/apache-tomcat-8.5.87/webapps/zhtcpt/images /opt/apache-tomcat-8.5.87/webapps/zhtcpt/bak
mv /opt/apache-tomcat-8.5.87/webapps/zhtcpt/upload /opt/apache-tomcat-8.5.87/webapps/zhtcpt/bak1
ln -s /home/test/zhtcpt/images /opt/apache-tomcat-8.5.87/webapps/zhtcpt/images
ln -s /home/test/zhtcpt/upload /opt/apache-tomcat-8.5.87/webapps/zhtcpt/upload


sh /opt/apache-tomcat-8.5.87/bin/shutdown.sh
/etc/init.d/nginx stop

sh /opt/apache-tomcat-8.5.87/bin/startup.sh
/etc/init.d/nginx start

sleep 5
```
