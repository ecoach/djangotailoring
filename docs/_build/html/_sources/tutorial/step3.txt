*************************
Step 3: Building Up Views
*************************

As you know, *views* in Django are callable objects that return some
meaningful response to an HTTP request. Generally, views that return HTML
do so using
`Django’s template language <http://docs.djangoproject.com/en/1.3/topics/templates/>`_.

Templates
=========

For this tutorial, you will need to make one base template, from which all
other templates will inherit. For simplicity’s sake, put all templates into
``main/templates/``. Best practice
dictates that global templates should exist in a global, not application,
folder. In this case, setting up such a folder is a bit of overkill.

Base Template
-------------

While the following will be HTML5 compliant, it really doesn’t have much to
show for it.

* Save the following in ``base.html``::
  
    <!doctype html>
    <html>
      <head>
        <title>{% block title %}djangotailoring tutorial{% endblock %}</title>
      </head>
      <body>
        <div id="navigation">
          {% block navigation %}{% endblock %}
        </div>
        <div id="content">
          {% block content %}{% endblock %}
        </div>
        <hr>
        {% if user.is_authenticated %}
          <div>
            <a href="{% url logout %}">Log out</a>
          </div>
        {% endif %}
        <footer>You have just witnessed the magic of djangotailoring.</footer>
      </body>
    </html>
  
There is nothing special about the above template, so set yourself up for an
underwhelming presentation.

Login Template
--------------

Because the site depends on users being logged-in, naturally you should have a
login page.

* Save the following in ``login.html``::
  
    {% extends 'base.html' %}
    
    {% block title %}Log in{% endblock %}
    
    {% block content %}
      <h1>Welcome to my tailored website.</h1>
      <p>
        Use the form below to log in.
      </p>
      <form action="{% url login %}" method="post" accept-charset="utf-8">
        {% csrf_token %}
        {{ form.as_p }}
        <p>
          <input type="submit" value="Log in">
        </p>
      </form>
    {% endblock %}
  
Hopefully it is apparent that there is no magic appearing here.

Survey Template
---------------

Alright, now on to the new stuff. After a new user has logged into our site.

* Save the following in ``survey.html``::
  
    {% extends 'base.html' %}
    
    {% load surveytags %}
    
    {% block title %}Tell me about yourself{% endblock %}
    
    {% block content %}
      <form action="" method="post" accept-charset="utf-8">
        {% csrf_token %}
        {% render_survey_segment chunk %}

        <p>
          {% if previous_url %}
            <a href="{{ previous_url }}">Previous</a>
          {% endif %}
          <input type="submit" value="Next &rarr;">
        </p>
      </form>
    {% endblock %}
  
Yes, OK, the name `chunk` could be better. But, what you see here is the
following:

1. ``{% load surveytags %}`` loads the tag that is used to render the part
   of the survey the user is currently on. Not surprisingly, this is:
2. ``{% render_survey_segment chunk %}`` which will be replaced with a set of
   HTML form elements produced by the tailoring engine.
3. ``previous_url`` is part of the default survey template context which is
   simply a URL to the previous page in the survey.
4. Notice that the form’s ``action`` attribute is empty. The survey view
   always ``post``\ s information back to the rendering resource.
5. ``{% csrf_token %}`` is a Django built-in feature that should be on any
   page that submits a form. It protects against a class of Cross-site
   scripting attacks.

SleepIntro Template
-------------------

It may be lame, but for the tutorial, you will only create one page template.
Worry not, because doing one is very much like doing any other one.

* Save the following in ``sleepintro.html``::
  
    {% extends 'base.html' %}

    {% load tailoring2tags %}

    {% block title %}{% render_section treq "pageheader" nowrap %}{% endblock %}

    {% block content %}
      {% render_section treq "pagesubhead" %}
      {% render_section treq "section1header" %}
      {% render_section treq "section1text" %}
      {% render_section treq "section2header" %}
      {% render_section treq "section2text" %}
      {% render_section treq "section3header" %}
      {% render_section treq "section3text" %}
      {% render_section treq "footertext" %}
      {% comment %}
        While the following works for rendering, the messing with the image
        paths is beyond the scope of this tutorial. Consider it an exercise
        left to the reader.
        {% render_section treq "section1image1" %}
      {% endcomment %}
    {% endblock %}
  
If things seem a bit simple, they are!

1. For tailoring message docs, use ``{% load tailoring2tags %}``. This
   provides two tags to the context, only one of which is being used here:
2. ``{% render_section treq "sectionname" %}`` does more or less what it says,
   it produces the rendered HTML for the given section of the document and
   subject defined in the TailoringRequest ``treq``. We’ll get to that later.
3. Notice that the title block uses ``render_section`` with the third
   parameter “nowrap”. Because sections output by default as a single
   ``<div>`` element, but title doesn't allow any HTML structure, within,
   this option strips the wrapping element, resulting in just the content
   within.

Views
=====

Now that you have the basics for the output, it’s time to build the views to
serve them. All of the code below should be input into ``main/views.py``.

Message Document
----------------

For the single Message document the app will present, you can leverage the
most basic of the built-in tailoring view classes. In fact, you can skip
writing the view code all-together, by using the ``TailoredDocView`` class.

Survey
------

Survey documents contain a lot of mechanics to be processed. For the vast
majority of cases, ``djangotailoring``\’s built-in ``SimpleSurveyView`` class
will get most of the job done.

1. Import the view::
   
     from django.shortcuts import redirect
     from djangotailoring.surveys.views import SimpleSurveyView
     from djangotailoring.views import UserProfileSubjectMixin
  
  Something snuck in there. What’s this ``UserProfileSubjectMixin`` business?
  While the built-in tailoring view classes have this option by default, it
  currently is not included in the ``SimpleSurveyView``. This isn't a big deal,
  though, because you can build it yourself…

2. Define your SurveyView::
   
     class SleepSurveyView(UserProfileSubjectMixin, SimpleSurveyView):
         template_name = 'survey.html'
         survey_document = 'Surveys/SleepSurvey.survey'
         survey_id = 'sleep'
         source = ''
         
         def handle_end_of_survey(self):
             self.save_subject(self.request_subject)
             return redirect('intro')
  
  By defining this class, you have built a runnable survey, which handles the
  document slicing, skip patterns, back-stepping, and restarting. By
  overriding handle_end_of_survey, you have set the user to be forwarded to
  the page named 'intro' after storing their survey data to the user's
  database subject. The class name itself isn't important, just so long as
  it’s imported properly in the URLconf.

Speaking of which, it’s time to move on to :doc:`step4`.