****************************
``djangotailoring.tracking``
****************************

.. module:: djangotailoring.tracking

.. toctree::

  models
  eventnames
  decorators
  fields
  support
  views

The tracking application is dedicated to supporting the creation and
management of Events, and their associated objects. Events are records that
fundimentally include names and timestamps. Apps are free to create events
with any name, and use them for whatever features they wish. Events can also
have a free-text note, as well as a GenericForeignKey relation to any other
Django-managed object.

Functions
=========

.. function:: create_event(name, request=None, user=None, note=None, related_object=None)
  
  :param name: the event name
  :type name: a string
  :param request: the request in whose context this event is created
  :type request: a Django HttpRequest object
  :param user: the user for which this event is associated
  :type user: a :mod:`django.contrib.auth` User
  :param note: a free-form note for this event
  :type note: a string
  :param related_object: an associated model object for this event
  :type related_object: a Django Model instance
  :rtype: a :class:`djangotailoring.tracking.models.Event` instance
  :returns: a persisted Event with the given parameters.
  
  A convenience function for the creation of events, especially when created
  in the context of an HttpRequest.
  
  Make an Event record for a given set of parameters. If request is given, the
  user is pulled from the request, and in the absense of a note, the note is
  set to the request path.

Auto-created Events
===================

While most :class:`Event <djangotailoring.tracking.models.Event>`\s are
created explicitly by your code, there are a few events that are automatically
created when this application is installed.

Login/Logout
------------

Events are written whenever a user logs in or out of the current site. The
events are:

  * :attr:`djangotailoring.tracking.EventNames.UserLoggedIn`
  * :attr:`djangotailoring.tracking.EventNames.UserLoggedOut`

