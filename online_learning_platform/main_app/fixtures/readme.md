# Create a migration fixture
1. Dump data
`python manage.py dumpdata  main_app > main_app/fixtures/<NAME>.json`


# Import a migration fixture, as an initial database population

1. Delete migrations folder in online_learning_platform/main_app

2. Delete the app migrations from db:
`DELETE from django_migrations WHERE app='main_app';` 

3. Sync the tables
`python manage.py migrate --run-syncdb`

4. load init data
`python manage.py loaddata  main_app/fixtures/init.json`