created a deployment yml for web application as web_application.yml and mysql-database as mysql-db.yml files
created sevice files for both 
Used node port for webapp sevice to access the container port forwarding port 80 for generated 30878 service port (check out in $kubectl get svc)
Used clusterIp for db service as it wont be accessed outside cluster

logged in to webapp pod and nano /var/www/html.index.php
edited the file with credentials

created database by logging into db pod and exited

accessed with clusterIP and nodeport as 192.168.49.2:30878 in this case
