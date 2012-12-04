**********************
Tailoring View Recipes
**********************

In here, you will find a set of sample code that can be used to both steal for
actual use, as well as learn about possible ways of building the types of
functionality you need for your app.

In each recipe, if a template is provided, it is assumed that there is a
template called ``base.html`` that includes a block called ``content``.

Tailoring Views
===============

In this section, views pertaining to producing MTS Message documents are
outlined.

.. _basic_tailored_page:

A Basic Tailored Page
---------------------

Consider a situation where there is a Message document called
``Messages/MyTailoredDoc.messages`` in your MTS project folder, and it has
sections called 'Intro', 'Part1', and 'Part2'.

In ``myapp/views.py``::
  
  from djangotailoring.views import TailoredDocView
  
  class MyTailoredDocView(TailoredDocView):
      template_name = 'myapp/mypage.html'
      message_document = 'Messages/MyTailoredDoc.messages'
  
In ``templates/myapp/mypage.html``::

  {% extends "base.html" %}
  
  {% load tailoring2tags %}
  
  {% block content %}
    {% render_section treq "Intro" %}
    {% render_section treq "Part1" %}
    {% render_section treq "Part2" %}
  {% endblock %}

.. _enhanced_tailored_page:

An Enhanced Tailored Page
-------------------------

Using the same message doc from above in
:ref:`Basic Tailored Page <basic_tailored_page>`, you could also choose to
have the section choices be made by a parameter to the view.

In ``myapps/views.py``::

  from django.http import Http404
  from djangotailoring.views import TailoredDocView
  
  class MyEnhancedDocView(TailoredDocView):
      template_name = 'myapp/myenhancedpage.html'
      message_document = 'Messages/MyTailoredDoc.messages'
      
      def get_selected_section(self):
          """This method checks the keyword arguments to my view to find
          a section name."""
          section_name = self.kwargs.get('section_name')
          if section_name not in ('Part1', 'Part2'):
              raise Http404
          return section_name
      
      # overrides a view method
      def get_context_data(self, **kwargs):
          kwargs['section_name'] = self.get_selected_section()
          return super(MyEnhancedDocView, self).get_context_data(**kwargs)

In ``templates/myapp/myenhancedpage.html``::

  {% extends "base.html" %}
  
  {% load tailoring2tags %}
  
  {% block content %}
    {% render_section treq "Intro" %}
    {% render_section treq section_name %}
  {% endblock %}

In ``urls.py``::
  
  from myapps.views import MyEnhancedDocView

  urlpatterns = patterns('',
      (r'^enhanced1/$', MyEnhancedDocView.as_view(), {
        'section_name': 'Part1',
      }),
      (r'^enhanced2/$', MyEnhancedDocView.as_view(), {
        'section_name': 'Part2',
      }),
      (r'^enhanced3/$', MyEnhancedDocView.as_view()),
      (r'^enhanced4/(?P<section_name>.*)/$', MyEnhancedDocView.as_view()),
  )

Here, the following will happen at each URL:

* /enhanced1/:
  Intro and Part1 appear in the tailored output.
* /enhanced2/:
  Intro and Part2 appear in the tailored output.
* /enhanced3/:
  404 Not Found
* /enhanced4/Part1/:
  Intro and Part1 appear in the tailored output.
* /enhanced4/Part3/:
  404 Not Found

.. _multiple_documents_on_a_page:

Multiple Documents on a Page
----------------------------

Consider we have a second document in addition to the one from
:ref:`the first example <basic_tailored_page>`. This document is called
``Messages/Graphic.messages``, which contains a single section named 'Header'.

In ``myapp/views.py``::

  from djangotailoring.views import MultipleTailoredDocView
  
  class MyMultipleDocView(MultipleTailoredDocView):
      template_name = 'myapp/multidoc.html'
      message_documents = {
          'graphic': 'Messages/Graphic.messages',
          'doc': 'Messages/MyTailoredDoc.messages'
      }

In ``myapp/multidoc.html``::
  
  {% extends "base.html" %}
  
  {% load tailoring2tags %}
  
  {% block content %}
    {% render_section graphics "Header" %}
    {% render_section doc "Intro" %}
    {% render_section doc "Part1" %}
    {% render_section doc "Part2" %}
  {% endblock %}

.. _tailored_page_titles:

Tailored Page Titles
--------------------

Consider a message doc named ``Messages/MyPage.messages`` which has a section
named 'Title' as well as 'Main'. 'Title' is destined for the HTML page's
title, so let’s go there.

In ``myapp/urls.py``::

  from djangotailoring.views import TailoredDocView
  
  urlpatterns = patterns('',
      (r'^mypage/$',
        TailoredDocView.as_view(
          template_name='myapp/simple.html',
          message_document='Messages/MyPage.messages')),
  )

In ``templates/myapp/simple.html``::

  {% load tailoring2tags %}
  <html>
    <head><title>{% render_section treq "Title" nowrap %}</title></head>
    <body>
      {% render_section treq "Main" %}
    </body>
  </html>

.. _logging_page_views:

Logging Page Views
------------------

Let's log the hits to the view from
:ref:`the first example <basic_tailored_page>`.

In ``myapp/views.py``::

  from djangotailoring.views import TailoredDocView
  from djangotailoring.tracking.views import LogPageViewMixin
  
  class MyTailoredDocView(LogPageViewMixin, TailoredDocView):
      template_name = 'myapp/mypage.html'
      message_document = 'Messages/MyTailoredDoc.messages'
  
.. _protecting_page_access:

Protecting Page Access
----------------------

To protect a view like the one used in
:ref:`the first example <basic_tailored_page>`, mix in a
:class:`.LoginRequiredMixin`.

In ``myapp/views.py``::

  from djangotailoring.views import TailoredDocView, LoginRequiredMixin
  
  class MyTailoredDocView(LoginRequiredMixin, TailoredDocView):
      template_name = 'myapp/mypage.html'
      message_document = 'Messages/MyTailoredDoc.messages'

.. _logging_protected_page_access:

Logging Protected Page Access
-----------------------------

Let’s combine the previous :ref:`two <logging_page_views>`
:ref:`examples <protecting_page_access>`.

In ``myapp/views.py``::

  from djangotailoring.views import TailoredDocView, LoginRequiredMixin
  from djangotailoring.tracking.views import LogPageViewMixin
  
  class MyTailoredDocView(LogPageViewMixin, LoginRequiredMixin, TailoredDocView):
      template_name = 'myapp/mypage.html'
      message_document = 'Messages/MyTailoredDoc.messages'

.. note::
  The order of the above mixins matters. The page logging will happen before
  the protection mechanism takes place. This way, the attempt to access the
  and the subsequent redirect are logged. However, since the user is not
  logged in, there is no sure way of linking the redirected :class:`.Event`
  with the user.

Survey Views
============

.. _basic_survey_view:

A Basic Survey View
-------------------

Consider a situation where you have a Survey Document at
``Surveys/Eligibility.survey``, in your MTS project folder. You wish to save
the subject data on every page once the data is valid.

In ``myapp/views.py``::

  from django.shortcuts import redirect
  
  from djangotailoring.surveys.views import SimpleSurveyView
  from djangotailoring.views import UserProfileMixin, LoginRequiredMixin
  
  class EligibilitySurveyView(LoginRequiredMixin, UserProfileMixin, SimpleSurveyView):
      template_name = 'myapp/eligsurvey.html'
      survey_document = 'Surveys/Eligibility.survey'
      source = 'Elig'
      survey_id = 'eligibility'
      
      def on_valid_submission(self):
          self.save_subject(self.request_subject)
      
      def handle_end_of_survey(self):
          return redirect('home')
  
In ``templates/myapp/eligsurvey.html``::

  {% extends "base.html" %}
  {% load surveytags %}
  
  {% block content %}
    <form action="" method="post">
      {% render_survey_segment chunk %}
      <div>
        {% if previous_url %}
          <a href="{{ previous_url }}">Previous</a>
        {% endif %}
        <button type="submit" name="submit" value="Next">
      </div>
    </form>
  {% endblock %}


In ``urls.py``::

  from myapp.views import EligibilitySurveyView

  urlpatterns = patterns('',
    (r'^eligibility/(?P<page_id>.*)$', EligibilitySurveyView.as_view())
  )

.. _protecting_a_survey:

Protecting A Survey
-------------------

Sure, the survey in :ref:`the previous example <basic_survey_view>` is already
protected from non-logged-in users, but what if the user should not be able to
return to the survey if they have already taken it?

We will make an event that should be recorded at the end of the survey, and
the presence of that event for the user will mean that they are no longer able
to take the survey.

In ``myapp/views.py``::

  from django.shortcuts import redirect
  
  from djangotailoring.surveys.views import SimpleSurveyView
  from djangotailoring.views import UserProfileMixin, LoginRequiredMixin
  from djangotailoring.tracking import create_event
  
  COMPLETED_ELIGIBILITY_EVENTNAME = 'CompletedEligibilitySurvey'
  
  class EligibilitySurveyView(LoginRequiredMixin, UserProfileMixin, SimpleSurveyView):
      template_name = 'myapp/eligsurvey.html'
      survey_document = 'Surveys/Eligibility.survey'
      source = 'Elig'
      survey_id = 'eligibility'
      
      def can_access_survey(self):
          e = self.get_profile().latest_event(COMPLETED_ELIGIBILITY_EVENTNAME)
          return e is None
      
      def handle_bad_page_request(self):
          return redirect('home')
      
      def on_valid_submission(self):
          self.save_subject(self.request_subject)
      
      def handle_end_of_survey(self):
          create_event(COMPLETED_ELIGIBILITY_EVENTNAME, request=self.request)
          return redirect('home')
  
  
.. _single_page_survey:

A Single-Page Survey
--------------------

What if your survey called ``Single.survey`` that is so simple that it’s just
a single page of questions, and you would rather not deal with the ugly
numbers in the URL? Then use :class:`SinglePageSurveyView`.

In ``myapp/views.py``::

  from django.shortcuts import redirect
  
  from djangotailoring.surveys.views import SinglePageSurveyView
  from djangotailoring.views import UserProfileMixin, LoginRequiredMixin
  
  class MySingleSurveyView(LoginRequiredMixin, UserProfileMixin, SinglePageSurveyView):
      template_name = 'myapp/singlesurvey.html'
      survey_document = 'Surveys/Single.survey'
      source = ''
      survey_id = 'single'
      
      def on_valid_submission(self):
          self.save_subject(self.request_subject)
      
      def handle_end_of_survey(self):
          return redirect('home')
      
  
In ``urls.py``::
  
  from myapp.views import MySingleSurveyView
  
  urlpatterns = patterns('',
    (r'^single/$', MySingleSurveyView.as_view())
  )

.. _userless_survey:

A User-less Survey
------------------

Here's a tricky one: What if you don’t want visitors to create a user account
before they take a survey?

The approach:

* Use the session to store a random user id.
* Create a simple Mixin to handle the Subject access.
* Create a subject in the default :class:`.SubjectLoader` upon completion.

In ``myapp/views.py``::

  from uuid import uuid4
  
  from django.shortcuts import redirect
  
  from djangotailoring.project import getsubjectloader
  from djangotailoring.surveys.views import SimpleSurveyView
  
  SUBJECT_ID_SESSION_KEY = 'subject_id'
  
  class NoUserMixin(object):
      subjectloader = getsubjectloader()
      
      def get_user_id(self):
          session = self.request.session
          try:
              return session[SUBJECT_ID_SESSION_KEY]
          except KeyError:
              return session.setdefault(SUBJECT_ID_SESSION_KEY, uuid4())
      
      def get_subject(self):
          return self.subjectloader.empty_subject()[0]
      
      def save_subject(self, subject):
          self.subjectloader.store_subject(self.get_user_id(), subject)
      
  
  class NoLoginRequiredSurvey(NoUserMixin, SimpleSurveyView):
      template_name = 'myapp/nologinsurvey.html'
      survey_document = 'Surveys/NoLogin.survey'
      source = ''
      survey_id = 'nologin'
      
      def handle_end_of_survey(self):
          self.save_subject(self.get_request_subject()[0])
          return redirect('register')

After this, if part of the process is having a user create an account, you may
either copy data from the stored subject, or even consider modifying the
user_id attributes of the Subject and State storage mechanisms to the new
user id.

