************************************
``djangotailoring.tracking.support``
************************************

.. module:: djangotailoring.tracking.support

Mixins
======

.. class:: LatestEventMixin
    
    Provides easy access to specific user events on an object with a user
    attribute. In particular,
    :class:`djangotailoring.userprofile.BaseUserProfile` borrows this.
    
    .. method:: latest_event(self, eventname=None)
    
      :param eventname: the name of an event to search for
      :type eventname: a string
      :rtype: :class:`djangotailoring.tracking.models.Event` or ``None``
      :returns: the Event instance whose name is ``eventname`` and has the
        future-most timestamp. If ``eventname`` is ``None``, then any event
        associated with the user is returned. If there are no matching events,
        ``None``.
    
    .. method:: latest_event_date(self, eventname=None)
    
      :param eventname: the name of an event to search for
      :type eventname: a string
      :rtype: a :class:`datetime.datetime` instance, or ``None``
      :returns: the timestamp of the latest event per :meth:`latest_event`
  

