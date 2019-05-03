# marketing-blocks
[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/) 
[![Django 1.11](https://img.shields.io/badge/django-1.11-blue.svg)](https://docs.djangoproject.com/en/1.11/)
[![Build Status](https://travis-ci.org/briefmnews/marketing-blocks.svg?branch=master)](https://travis-ci.org/briefmnews/marketing-blocks)
[![codecov](https://codecov.io/gh/briefmnews/marketing-blocks/branch/master/graph/badge.svg)](https://codecov.io/gh/briefmnews/marketing-blocks)      
Manage marketing blocks from back office for django

## Installation
Install with [pip](https://pip.pypa.io/en/stable/):
```shell
pip install -e git://github.com/briefmnews/marketing-blocks.git#egg=marketing_blocks
```

## Setup
In order to make `marketing-blocks` works, you'll need to follow the steps below.

### Settings
First you need to add the following configuration to your settings:
```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',

    'marketing_blocks',
    ...
)
```

### Migrations
Next, you need to run the migrations in order to update your database schema.
```shell
python manage.py migrate
```

## Tests
Testing is managed by `pytest`. Required package for testing can be installed with:
```shell
pip install -r test_requirements.txt
```
To run testing locally:
```shell
pytest
```
