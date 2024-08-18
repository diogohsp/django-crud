# Django Commands

## Start Server

Start the Django development server.

```bash
python manage.py runserver
```

## Migrations

##### Makemigrations command detects the changes made to your models and creates migration files inside the migrations directory of each app in your project. These files contain instructions for applying the changes to the database.

```bash
python manage.py makemigrations
```

##### Migrate, which actually applies the migrations and updates the database.

```bash
python manage.py migrate
```
