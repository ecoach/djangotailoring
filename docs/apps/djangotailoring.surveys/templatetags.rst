*************
Template Tags
*************

.. module:: djangotailoring.surveys.templatetags

All template commands in this module are available in templates by including
the following:

  {% load surveytags %}

in your templates.

Tags
====

.. _render_survey_segment:

render_survey_segment
---------------------

Produces a survey output for for a given :class:`.SurveyRenderChunk`::

  {% render_survey_segment chunk %}

If :data:`settings.TAILORING2_DEBUG` or :ref:`tailoring2_debug` is set, any
errors in the tailoring will be output into the template after any content
is rendered. This includes stack traces if something goes horribly wrong.

