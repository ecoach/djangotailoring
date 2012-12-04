****************************************
``djangotailoring.surveys.views.render``
****************************************

.. module:: djangotailoring.surveys.views.render

Classes
=======

.. class:: SurveyRenderChunk(tree, subject, treq, page_data, show_errors, request_errors=None):

  :param tree: The MTS Messages tree for the current survey page
  :type tree: an :class:`ElementTree` instance
  :param subject: the current subject *with* current survey data
  :type subject: a :class:`tailoring.subjects.Subject` instance
  :param treq: the TailoringRequest for the current page
  :type treq: a :class:`.TailoringRequest` instance
  :param page_data: the map of characteristic names to values for the current
    page.
  :type page_data: a dictionary
  :param show_errors: dictates whether ``validate`` commands in the tree will
    be shown or not.
  :type show_errors: a boolean
  :param request_errors: the list of type errors that will be re-inserted into
    the rendered output.
  :type request_errors: a list of :class:`surveytracking.projectutils.InvalidDataError`\s

  Encapsulates all of the relevant information to send to the tailoring engine
  for rendering a single page of a survey.
  
  Clients will primarily be familiar with this as the context item that the
  :ref:`render_survey_segment` tag uses to output a page of survey form
  elements.
  
  .. method:: has_content(self)
  
    :rtype: a boolean
    :returns: whether the current tailored output has any renderable content.
  
  .. method:: has_errors(self)
  
    :rtype: a boolean
    :returns: whether the set of objects will result in any errors.
  
  .. method:: render(self)
  
    :rtype: an :class:`ElementTree` instance
    :returns: a rendered ElementTree of the final HTML-ified survey output.
  
