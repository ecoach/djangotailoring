***************************************
``djangotailoring.tracking.eventnames``
***************************************

.. module:: djangotailoring.tracking.eventnames

This module contains a single class whose purpose is to encapsulate a set of
general event names for use in any application. While this set is available,
there is not requirement to use it.

EventNames
==========

The EventNames namespace simply contains attribute values associated with
strings of attribute names. The standard set is:

.. class:: EventNames
  
  .. attribute:: UserCreated = 'UserCreated'
  
  .. attribute:: UserPasswordChanged = 'UserPasswordChanged'
  
  .. attribute:: UserEmailSent = 'UserEmailSent'
  
  .. attribute:: UserConsented = 'UserConsented'
  
  .. attribute:: UserActivated = 'UserActivated'
  
  .. attribute:: UserWithdrawn = 'UserWithdrawn'
  
  .. attribute:: UserReset = 'UserReset'
  
  .. attribute:: UserLoggedIn = 'UserLoggedIn'
  
    This is automatically created by ``djangotailoring.tracking`` when a user
    logs in.
  
  .. attribute:: UserLoggedOut = 'UserLoggedOut'
  
    This is automatically created by ``djangotailoring.tracking`` when a user
    logs out.
  
  .. attribute:: PageViewed = 'PageViewed'
  
    This is automatically created by
    :func:`djangotailoring.tracking.decorators.log_page_view` when a user
    visits a decorated view whose response status code is ``200``.
  
  .. attribute:: PageError = 'PageError'
  
    This is automatically created by
    :func:`djangotailoring.tracking.decorators.log_page_view` when a user
    visits a decorated view whose response status code is anything but ``200``
    or ``302``.
  
  .. attribute:: Redirected = 'Redirected'
  
    This is automatically created by
    :func:`djangotailoring.tracking.decorators.log_page_view` when a user
    visits a decorated view whose response status code is ``302``.
  
