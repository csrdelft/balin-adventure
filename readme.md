## Getting Started With Development

#### Native

    make install && npm install && npm install -g gulp && gem install compass
    gulp
    source .virtualenv/bin/activate
    mysql -u root -e "create database csrdelft_django; grant all privileges on csrdelft_django.* to csrdelft@localhost identified by 'bl44t';"
    cd src
    ./manage.py migrate

    # You now have a fresh databse
    # import some data
    ./manage.py loaddata dev.yaml

    # You should be good to go...
    ./manage.py runserver


#### Windows

1. Install Python (including pip), NodeJS (including npm)
2. Open cmd prompt at the root of the repository
3. Run the following commands

    # create the python sandbox (only first time)
    python -m venv .virtualenv
    # activate the sandbox (every time)
	  .virtualenv\Scripts\activate

	  # install the python requirements in the sandbox
	  python -m pip install -r requirements

	  # install the javascript dependencies (as listed in package.json)
	  npm install
	  # globally install gulp (the build tool)
	  npm install -g gulp
	  # run the build
    gulp

    # create the database
    mysql -u root -p -e "create database csrdelft_django; grant all privileges on csrdelft_django.* to csrdelft@localhost identified by 'bl44t';"

    # run the migrations to get the database schema up to date
    python src\manage.py migrate
    python src\manage.py migrate // yeah 2x

    # run the server
	  python src\manage.py runserver

4. You should now be able to visit `localhost:8000` (and `localhost:8000/admin/`) in your browser

#### Vagrant

Deprecated:

    vagrant up --provider viritualbox
    # django will throw error in the end of first go
    # because we haven't initialized the database yet
    vagrant ssh
    > mysql_secure_installation
    > mysql -u root -e "create database csrdelft_django; grant all privileges on csrdelft_django.* to csrdelft@localhost identified by 'bl44t';"
    > cd /vagrant/src
    > ../.virtualen/bin/python manage.py migrate
    > ../.virtualen/bin/python manage.py loaddata dev
    > exit
    vagrant reload

Next time `vagrant up` should be enough. `vagrant ssh` allows you to migrate and such.

### Migrating old models

The idea is to take the existing production database, create a model + migration on the django side
that is compatible with it, migrate the existing data as exampled below and take it from there.

## Apps

### Base

You can import the data from 'profielen' on the database after migration 0001 (or 0002)

    mysqldump -u root profielen --no-create-info -c > profielen_data.sql
    mysql -u root csrdelft_django < profielen_data.sql

After importing those, you can create the authentication users from the legacy `accounts` table.
Because the migration requires some transformation of the passwords and access to both
the old and new database, it has been implemented as a separate script (`bin/migrate_accounts.py`).
If you've setup the DATABASE config in your `settings.py` correctly, with legacy pointing to
a running legacy database, you can run the script `python bin/migrate_accounts.py` from the `src/`
directory.

You can import the data from 'groepen' on the database after base migration 0003:

    mysqldump -u root csrdelft \
      kringen kring_leden \
      commissies commissie_leden \
      besturen bestuurs_leden \
      werkgroepen werkgroep_deelnemers \
      verticalen verticale_leden \
      onderverenigingen ondervereniging_leden \
      lichtingen lichting_leden \
      ketzers ketzer_deelnemers \
      activiteiten activiteit_deelnemers \
      groepen groep_leden \
      --no-create-info -c > groepen_data.sql
    mysql -u root csrdelft_django < groepen_data.sql

### Forum

You can import the data from the production database after it's initial migration 0001:

    mysqldump -u root csrdelft \
      forum_posts forum_draden_gelezen forum_draden_reageren \
      forum_draden_volgen forum_draden_verbergen forum_categorien \
      forum_delen forum_draden --no-create-info -c > forum_data.sql
    mysql -u root csrdelft_django < forum_data.sql

#### Backwards compatability

To use the legacy production database *directly as a backend*, you need to
fake migration 0001 and make sure the database is field-wise the same as the one generated by
django. The one difference being the id columns on the following tables, which were added:

    forum_draden_gelezen
    forum_draden_reageren
    forum_draden_verbergen
    forum_draden_volgen

## TODO

- Add password policies (has been implemented for django)

## Notes

### Setting up

#### How do I django???
Django has EXCELLENT documentation: https://docs.djangoproject.com/en/1.8/

#### How can I CLI???
By default IPython and Django extensions are installed, so you can `./manage.py shell_plus`
to open a top-notch shell with autocomplete, colors, great debugging and all the models
preloaded.

#### Migrations???
Ain't it awesome? Remember these commands:

    python manage.py makemigrations # to generate new migrations based on model changes (CHECK!)
    python manage.py migrate # make db up to date
    python manage.py migrate <appname> <000x> # migrate specific app to specific migration
    python manage.py makemigrations --empty base # create new data migration for app base
