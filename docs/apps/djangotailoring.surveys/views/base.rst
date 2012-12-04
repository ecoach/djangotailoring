**************************************
``djangotailoring.surveys.views.base``
**************************************

.. module:: djangotailoring.surveys.views.base

Background
==========

Survey View classes have a lot of complicated methods that are designed to be
easily overridden and allow you to keep your mitts off of the nasty bits of
survey rendering and error handling.

Each Survey View is responsible for handling all of the pages for a particular
Survey. Each request made to the view should have some way of communicating
which page the user is on, and which user is requesting the page.

By default, the values are derived as follows:

* The page is identified by a unique MTS Message ID of an element within the
  page, which is derived from a URL/Request parameter ``page_id``.
* The user is identified by the
  :class:`djangotailoring.subjects.SubjectLoader`\-compatible ID returned by
  :meth:`BaseSurveyView.get_user_id`.

Exceptions
==========

.. exception:: PageNotFound

  Raised by Survey View classes when the requested Page is not found in the
  current Survey document structure.

.. exception:: StateNotFound
  
  Raised by Survey View classes when no state is found for the page/user pair.

BaseSurveyView Class
====================

Attributes
----------

.. class:: BaseSurveyView

  A subclass of :class:`django.views.generic.base.TemplateView` that will
  render a template with a survey ‘chunk’ per the request’s user and page
  pair.
  
  .. attribute:: survey_manager = None
  
    A reference to a :class:`surveytracking.classes.SurveyManager` object.
    This is accessed by way of :meth:`get_survey_manager`.
  
  .. attribute:: survey_id = None
  
    A unique name of the current survey used when serializing State objects.
    This is accessed by way of :meth:`get_survey_id`.
  
  .. attribute:: context_chunk_name = 'chunk'
  
    The name of the :class:`djangotailoring.surveys.render.SurveyRenderChunk`
    instance passed to the rendering context. 
  

Attribute Getters
-----------------
    
.. method:: BaseSurveyView.get_survey_id(self)

  :rtype: a string
  :returns: a unique identifier for the survey which is used to distinguish it
    from other surveys in the State serialization structure.
  
  By default, this returns :attr:`survey_id`.

.. method:: BaseSurveyView.get_user_id(self)
  
  :rtype: a string
  :returns: a user id which is used to locate the appropriate State for the
    current request. It should be compatible with a
    :class:`djangotailoring.subjects.SubjectLoader`.
  
  **required** This method must be overridden.

.. method:: BaseSurveyView.get_survey_manager(self)

  :rtype: a :class:`surveytracking.classes.SurveyManager` instance
  :returns: the active survey manager to handle page transitions and other
    survey mechanics.
  
  By default, this returns :attr:`survey_manager`.
    
.. method:: BaseSurveyView.get_project(self)

  :rtype: a :class:`tailoring2.project.BasicProject` instance
  :returns: the current Project instance.
  
  By default, this is the current survey manager's project.

.. method:: BaseSurveyView.get_subject(self)

  :rtype: a :class:`tailoring2.subjects.Subject` instance
  :returns: the current subject being used for the survey.
  
  **required** This method must be overridden.
  
  The subject *does not* need to be constantly updated with the responses from
  the survey, since those are automatically combined with the running survey
  data loaded from the current survey state in :meth:`get_request_subject`.

.. method:: BaseSurveyView.get_request_subject(self)

  :rtype: a tuple of (a :class:`tailoring2.subjects.Subject` instance,
    a list of subject generation errors)
  :returns: the current subject *with* all of the survey response data up to
    the current page of the survey, along with any errors in generating that
    subject.
  
  The subject is based on the current state data, and the subject returned by
  :meth:`get_subject`. A new subject is created, so no damage is done to
  either the request data, or the subject returned from :meth:`get_subject`.

.. method:: BaseSurveyView.get_tailoring_request(self)

  :rtype: a :class:`djangotailoring.tailoringrequest.TailoringRequest`
    instance
  :returns: a TailoringRequest instance that *will be* modified to suit the
    current survey request's needs.
    
  By default, it returns an empty TailoringRequest instance.

.. method:: BaseSurveyView.get_active_source(self)

  :rtype: a string
  :returns: the name of the source that data is inserted to.
  
  By default, it checks the TailoringRequest returned by
  :meth:`get_tailoring_request` for a :attr:`default_source` value. If that
  doesn’t exist, it returns the source of the current survey manager.

.. method:: BaseSurveyView.get_current_page(self)

  :rtype: a :class:`surveytracking.classes.Page` instance
  :returns: the page for the current request.

..
  Internal getters:
  
  .. method:: BaseSurveyView.subject_with_additional_data(self, data)
  
  .. method:: BaseSurveyView._get_tailoring_context(self, subject=None)

Traversal Handlers
------------------

.. method:: BaseSurveyView.can_pass_page(self[, subject=None])

  :param subject: the subject to test against.
  :type subject: a :class:`tailoring2.subjects.Subject` instance
  :rtype: a boolean
  :returns: whether ``subject`` can advance beyond the current page.
  
  A user can pass the page if there are no validation errors on the current
  page. If there are no previous errors, and there are any loose validation
  errors, a user cannot pass the current page.
  
  If subject is None, then it will test with the subject made with
  :meth:`get_request_subject`.

.. method:: BaseSurveyView.get_render_chunk(self[, show_errors=None])

  :rtype: :class:`.SurveyRenderChunk` instance
  :returns: the chunk that is passed to the template context for the current
    request.

..
  Internal Traversal Handlers:

  .. method:: BaseSurveyView._can_pass_page(self, page, context, ignore_loose_validation)
  
  .. method:: BaseSurveyView._next_page_with_content(self)

  .. method:: BaseSurveyView.is_valid_submission(self)


Navigation Handlers
-------------------

.. method:: BaseSurveyView.get_base_url(self)

  :rtype: a string
  :returns: the absolute URL to this survey view, with the page_id stubbed out
    as the string-formatting parameter '%s'.
  
  This is used to build URLs for redirects within the current survey view.

.. method:: BaseSurveyView.url_for_page_id(self, page_id)

  :param page_id: the ID for the page you wish to have the URL for
  :type: a string
  :rtype: a string
  :returns: the absolute URL to the passed survey page.

.. method:: BaseSurveyView.get_previous_url(self)

  :rtype: a string
  :returns: the absolute URL to the previous survey page.

.. method:: BaseSurveyView.redirect(self, page=None, page_id=None)

  :param page: the page you wish to redirect to
  :type page: a :class:`surveytracking.classes.Page` insance
  :param page_id: the ID of the page you wish to redirect to
  :type page_id: a string
  :rtype: a :class:`django.http.HttpResponse`
  :returns: a response that temporarily redirects the user to the requested
    page.


Request Data Conversion
-----------------------

.. method:: BaseSurveyView.get_request_data(self)

  :rtype: a :class:`django.http.QueryDict` instance
  :returns: the Query dictionary to search for survey data.
  
  By default, this returns :attr:`self.request.POST`.

.. method:: BaseSurveyView.get_request_survey_data(self)

  :rtype: a tuple of (dictionary, list of errors)
  :returns: a converted set of survey answers found in the request data.
  
  This method packs a serious punch. All data in the QueryDict returned by
  :meth:`get_request_data` is sifted through and coercion from string to
  MTS Dictionary type is attempted. Any errors found during that conversion
  are caught and inserted into the list of errors returned as well.

..
  Internal Data Conversion methods:
  
  .. method:: BaseSurveyView.get_context_data(self, **kwargs)

  .. method:: BaseSurveyView._request_value_for_chardef(self, chardef)

  .. method:: BaseSurveyView._tailoring_value_for_chardef(self, chardef)
  

..
  Internal Dispatch Handler methods:
  
  Dispatch Handlers
  -----------------
  
  .. method:: BaseSurveyView.init_locals(self)

  .. method:: BaseSurveyView.get(self, request, *args, **kwargs)
  
  .. method:: BaseSurveyView.post(self, request, *args, **kwargs)
  
  .. method:: BaseSurveyView.render_to_response(self, context, **response_kwargs)
    

View Handlers
-------------

.. method:: BaseSurveyView.can_access_survey(self)

  :rtype: a boolean
  :returns: whether the user requesting the current page should be allowed to
    access the current survey.
  
  If this is false, the view will return the result of
  :meth:`handle_bad_page_request` is given to the client.
  
  Returns ``True`` by default.

.. method:: BaseSurveyView.handle_bad_page_request(self)

  :rtype: a :class:`django.http.HttpResponse` instance
  :returns: a response that indicates that a page is inaccessible.
  
  Returns a “403 Forbidden” response by default.

.. method:: BaseSurveyView.handle_end_of_survey(self)
  
  :rtype: a :class:`django.http.HttpResponse` instance
  :returns: a response that indicates that the survey has been completed,
    such as redirecting to an acknowledgement page.
  
  Redirects a user to the root page of the site (``/``) by default.

.. method:: BaseSurveyView.on_successful_page_request(self)

  Once a request is determined to be for a known page with a known State, this
  method is called.
  
  There is no default implementation.

.. method:: BaseSurveyView.on_valid_submission(self)
  
  Once a POST request is determined to be free of validation errors, this
  method is called.
  
  There is no default implementation.

.. method:: BaseSurveyView.on_invalid_submission(self)

  If a POST request is determined to have one or more validation errors, this
  method is called.
  
  There is no default implementation.

State handlers
--------------

.. method:: BaseSurveyView.get_current_state(self)

.. method:: BaseSurveyView.get_latest_state(self)

.. method:: BaseSurveyView.create_next_state(self, next_page)

.. method:: BaseSurveyView.create_initial_state(self)

.. method:: BaseSurveyView.state_subject_data(self, state)

.. method:: BaseSurveyView.state_has_validation_errors(self, state)

.. method:: BaseSurveyView.on_validation_error(self, state)

.. method:: BaseSurveyView.get_previous_page(self, state)

.. method:: BaseSurveyView.redirect_to_state(self, state)

.. method:: BaseSurveyView.set_state_request_data(self, state, data)

.. method:: BaseSurveyView.save_state(self, state)

.. method:: BaseSurveyView.state_for_restart(self)

..
  Internal State Handlers:
  
  .. method:: BaseSurveyView._get_state_for_page(self, page=None)
  

SimpleSurveyView Class
======================

.. class:: SimpleSurveyView
  
  Subclass of :class:`BaseSurveyView` to create a self-contained Survey view
  for a specified Survey Document and source.

  .. attribute:: survey_document
    
    A path to an MTS survey, optionally relative to the current project.
    
  .. attribute:: source
  
    A string representing the name of the source that survey data will be
    stored.
  

SinglePageSurveyView Class
==========================

.. class:: SinglePageSurveyView

  Subclass of :class:`BaseSurveyView` to build a view that assumes that
  the Survey document consists of a single page. This removes the requirement
  that the view have a page_id keyword argument. Attributes operate the same
  as :class:`SimpleSurveyView` as it also derives from
  :class:`NoManagerMixin`.

Mixins
======

.. class:: AutoSaveSubjectDataMixin

  Calls save_subject when a user submits a valid request on a survey page.

.. class:: NoManagerMixin
  
  Automatically creates a SurveyManager based on two parameters for use
  in a SurveyView. Simplifies the creation of a survey view down to a single
  subclass with class attributes rather than having to create a manager
  out-of-band.
  
  .. attribute:: survey_document = None
  
    A path to an MTS survey, optionally relative to the current project.
    This is accessed by way of :meth:`get_survey_document`.
  
  .. attribute:: source = None
  
    A string representing the name of the source that survey data will be
    stored. This is accessed by way of :meth:`get_source`.
  
  .. method:: get_survey_document(self)
  
    :rtype: a string
    :returns: a path to an MTS sruvey document.
  
    By default, this returns :attr:`survey_document`.
  
  .. method:: get_source(self)
  
    :rtype: a string
    :returns: a string identifying the active source for the survey.
  
    By default, this returns :attr:`source`.
  
