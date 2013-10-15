# Lottery Server

Steps necessary to run a development version of Lottery project.

## System Setup

In order to develop Lottery you need a few software packages. Lottery is designed to run on:

* OS X 10.7 or newer

Later will be available a Linux version


## System Setup on **OS X**

**First you need a working [Homebrew](http://mxcl.github.com/homebrew/) install.**

Once you've got `Homebrew` you can install the dependencies:

    brew update
    brew install gettext
    brew link gettext

Download and install [Postgres.app](http://postgresapp.com/).
Start Postgres app and create the database for Lottery to run:

    /Applications/Postgres.app/Contents/MacOS/bin/createdb -E utf8 -T template0 lottery


## Lottery Development Setup

Now clone the repository from GitHub:

    git clone git@github.com:e3c/adroaldof/lottery.git
    cd lottery

Then create and activate a `virtualenv` that will hold all `python` dependencies:

    curl https://raw.github.com/pypa/virtualenv/69eb6f4f932d7479ca166e221177cbb8f13b7c84/virtualenv.py | python2.7 /dev/stdin env
    . env/bin/activate
    pip install -r lottery/requirements.txt

After installation finishes you can configure the development database:

    python lottery/manage.py syncdb

Now you can run Lottery page:

    python manage.py runserver

And you are ready to go, just click on the link below

[http://127.0.0.1:8000](http://127.0.0.1:8000 "localhost")

-----