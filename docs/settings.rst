********
Settings
********

.. module:: settings

Djangotailoring looks for a handful of settings in the Django ``settings``
module to perform the tailoring throughout the application.

.. data:: TAILORING2_PROJECT_ROOT

  **required** The absolute path to the root folder of your MTS project.
  
.. data:: TAILORING2_PROJECT_CONFIG
  
  The path to a tailoring2 config file used to instantiate the project.  If a
  relative path is given, it is assumed to be relative to
  :data:`TAILORING2_PROJECT_ROOT`.

.. data:: TAILORING2_DICTIONARY

  The path to the dictionary file for your MTS project. If a relative path is
  given, it is assumed to be relative to :data:`TAILORING2_PROJECT_ROOT`.

.. data:: TAILORING2_CUSTOMIZATION_MODULE
  
  The path to the application.py customization module for your MTS project. If
  a relative path is given, it is assumed to be relative to
  :data:`TAILORING2_PROJECT_ROOT`.

.. data:: TAILORING2_SUBJECT_LOADER_CLASS

  The name of a :class:`djangotailoring.subjects.SubjectLoader` class to use
  for loading and storing subjects. By default, it will be set to
  `'djangotailoring.subjects.SerializedSubjectLoader'`

.. data:: TAILORING2_DEBUG

  A Python boolean that globally sets whether djangotailoring render tags
  also produce a list of tailoring2 ProcessingError messages. This can be
  overridden by using the :ref:`tailoring2_debug` tag.

To work, :data:`TAILORING2_PROJECT_ROOT` is required and either
:data:`TAILORING2_PROJECT_CONFIG` or the combination of
:data:`TAILORING2_DICTIONARY` and :data:`TAILORING2_CUSTOMIZATION_MODULE` can
be provided to initialize a project with specific parameters.

