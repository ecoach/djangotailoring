*************
Template Tags
*************

All template commands in this module are available in templates by including
the following:

  {% load tailoring2tags %}

in your templates.

Tags
====

.. _render_section:

render_section
--------------

Produces a tailored output for a given tailoring requeest, and section name::

  {% render_section treq sectionname %}

Two arguments are required:

  * **treq** a tailoring request object
  * **sectionname** a section name. This can be a variable, or a literal,
    quoted string.

If :data:`settings.TAILORING2_DEBUG` or :ref:`tailoring2_debug` is set, any
errors in the tailoring will be output into the template after any content
is rendered. This includes stack traces if something goes horribly wrong.

There is a third, optional argument that is a literal (unquoted) string:

  * ``nowrap``

It can be used as the last argument in the tag::

  {% render_section treq "Section" nowrap %}

When it is present, the wrapping ``<div>`` tag will be removed from the
rendered string before it is placed in the template.

.. _tailoring2_debug:

tailoring2_debug
----------------

Sets a context variable for the active template that, if ‘on’, will for any
errors to be rendered to the template. 

There are two options, either ``on`` or ``off``. For example::

  {% tailoring2_debug on %}

for enabling the debugging output, or::

  {% tailoring2_debug off %}

for disabling it.

This overrides any setting of :data:`settings.TAILORING2_DEBUG`

Filters
=======

.. _nowrapper:

nowrapper
---------

Takes a string object and if a matching beginning and ending HTML tag exist
at the head and tail of the string, the tag will be removed.
