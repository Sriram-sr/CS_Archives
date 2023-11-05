Django sqllite db check 
$ python3 manage.py shell - To enter into interactive shell

Each django model is a db table

After creating table to migrate 
$ python manage.py makemigrations <app_name>
$ python manage.py migrate - this will show all migrations happenning
$ python manage.py sqlmigrate <app_migrate_number> - You can get your app migrate number from above command
  - this will show the real table creation command

blank = True or null = True serves same

