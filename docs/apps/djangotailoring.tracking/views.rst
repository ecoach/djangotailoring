**********************************
``djangotailoring.tracking.views``
**********************************

.. module:: djangotailoring.tracking.views

View Mixins
===========

.. class:: LogPageViewMixin
  
  Can be mixed with any Django Generic View class to provide logging with
  the :func:`djangotailoring.tracking.decorators.log_page_view` decorator.
  
  For example::
  
    class LoggingRedirectToHomeView(LogPageViewMixin, RedirectView):
        url = '/'
  
  The above is a view that will redirect users to the home page of the site,
  and log that action on the way through.
