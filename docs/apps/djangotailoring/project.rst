***************************
``djangotailoring.project``
***************************

.. module:: djangotailoring.project

The core module of ``djangotailoring`` is ``project``. There are several
functions available that are used to load or locate resources defined for the
whole of the ``djangotailoring`` application.

Functions
=========

.. function:: getproject()

  :rtype: tailoring2.BaseProject instance
  :returns: the current application’s tailoring2 Project instance.
  
  This is based on the :doc:`global djangotailoring settings </settings>`.
  The project object is lazily loaded.

.. function:: getprojectroot()
  
  :rtype: a string
  :returns: the absolute path to the current project's root folder.

.. function:: getsubjectloader()

  :rtype: :class:`djangotailoring.subjects.SubjectLoader` object
  :returns: the current subject loader class as defined by
    :data:`settings.TAILORING2_SUBJECT_LOADER_CLASS`.

.. function:: project_document_path(path)

  :param path: a project-relative file path
  :type path: a string
  :rtype: a string
  :returns: the absolute path to the document ``path``.

.. function:: project_tailoring_doc(path)

  :param path: a project-relative file path
  :type path: a string
  :rtype: a tailoring2 Document instance
  :returns: the tailoring2 Document (an ElementTree) for the document at
    ``path``.
