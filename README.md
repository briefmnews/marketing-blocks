
# marketing-blocks
[![Python 3.x](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-377/) 
[![Django 2.x](https://img.shields.io/badge/django-2.x-blue.svg)](https://docs.djangoproject.com/en/2.11/)
[![Build Status](https://travis-ci.org/briefmnews/marketing-blocks.svg?branch=master)](https://travis-ci.org/briefmnews/marketing-blocks)
[![codecov](https://codecov.io/gh/briefmnews/marketing-blocks/branch/master/graph/badge.svg)](https://codecov.io/gh/briefmnews/marketing-blocks)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)  
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
#### Optional
You can set a label to your marketing blocks with the following settings:
```python
MARKETING_BLOCKS_LABEL_CHOICES
```

Here is an exemple of usage:
```python
MARKETING_BLOCKS_LABEL_CHOICES = [("", "-----"), ("issue", "Issue"), ("panorama", "Panorama")]
```

### Migrations
Next, you need to run the migrations in order to update your database schema.
```shell
python manage.py migrate
```

## Hot to use ?
In django-admin you can do to the app `Marketing_blocks` and create a new marketing bock.\
3 positions are available:
* **pre_header**: only one pre_header block can be active at the time.
* **header**: only one header block can be active at the time.
* **footer**: only one footer block can be active at the time.
* **pre_footer**: only one pre_footer block can be active at the time.
* **body_{1..5}**: you can set up to 5 body blocks.

Next you can retrieve all the active blocks like this:
```python
from marketing_blocks.models import MarketingBlock


def dummy_view(request):
    ...
    
    marketing_blocks = MarketingBlock.objects.get_block_contents_by_position()
    
    ...
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
