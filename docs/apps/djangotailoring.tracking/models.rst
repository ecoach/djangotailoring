***********************************
``djangotailoring.tracking.models``
***********************************

.. module:: djangotailoring.tracking.models

The heart of the ``djangotailoring.tracking`` application is here: the
:class:`Event` class. Nearly all operations involve this model in
one way or another. While you may create an :class:`Event` using the usual
methods, consider using the :func:`djangotailoring.tracking.create_event`
function for convenience.

Models
======

.. class:: Event

  A Django model object that represents a single, named historical event.
  Events can be directly related to :mod:`django.contrib.auth` User objects,
  and generically related to any other model object. Additionally, there is a
  255 character note field for storing any additional contextual information
  necessary.
  
  When querying, there is a default ordering, which is most recent events
  first.

  .. attribute:: user
  
    A foreign key relation to :class:`django.contrib.auth.models.User`. This
    is nullable, for events unrelated to any user. The default is ``None``.
  
  .. attribute:: name
  
    **required** A 100 character long string identifying the type of event
    occurrence. While there are some preset names, there is no requirement
    that any pattern or convention is followed.
  
  .. attribute:: timestamp
  
    A datetime object defining when the event occurred. By default, it is set
    to the database creation time of the event.
  
  .. attribute:: note
  
    A 255 character long string containing any information. There are no
    restrictions on content other than length. The default is the empty
    string.
  
  .. attribute:: related_object
  
    A :class:`django.contrib.contenttypes.generic.GenericForeignKey`
    referencing another model object. This field is nullable. A related object
    can be anything that you wish to associate with an event, whether it be
    an additional User object, or a particular
    :class:`djangotailoring.models.SubjectData` instance. Anything.
  
  .. classmethod:: events_related_to(cls, related_object)
    
    :param related_object: any Django Model instance
    :rtype: a QuerySet of Events
    :returns: all events referencing related_object
    
    .. note::
      This method works well, but may be more idiomatic if it were handled by
      a custom Manager class. Also, if this is a frequent action on a
      particular Model type, consider using
      :class:`django.contrib.contenttypes.generic.GenericRelation` on that
      Model class.
    
  
Events and Logging
==================

Since events can be thought of as persisted, queryable logging statements, all
events are automatically logged using the python logging library.

The logger name is ``djangotailoring.tracking.events``. All events are logged
at the INFO level.

.. note::
  An additional feature of the event logging is that if an :class:`Event` is
  saved with a :attr:`request` attribute, that ``request`` is available in the
  ``extras`` dictionary attached to the :class:`LogRecord`. The ``request``
  is not persisted to the database, but merely used as a convenience for
  logging handlers in the case where the knowledge about the context in which
  the event was created is important.
