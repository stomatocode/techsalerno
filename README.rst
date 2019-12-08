TechSalerno
===========

Working Association

.. image:: https://img.shields.io/badge/based%20on-Django%20Naqsh-0952D5.svg
     :target: https://github.com/mazdakb/django-naqsh/
     :alt: Built with Django Naqsh
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Settings
--------

Moved to settings_.

.. _settings: http://django-naqsh.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy techsalerno

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd techsalerno
    celery -A config.celery worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.



Deployment
----------

The following details how to deploy this application.


