*******************************
``djangotailoring.userprofile``
*******************************

.. module:: djangotailoring.userprofile

A major convenience for tailoring users with ``djangotailoring`` is
associating a Profile object with :mod:`django.contrib.auth` User objects. In
doing so, a number of view classes can expect tailoring subject data to be
available easily on every request. To facilitate this optional, yet powerful
feature, ``djangotailoring`` provides an abstract Profile class that provides
the functionality to make this process simple.

.. warning:: As of the current version of ``djangotailoring``, if you use the
  BaseUserProfile class, you **must** also add the
  :mod:`djangotailoring.tracking` application to your INSTALLED_APPS list.
  This is because, by default, BaseUserProfile inherits from
  :class:`djangotailoring.tracking.support.LatestEventMixin`.

Models
======

.. class:: BaseUserProfile
  
  An abstract model class which provides the :attr:`tailoringsubject`
  attribute, among other features, to make using the View classes simple.
  In addition to the functions available here, it is mixed with
  :class:`djangotailoring.tracking.support.LatestEventMixin` for additional
  convenience, including :meth:`LatestEventMixin.latest_event` and
  :meth:`LatestEventMixin.latest_event_date`
  
  .. attribute:: subjectloaderclass
    
    A reference to an object that follows the
    :ref:`SubjectLoader <subject-loader-infrastructure>` protocol. This
    SubjectLoader will be used to with :attr:`tailoringid` to handle
    :attr:`tailoringsubject` creation, storage and deletion.
  
    By default, it is assigned the return value of
    :func:`djangotailoring.project.getsubjectloader`
    
  .. attribute:: user
    
    A ForeignKey reference to the associated django.contrib.auth User object.
    
  .. attribute:: accepted_consent
  
    A Nulltable boolean field indicating whether a user has accepted or
    declined a study’s consent process. ``None`` indicates that the user has
    done neither.
  
  .. attribute:: withdrawn_reason
  
    A 64-character-long string field that can be used to store a short
    description of why a user has been withdrawn from a study. If a user has
    any ``withdrawn_reason`` set, it is assumed to be no longer active.
  
  .. attribute:: updated
  
    The timestamp for when this Profile object was last saved to the database.
  
  .. attribute:: created
  
    The timestamp for when this Profile object was created in the database.
  
  .. attribute:: tailoringid
  
    The string which is used when asking :attr:`subjectloaderclass` to load,
    store, or delete the :attr:`tailoringsubject`. By default, this is a
    read-only property equal to ``self.user.id``.
  
  .. attribute:: tailoringsubject
  
    A tailoring2 subject instance for the associated django.contrib.auth User
    object.
    
    By default, it is a read/write/delete-able property backed by
    :attr:`subjectloaderclass` using :attr:`tailoringid` as the subjectid.
  
  .. method:: is_active_participant(self)
  
    Provides a notional indication of whether a user is in-fact active as a
    study participant. This is true if :attr:`accepted_consent` is True and
    :attr:`withdrawn_reason` is set to anything other than ``None`` or the
    empty string.
  
  .. method:: characteristic_value(self, valuename[, source=''])
  
    :param valuename: the characteristic to look up
    :type valuename: a string
    :param source: the source in which to lookup ``valuename``
    :type source: a string
    :rtype: an object appropriately typed to the characteristic type


Functions
=========

.. function:: register_profile_post_save_handler(profileclass)

  :param profileclass: class that should be registered
  :type profileclass: a subclass of :class:`BaseUserProfile`
  
  Registers a database signal handler to create an instance of
  ``profileclass`` whenever a :mod:`django.contrib.auth` User object is
  created.

