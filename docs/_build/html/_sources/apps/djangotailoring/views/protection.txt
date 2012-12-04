************************************
``djangotailoring.views.protection``
************************************

.. module:: djangotailoring.views.protection

Protection provides a pair of Mixin classes that automatically redirect users
in a particular state when accessing the page.

Mixins
======

.. class:: UserPassesTestMixin

  A mix-in class that validates that the requesting user meets a certain set
  of criteria. This leverages Django’s
  :func:`django.contrib.auth.decorators.user_passes_test` decorator. The
  attributes below are passed to the decorator as well. The test is provided
  by overriding the :meth:`user_passes_test` method.
  
  .. attribute:: login_url
  
    See `the Django documentation for login_required <http://docs.djangoproject.com/en/1.3/topics/auth/#the-login-required-decorator>`_
    for more information.
  
  .. attribute:: redirect_field_name
  
    See `the Django documentation for login_required <http://docs.djangoproject.com/en/1.3/topics/auth/#the-login-required-decorator>`_
    for more information.
  
  In addition, the following methods provide access to the above attributes:
  
  .. method:: get_login_url(self)
  
    Used when determining what to pass as the ``login_url`` to the test
    decorator. By default, returns :attr:`login_url`.
  
  .. method:: get_redirect_field_name(self)
  
    Used when determining what to pass as the ``redirect_field_name`` to the
    test decorator. By default, returns :attr:`redirect_field_name`.
  
  Finally, the actual test that is performed on the user is done in:
  
  .. method:: user_passes_test(self, user)
  
    :rtype: a boolean
    :returns: whether ``user`` should be able to access the view.
    
    By default, returns ``True``. For more information, see
    `the user_passes_test documentation <http://docs.djangoproject.com/en/1.3/topics/auth/#django.contrib.auth.decorators.user_passes_test>`_

.. class:: LoginRequiredMixin

  A mix-in class that forces any access of the implementing view
  class to be accessible only to logged-in users. The behavior is the same as
  django’s :func:`django.contrib.auth.decorators.login_required` decorator.
