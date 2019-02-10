# Knowledge Prerequisites
* Python lists - Dictionaries
* Object oriented programming (python classes)
* Python Decorators (sort of required, at least have a look)

# What will you learn at the end of the lesson
* Create a git repo
* Decorators? Decorators
* Create a Flask application
* Create a REST API with Flask
* Add authentication to your REST API
## Next Steps (not in this lesson haha salu2, but we can talk a little bit)
* Swagger UI (similar to Postman, but integrated as a Python module)
* Use SQL database (MySQL - Postgres) / Firebase (NoSQL)
* Deploy Flask API to Heroku/DigitalOcean/OVH/Amazon

# Installation
## Programs
* Git: https://git-scm.com/downloads
* Sourcetree (recommended): https://www.sourcetreeapp.com/
* Postman: https://www.getpostman.com/products
* Pycharm community IDE (recommended): https://www.jetbrains.com/pycharm/download/
    * Other IDEs: Atom/Visual Studio Code/Sublime Text


## Dependencies - Virtual Environment
Let's create a virtual environment! Such a great idea! It lets you isolate 
all your projects so that they don't depend on modules of other projects

In case you don't have Pycharm -> Create Virtual Environment and activate
```bash
$ cd <your dir>
$ pip3 install virtualenv
$ virtualenv venv --python=python3.6
$ source venv/bin/activate
```
Now that you have a Virtual Environment, install all the libraries needed:
```bash
$ pip3 install -r requirements.txt
```
### .gitignore
Gitignore file at the root of the project makes git ignore all files that match a pattern 
so that they don't get committed. Useful for files with keys/tokens/passwords or huge files that you don't want 
to be pushed (e.g. virtual Env)

There is one webpage that generates this file for you, kinda helpful:
https://www.gitignore.io/

# Concepts
## HTTP Verbs
![HTTP Verbs](/screenshots/httpverbs.png)

## Decorators
Decorator example (more inside examples/example_decorator.py)

```python
def dec_returns(func):
    def wrapper(*args, **kwargs):
        print("I do something before")
        aux_out = func(*args, **kwargs)
        print("I do something after")
        return aux_out
    return wrapper


@dec_returns
def los_hahas():
    return "LOL"


a = los_hahas()
print(a)
```

Out: 
```bash
I do something before
I do something after
LOL
```

## TestDrivenDevelopment
TDD - BDD, o como debería ser SEAT

## JWT - Json Web token
Basically, a token that is passed with the Header attribute of the HTTP Verb

### Ideas lokas to do with Flask:
* send chistes to a list of users ;)
* Tweet generator
* Shakespeare Insult Generator: http://www.pangloss.com/seidel/shake_rule.html
* QR Generator
* Automatic watering for plants with Raspberry: https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc
* Free apis: https://github.com/toddmotto/public-apis


