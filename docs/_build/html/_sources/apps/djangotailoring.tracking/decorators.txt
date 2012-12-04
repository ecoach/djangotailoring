***************************************
``djangotailoring.tracking.decorators``
***************************************

Decorators
==========

.. module:: djangotailoring.tracking.decorators

.. function:: log_page_view(f)
  
  :param f: the wrapped view callable
  :type f: a Django view callable
  :rtype: a Django view callable
  
  Acts as a wrapper for any callable Django view that returns an
  :class:`django.core.http.HttpResponse`. When the view returns a response,
  its :attr:`status_code` attribute is checked. If the status_code is 200, a
  :attr:`djangotailoring.tracking.eventnames.EventNames.PageViewed` event is
  created. Otherwise, if the response is a redirect, a
  :attr:`djangotailoring.tracking.eventnames.EventNames.Redirected` event is
  created with the request path and destination path attached in the note. In
  any other case, a
  :attr:`djangotailoring.tracking.eventnames.EventNames.PageError` event is
  created with the path and response code attached to the note.

