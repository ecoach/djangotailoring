***********************************
``djangotailoring.views.localized``
***********************************

.. module:: djangotailoring.views.localized

Search Order
============

``djangotailoring`` attempts to provide thorough internationalization and
localization support. The set of view classes defined here use the following
search order to determine which locale to use for tailoring.

1. ``request.LANGUAGE_CODE``
2. the base language of ``request.LANGUAGE_CODE``
3. ``settings.LANGUAGE_CODE``
4. ``'en'``
5. ``''``
6. ``None``

Localized Document Dictionaries
-------------------------------

In the views below, documents are attached to locales in a dictionary mapping.
The structure of the dictionary is as follows::

  {
      locale: document_path,
      other_locale: other_document_path,
      # ...,
  }

Example
-------

Consider a view where two documents are defined::

  {
    'en': 'Messages/en/Welcome.messages',
    'es': 'Messages/es/Welcome.messages',
  }

1. If the view were accessed by a user with their locale set to ``en``, for
   English, ``'Messages/en/Welcome.messages'`` would be rendered in the view.
   This is because there is an exact match for the user’s locale in the
   mapping.

2. If the view were accessed by a user with their locale set to ``es-mx``, for
   Spanish/Mexican, ``'Messages/es/Welcome.messages'`` would be rendered in
   the view. This is because there is no match for ``es-mx`` in the view,
   however, there is one for the base-langauge of ``es-mx``, ``es``.

3. However, if the view were accessed by a user with their locale set to
   ``fr``, ``'Messages/en/Welcome.messages'`` would be chosen, as there is no
   matching document for that locale, and the ``en`` choice is defaulted to in
   this case.

.. note:: Additional localized strings within the application, such as
  message substitutions, will be localized per the view's selected lanaguage.
  For instance, even if there are French localization strings for this example
  view, in situation 3 above, any substitutions will be rendered in English,
  as that is the assumption for the language of the selected message document.

Views
=====

As with the :mod:`djangotailoring.views.tailoring` view classes, there are two
types of view classes in ``localized``, a pair of base classes, and a pair
of directly usable classes. Each pair consists of a single-document view, and
a multi-document view.

Base Views
----------

.. class:: BaseLocalizedTailoredDocView

  A base for generic views that tailor MTS message documents based on a
  user’s locale.
  
  This is a subclass of
  :class:`BaseTailoredDocView`, and behaves
  similarly, however, instead of using the
  :attr:`BaseTailoredDocViewmessage_document` attribute, it
  uses its own :attr:`localized_documents` as described below.
  
  There are three attributes:
  
  .. attribute:: localized_documents
    
    **required** A dict-like object that maps locale names to message
    document paths. Its default is an empty dictionary.
  
  .. attribute:: context_treq_name
    
    serves the same function as described for
    :class:`BaseTailoredDocView`. The default is ``'treq'``.
  
  .. attribute:: template_name
    
    **required** inherited from
    :class:`django.views.generic.base.TemplateView`.
  
  In addition to the methods available in :class:`BaseTailoredDocView`, there
  is one extra customizable method available for overriding the attributes
  above.
  
  .. method:: get_localized_documents(self)
  
    Provides the localized_documents dictionary to the view.
  

.. class:: BaseMultipleLocalizedTailoredDocView

  A base for generic views that tailor multiple MTS message documents in a
  single template based on a user’s locale.
  
  This is a subclass of
  :class:`BaseMutipleTailoredDocView`, and
  uses the same attributes and methods. However, the format of the attribute
  :attr:`message_documents` is different.
  
  There are two attributes:
  
  .. attribute:: message_documents
  
    **required** A mapping of :class:`TailoringRequest` context names to
    localized document mappings. For example::
    
      message_documents = {
        'treq1': {
          'en': 'Messages/English.messages',
          'es': 'Messages/Spanish.messages',
        },
        'treq2': {
          '': 'Messages/UniversalGraphics.messages'
        }
      }
    
  .. attribute:: template_name

    **required** inherited from
    :class:`django.views.generic.base.TemplateView`.

Public Views
------------

.. class:: LocalizedTailoredDocView

  Blends :class:`BaseLocalizedTailoredDocView` with
  :class:`UserProfileSubjectMixin` to make a turn-key tailoring view. It
  requires the same attributes/overrides as ``BaseLocalizedTailoredDocView``.

.. class:: MultipleLocalizedTailoredDocView

  Blends :class:`BaseMultipleLocalizedTailoredDocView` with
  :class:`UserProfileSubjectMixin` to make a turn-key mutli-document tailoring
  view. It requires the same attributes/overrides as
  ``BaseMultipleLocalizedTailoredDocView``.
  

