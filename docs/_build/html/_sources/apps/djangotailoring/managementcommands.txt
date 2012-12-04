*******************
Management Commands
*******************

Django management commands allow for project related tasks to be easily and
repeatedly performed without having to write a request-responding view.
Djangotailoring provides two such commands.

Model Creation Assistance
=========================

.. _makemtsmodels-command:

makemtsmodels
-------------

When called in a project configured for ``djangotailoring``::

  $ python manage.py makemtsmodels

the project dictionary will be read, and used to build functional Python
module code that contains :class:`djangotailoring.models.SubjectData` objects
representing each source and its constituent characteristics. This code is
written to standard-out.

The best way to use this is to redirect the output to a file using the shell::

  $ python manage.py makemtsmodels > myapp/mtsmodels.py

The resulting file should be ``import``\able and ``syncdb``\-able.

Localization Assistance
=======================

.. _makedictmessages-command:

makedictmessages
----------------

When called in a project configured for ``djangotailoring``::

  $ python manage.py makedictmessages <langcode>

the project dictionary will be read, and used to build a set of GNU gettext
packages for translating the current dictionary objects from the native
language to another.

This command performs the same as Django's built-in ``makemessages`` command;
the output file paths are the same, the document domain is the same, and the
argument structure is the same.

Various objects in the dictionary are written to the file, and categorized
accordingly:

  * Survey questions (*mts|question*)
  * Survey option text (*mts|option*)
  * Substitution values (*mts|substitution*)

