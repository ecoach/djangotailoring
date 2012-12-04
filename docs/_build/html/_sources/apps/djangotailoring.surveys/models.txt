**********************************
``djangotailoring.surveys.models``
**********************************

.. module:: djangotailoring.surveys.models

Generally, you will not have to deal with the model classes in this module
directly. The class is used by
:class:`djangotailoring.surveys.views.base.BaseSurveyView` as part of its
state management system.

Models
======

.. class:: SurveyState
  
  Encapsulates all of the data necessary to rebuild where a user was in a
  survey at a given point in time. SurveyState objects should be created
  before a user has access to the associated page.
  
  .. attribute:: user_id
  
    A string that represents a unique user ID. The ID can be anything, as long
    as it is the same as that used by the tailoring views for their subject
    id.
  
  .. attribute:: survey_id
  
    A string that identifies the survey that the state belongs to.
  
  .. attribute:: page_msgid
  
    A string that uniquely identifies which page this state belongs to. This
    is an MTS Message ID found somewhere within one and only one page.
  
  .. attribute:: running_subject_data
  
    A dictionary of characteristic names mapped to values. The dictionary is a
    union of all answers given by the in the survey for this state, and all
    previous states.
  
  .. attribute:: latest_page_data
  
    A dictionary of characteristic names mapped to values. The dictionary is a
    set of responses given at the most recent submission to the page.
  
  .. attribute:: validation_errors
  
    A count of the number of times the user has submitted invalid data to this
    page.
  
  .. attribute:: previous_state
  
    A reference to another :class:`SurveyState`, identifying which state comes
    before it in a user’s path of the survey. If it is ``None``, it is assumed
    to be the starting state.
  
  .. attribute:: valid
  
    A boolean indicating whether the current state should be considered valid
    when searching for a page’s data.
  
  .. attribute:: created
  
    The time when the state was first created.
  
  .. attribute:: modified
  
    The time when the state was most recently changed.
    
  .. method:: invalidate_descendents(self)
  
    Find all :class:`SurveyState`\s that include this state as an ancestor,
    and set their :attr:`valid` attribute to False, and do the same for each
    state's progeny as well.
  
  .. method:: rebuild_running_subject_data(self)
  
    :rtype: a dictionary
    :returns: a dictionary of Characteristic names mapped to values.
    
    Dig through all of this state’s ancestors and build a dictionary of their
    values.
  
  .. method:: current_subject_data(self)

    :rtype: a dictionary
    :returns: a dictionary of Characteristic names mapped to values.
    
    A convenience method for overlaying the :attr:`latest_page_data` on top of
    :attr:`running_subject_data`.
  
