***********************************
``djangotailoring.tracking.fields``
***********************************

.. module:: djangotailoring.tracking.fields

The ``fields`` module provides a set of concrete model fields for
denormalizing model objects upon event creation. The merits of such an action
is left as a decision for the user, but for those in need, the infrastructure
is in place to both use the built-in fields, as well as create ones own, if
they so desire.

.. note::
  The denormalized field infrastructure assumes that the values are
  denormalized on a per-user basis, and therefore assume that the model has a
  ForeignKey relation to a :class:`django.contrib.auth.models.User` object
  called :attr:`user`.

Using Denormalized Fields
=========================

Denormalized model fields are functionally different than regular model
fields. In normal operation, you get a Model instance, assign values to the
fields as attributes, and likely call ``.save()`` on the instance.
Denormalized fields are read-only in practice; their values are not assigned
by you, rather, they are set outside of this normal fetch, modify, store
process.

When an event is created anywhere in the system, each model field
is notified. If the field's eventname matches an event, the field fetches any
instances of the Model related to the same user, and will update itself,
saving all instances back to the database.

.. warning::
  Due to this process, any in-memory Model objects will *not* have up-to-date
  information in their fields. To be sure you have the latest denormalized
  data, re-fetch those objects.

Fields
======

.. class:: DenormalizedEventTimestampField(eventname)

  A :class:`django.db.models.DateTimeField` subclass which accepts any
  additional arguments relating to that type. Any time an event of
  ``eventname`` is created for the associated :attr:`user`, the field will be
  updated to the timestamp of that event.
  
  For example, if a model were defined as::
  
    class MyModel(models.Model):
        user = models.ForeignKey(User)
        last_logout = DenormalizedEventTimestampField(Eventnames.UserLoggedOut)
      
  Whenever a a ``UserLoggedOut`` event was created for the user, their
  associated ``MyModel``\’s ``last_logout`` will be set to the timestamp of
  the event.

.. class:: DenormalizedEventCountField(eventname)

  A :class:`django.db.models.PositiveIntegerField` subclass which accepts any
  additional arguments relating to that type. Any time an event of
  ``eventname`` is created for the associated :attr:`user`, the field will be
  updated to the count of all similar events.
  
  For example, if a model were defined as::
  
    class MyModel(models.Model):
        user = models.ForeignKey(User)
        logged_in_count = DenormalizedEventCountField(EventNames.UserLoggedIn)
        
  
  Whenever a ``UserLoggedIn`` event was created for the user, their associated
  ``MyModel``\’s ``logged_in_count`` will be set to the number of
  ``UserLoggedIn`` events for that user.

Creating Your Own Fields
========================

Mixins
------

.. class:: DenormalizedEventFieldMixin

  Provides a bridge between a model field definition and an event set
  and a model with a .user reference. It will listen for the creation of the
  specified event, and set its value to that returned by get_value().

  .. method:: get_value(self, event)
    
    :param event: the newly created event instance.
    
    Override this method to return the value that the field will be assigned
    upon the creation of the specified event.
  

Integration with South
======================

`South <http://south.aeracode.org>`_ requires intimate knowledge of the types
of fields models it migrates. This application provides the introspection
information to South by default, so all models using these fields should be
migratable.
