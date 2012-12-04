***********************************
``djangotailoring.views.tailoring``
***********************************

Views
=====

The view classes are divided into a pair of base classes, and a pair of
classes inheriting from the base with enough functionality to be used on their
own. 

Base Views
----------

.. module:: djangotailoring.views.tailoring

.. class:: BaseMultipleTailoredDocView

  As a subclass of ``TemplateView``, it renders a django template with
  multiple tailoring documents accessible in the template context. There are
  two required attributes to make this view function:
  
  .. attribute:: message_documents

    A dictionary-like object that builds at
    mapping of template context names to message document paths.
    For instance, if it is a dict of::
  
      {'treq1': 'Messages/Welcome.messages', 'treq2': 'Messages/Header.messages'},
  
    The template context would have two variables ``treq1`` and ``treq2`` that 
    reference the tailoring requests for the associated documents. The default
    is an empty dictionary.

  .. attribute:: template_name
  
    A string, or list of strings, that identify the template to render on
    request. The default is ``None``.
    
  All methods of :class:`django.views.generic.TemplateView` are available.
  When overriding, be sure to call the super method. In addition, there are
  three more methods that may be overridden:

  .. method:: get_subject(self)
  
    :rtype: tailoring2.Subject
  
    A method to override (generally by mixin) that returns a subject based on
    the active request. By default, it returns None. Implementors should
    override this method.

  .. method:: get_message_documents(self)
  
    :rtype: dictionary of context_name strings to document paths
  
    Override this method to customize the dictionary of message doc paths that
    is used for rendering in the format for the ``message_documents``. By
    default, it returns ``self.message_documents``

  .. method:: get_tailoring_request(self, doc)
  
    :param doc: message document path
    :rtype: djangotailoring.TailoringRequest for the current subject and doc

.. class:: BaseTailoredDocView()
  
  A subclass of :class:`BaseMultipleTailoredDocView`. Its purpose is to
  simplify the one Message document, one template scenario. Instead of using
  the :attr:`BaseMultipleTailoredDocView.message_documents` attribute and
  associated method, use the :attr:`message_document` attribute and associated
  method to define the functionality. It is functionally equivalent to
  defining a ``BaseMultipleTailoredDocView`` with message_documents set to::
  
    {self.context_treq_name: self.get_message_document()}
  
  .. attribute:: message_document
  
    A path to a message document. The path may be relative to the project or
    absolute.
  
  .. attribute:: context_treq_name
  
    A string. This is the variable name that will be used for the
    generated :class:`TailoringRequest`.
  
  As with ``BaseMultipleTailoredDocView``, you may override the following
  method to customize the rendering behavior:
  
  .. method:: get_message_document(self)
  
    Customize the path to the message document to tailor based upon any
    additional information. By default, it returns
    :attr:`self.message_document`.

Public Views
------------

.. class:: TailoredDocView

  Blends :class:`BaseTailoredDocView` with :class:`UserProfileSubjectMixin` to
  make a turn-key tailoring view. It requires the same attributes/overrides as
  ``BaseTailoredDocView``.

.. class:: MultipleTailoredDocView

  Blends :class:`BaseMultipleTailoredDocView` with
  :class:`UserProfileSubjectMixin` to make a turn-key mutli-document tailoring
  view. It requires the same attributes/overrides as
  ``BaseMultipleTailoredDocView``.
  

Mixins
======

.. class:: UserProfileSubjectMixin
  
  A tailoring view mixin class that provides a :meth:`get_subject()`
  implementation which returns a Subject instance return by the
  logged-in user's :attr:`UserProfile.tailoringsubject` attribute. In
  addition, it provides a few additional methods for access to certain
  fields of the user's profile.
  
  .. method:: get_subject(self)
    
    :rtype: :class:`tailoring2.Subject`
    
    Returns the request.user’s tailoring Subject instance.
    
  .. method:: get_profile(self)
    
    :rtype: a :class:`djangotailoring.userprofile.BaseUserProfile` instance
  
    A shortcut to get the user profile of the current request user.
  
  .. method:: get_user_id(self)
    
    :rtype: a String
  
    A shortcut to the tailoring id of the request user.
  
  .. method:: save_subject(self, subject)
    
    :param subject: a :class:`tailoring2.Subject` instance
  
    Stores the subject data using the request user’s profile’ subject loader.
  

