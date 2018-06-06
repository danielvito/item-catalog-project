# Build an Item Catalog Application Project

Source code to run an item catalog application.

## Project

This is an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.
This project makes part of the [Full-Stack Web Nanodegree Program](https://udacity.com/course/full-stack-web-developer-nanodegree--nd004) from Udacity.

## Code

Code is neatly formatted and follows the Python [PEP-8 Guidelines](http://pep8online.com/).

## Installation and Usage

In order to run this project you need python 3.x installed.

```sh
git clone https://github.com/danielvito/item-catalog-project.git
cd [item-catalog-project
```

Open url <http://localhost:5000/> with a web browser.

### Database

You can change the file lotsofitens.py and execute it if you want to recreate a initial database file.

```sh
cd item-catalog-project/database_setup/
python lotsofitens.py
# generate the ./catalog.db file
```

### Running the application in dev mode on Linux

```sh
export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_APP=project.py
flask run
```

### Running the application in dev mode on Windows (Power Shell)

```sh
$env:FLASK_DEBUG=1
$env:FLASK_ENV='development'
$env:FLASK_APP='project.py'
flask run
```

### Running the application in shell mode

```sh
# after create FLASK_APP env var
flask shell
>>> app
<Flask 'app'>
>>> User
<class 'app.models.User'>
>>> Brand.query.all()
[<Brand Nike>, <Brand Adidas>, <Brand Wilson>]
```

### I18n

This app uses the Flask-babel extension for translation.

The code below finds every use of the function `_('any_key')` and updates the Portuguese and English translation files.

```sh
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d app/translations
pybabel compile -d app/translations
```

## License

All the code in this project is a public domain work, dedicated using [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Feel free to do whatever you want with it.