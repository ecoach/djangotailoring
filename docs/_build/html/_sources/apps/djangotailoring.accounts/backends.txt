*************************************
``djangotailoring.accounts.backends``
*************************************

.. module:: djangotailoring.accounts.backends

For users to be able to authenticate with AccessCodes and email addresses,
Authentication Backends are required. ``djangotailoring.accounts`` supplies
three of them.

Authentication Backends
=======================

All of the Authentication Backends are subclasses of
:class:`django.contrib.auth.backends.ModelBackend`.

Email Address Backends
----------------------

.. class:: EmailModelBackend

  Authenticates a user based on an email address and a password.
  
  Arguments:
  
  * ``email``
  * ``password``

AccessCode Backends
-------------------

.. class:: AccessCodeBackend

  Authenticates a user based on an accesscode alone. If there is an email
  address and password set, the user will **not** be authenticated.
  
  Arguments:
  
  * ``accesscode``
  
  .. attribute:: groupcode_class
  
    In cases where a user enters a Group access code, this backend will
    automatically create a new user and authenticate with that newly created
    user. For this to behave correctly, a reference to the proper
    :class:`GroupAccessCode` type is required. By default, it is simply
    :class:`djangotailoring.accounts.models.GroupAccessCode`.

.. class:: BasicAccessCodeBackend

  A version of AccessCodeBackend whose :attr:`groupcode_class` attribute is
  set to :class:`djangotailoring.accounts.models.BasicGroupAccessCode`.

