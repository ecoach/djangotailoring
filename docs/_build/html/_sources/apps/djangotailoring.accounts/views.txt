**********************************
``djangotailoring.accounts.views``
**********************************

.. module:: djangotailoring.accounts.views

Views
=====

.. function:: login(*args, **kwargs)

  A clone of :class:`django.contrib.auth.views.login` that uses
  :class:`djangotailoring.accounts.forms.EmailAuthenticationForm` rather than
  the standard form. See the official Django documentation for the behavior
  and arguments of this function.

.. function:: validate_access_code(request, redirect_url=None, template_name='accounts/accesscodelogin.html')

  :param request: the current request
  :type request: a Django HttpRequest object
  :param redirect_url: the url to redirect to on successful login, if ``None``
    then it is presumed to be '/'
  :type redirect_url: a string
  :param template_name: the name of the template to use for rendering the page
  :type template_name: a string or list of strings
  
  A simple view that handles login via
  :class:`djangotailoring.accounts.forms.AccessCodeForm`.
