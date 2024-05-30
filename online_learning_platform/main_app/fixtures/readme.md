
## Delete migrations folder in online_learning_platform/main_app

## deleted the migrations from db:
`DELETE from django_migrations WHERE app='main_app';` 

## create the tables
`python manage.py migrate --run-syncdb`

## load init data
`python manage.py loaddata  main_app/fixtures/init.json`