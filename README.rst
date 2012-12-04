Requirements
============

- A Django >= 1.3.
- South >= 0.7 (for development).

The development leverages South, the django model migrations
toolkit.  South is not technically required to use django-tailoring, but it
should be used if updating the application itself.

In addition, django-tailoring assumes that the following packages are
available on the Python path:

- tailoring2
- surveytracking

settings.py
===========

A django-tailoring app has the following settings.py options:

TAILORING2_PROJECT_ROOT (required):
    The absolute path to the root of the tailoring2 project directory.

TAILORING2_PROJECT_CONFIG:
    The path to the config file for the tailoring2 project. If it is not an
    absolute path, it should be relative to the project root.

TAILORING2_DICTIONARY:
    The path to the dictionary file for the tailoring2 project. If it is not
    an absolute path, it should be relative to the project root.

TAILORING2_CUSTOMIZATION_MODULE:
    The path to the application.py customization module for the tailoring2
    project. If it is not an absolute path, it should be relative to the
    project root.

TAILORING2_SUBJECT_LOADER_CLASS:
    The name of a djangotailoring.subjects.SubjectLoader class to use for
    loading and storing subjects. By default, it will use:
    'djangotailoring.subjects.SerializedSubjectLoader'.

TAILORING2_DEBUG:
    A Python boolean that globally sets whether djangotailoring render tags
    also produce a list of tailoring2 ProcessingError messages. This can be
    overridden by using the tailoring2debug tag defined below.

To work, TAILORING2_PROJECT_ROOT is required and either
TAILORING2_PROJECT_CONFIG or the combination of TAILORING2_DICTIONARY and
TAILORING2_CUSTOMIZATION_MODULE can be provided to initialize a project with
specific parameters.

Template Tags & Filters
=======================

There are three template tags and one template filter that are available to
django-tailoring projects. These can be activated by inserting:

{% load tailoring2tags %}

At the top of a django template.

render_section
--------------
render_section requires two arguements:

1. A django-tailoring TailoringRequest object.

2. A section name. This can be either a quoted string literal, or a template
variable.

It will output the result of tailoring2.render.tostring() for the section of
the document specified in the TailoringRequest object.

The optional third argument is a 'keyword': "nowrap". When nowrap is present
as the third and final argument of render_section, it has the same effect as
calling render_section_nowrap, as defined below.

render_section_nowrap
---------------------
render_section_nowrap is exactly the same as render_section, except the outer
html tags (usually <div> and </div>) are removed from the output. This is
useful for situations like the document <head>, or output that is directed to
html attributes in the template.

render_survey_segment
---------------------
render_survey_segment requires a single argument: A django-tailoring
SurveyController object. It will output the result of
tailoring2.render.tostring() on the page of the controller's survey state.
The output is not wrapped in a <form> tag, so all directing of the http
requests are handled by the application.

tailoring2debug
---------------
tailoring2debug is a command that produces no output on its own. When set to
"on", any tailoring2 ProcessingErrors that exist in the rendering tags above
will be appended to the end of the rendering in an HTML unordered list. This
tag will override the TAILORING2_DEBUG setting, if defined.

nowrapper
---------
nowrapper is a template filter that takes a string, and will remove any
balanced (X)HTML wrapping tag from the head and tail of the string.

An example use-case is for using tailored output where HTML tags are verboten.
For tailoring output, it is best used in conjunction with the filter template
tag. For example:

<head>
    <title>
        {% filter nowrapper %}
            {% render_section trequest "Title" %}
        {% endfilter %}
    </title>
</head>

Simple Tailoring
================

A short example:

--- app/views.py ---
from djangotailoring import getproject
from djangotailoring.views import TailoringDocView

class MyTailoringView(TailoringDocView):
    template_name='templatepage.html'
    message_document='Messages/MessageDoc.messages'
    
    def get_subject(self):
        return getproject().subject_for_primary_chars({})

myview = MyTailoringView.as_view()

--- app/templates/tailoredpage.html ---
{% load tailoring2tags %}
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>A tailored page</title>
</head>
<body>
  {% render_section treq "Body" %}
</body>
</html>

Simple Survey
=============

--- app/views.py ---
from djangotailoring.surveys.views import SimpleSurveyView

class MySurveyView(SimpleSurveyView):
    template_name='survey.html'
    survey_document='Surveys/SurveyDoc.survey'
    survey_id='survey'
    source=''
    
    def get_user_id(self):
        return self.kwargs.get('userid')


--- app/templates/survey.html ---
{% load surveytags %}
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>A survey</title>
</head>
<body>
  <form action="" method="post" accept-charset="utf-8">
    {% render_survey_segment chunk %}
    <p>
      <input type="submit" value="Continue &rarr;">
    </p>
  </form>
</body>
</html>

