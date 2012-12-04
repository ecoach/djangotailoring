*************************
``djangotailoring.views``
*************************

.. module:: djangotailoring.views

Contents:

.. toctree::
   
   tailoring
   protection
   localized

The ``views`` package of djangotailoring has three modules that contain 
generic views for different scenarios.

* :mod:`djangotailoring.views.tailoring` contains views for rendering
  templates with content derived from one or more message documents.
  
* :mod:`djangotailoring.views.localized` contains views that extend the
  views in the ``tailoring`` module by supporting the selection of message
  document based on an individual's selected locale.

* :mod:`djangotailoring.views.protection` contains a view mixin useful for
  restricting access to a page to logged-in users.

