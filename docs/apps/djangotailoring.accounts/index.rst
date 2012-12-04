****************************
``djangotailoring.accounts``
****************************

.. module:: djangotailoring.accounts

Contents:

.. toctree::

  accesscodes
  models
  forms
  backends
  views

The ``accounts`` application in ``djangotailoring`` provides common features
for creating, and authenticating users based on abstract Access Codes.

Overview
========

Access Codes are a set of pre-defined codes that provide invite-only
access to the site. The codes in this app are replacements for the
:attr:`username` field of the :class:`django.contrib.auth.models.User` model.

In addition to allowing for single-token access to the site, they also allow
for a staged registration process. The process works something like this:

  * A user enters an access code
  * They may view portions of the site, or none at all
  * They add an email address and password for their account
  * They may access the rest of the site

Once the account setup is complete, the user may no-longer access the site
with the access code they were provided.

Group Codes
-----------

One additional feature of ``djangotailoring.accounts`` is the concept of
Group Codes. A group code is a single access code that, when used to log in,
generates a new, unique access code which is assigned to the user and used
throughout the sign-up process. There are no limits to the amount of group
codes that are available. Group access codes can have limits on how many
times they may be used.

Functions
=========

.. function:: def account_setup_complete(user)

  :param user: the user to inspect
  :type user: a :mod:`django.contrib.auth` User instance
  :rtype: a boolean
  :returns: whether the user account is assigned an email address and
    password.
