# Knowledge Prerequisites
* Python lists - Dictionaries
* Object oriented programming (python classes)
* Python Decorators (sort of required, at least have a look)

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

## TestDrivenDevelopment
TDD - BDD

## JWT - Json Web token



# next steps
* Swagger UI
* Use SQL database / Firebase
* Deploy Flask api to Heroku/DigitalOcean/OVH/Amazon


### Ideas lokas to do with Flask:
* send chistes to a list of users ;)
* Tweet generator
* Shakespeare Insult Generator: http://www.pangloss.com/seidel/shake_rule.html
* QR Generator
* Automatic watering for plants with Raspberry: https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc
* Free apis: https://github.com/toddmotto/public-apis


