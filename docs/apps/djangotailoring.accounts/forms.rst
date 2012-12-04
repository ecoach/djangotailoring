**********************************
``djangotailoring.accounts.forms``
**********************************

.. module:: djangotailoring.accounts.forms

A set of forms are provided for helping with authentication and user creation.
When a user has an incomplete account (that is, without either a valid email
address or a valid password), they may authenticate using just an access code.
If they have a valid account, they may use their email address and chosen
password to do the job. Both authentication forms are provided. Additionally,
a User completion form is available to help the user from make a valid user
account.

Authentication Forms
====================

Both forms are drop-in replacements for the login form of the built-in view
:func:`django.contrib.auth.views.login`

.. class:: EmailAuthenticationForm(request=None, *args, **kwargs)

  Provides users with a login form with two fields:
  
  * “Email Address” (``email``)
  * “Password” (``password``)
  
  This is useful in conjunction with
  :class:`djangotailoring.accounts.backends.EmailModelBackend`

.. class:: AccessCodeForm(request=None, *args, **kwargs)

  Provides users with a login form with one field:
  
  * “Access Code” (``accesscode``)
  
  This is useful in conjunction with
  :class:`djangotailoring.accounts.backends.AccessCodeBackend` and the like.


User Account Completion Forms
=============================

.. class:: CompleteUserForm(user, *args, **kwargs)

  :param user: the user to update.
  :type user: a :mod:`django.contrib.auth` User instance
  
  Provides users with a form with three fields:
  
  * “Email Address” (``email``)
  * “Password” (``password1``)
  * “Password” (again) (``password2``)
  
  This validates that a user's email address is legitimate and unique, and has
  input two matching passwords.
  
  .. method:: save(self[, commit=True])
    
    :param commit: instructs 
    :type commit: a boolean
    :rtype: a :mod:`django.contrib.auth` User instance
    
    Assigns the email address and password to the :attr:`user`. ``commit``
    controls whether the user is saved, or returned unsaved.
  
