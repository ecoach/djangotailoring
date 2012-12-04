************************************
``djangotailoring.tailoringrequest``
************************************

.. module:: djangotailoring.tailoringrequest

When ``djangotailoring`` needs to communicate with the tailoring engine, it
uses :class:`TailoringRequest` objects. Each object encapsulates a combination
of document path and subject data which can send themselves through the
tailoring engine to produce tailored output.

Exceptions
==========

.. exception:: TailoringRequestError

  A base class for the following exceptions. Can be used to grab any
  downstream tailoring-request related error.

.. exception:: MissingSectionError

  Raised when a requested section does not exist in the current document.

.. exception:: MissingDocumentError

  Raised when a requested document does not exist on the file system.

Classes
=======

.. class:: TailoringRequest(self, project, docpath=None, subject=None, source='', render_transforms=None)
  
  :param project: the project used when building a tailoring engine pipeline
  :type project: a tailoring2 Project instance
  :param docpath: the path (absolute or project-relative) to the document
    to tailor with
  :type docpath: a string
  :param subject: the subject to tailor on
  :type subject: a tailoring2 Subject instance
  :param source: the data source to hoist by default
  :type source: a string
  :param render_transforms: the list of render transforms to perform on the
    tailored output
  :type render_transforms: a list of tailoring2.render transform functions

  .. attribute:: messagedoc
  
    The tailoring2 document (an ElementTree) for this tailoring request.
    Accesses with an undefined docpath will result in ``None``. Accesses for
    an invalid docpath will raise :exc:`MissingDocumentError`
  
  .. attribute:: sections
  
    A dictionary of the section names in :attr:`messagedoc` mapped to their
    associated section ElementTree Elements.
  
  .. method:: render_section(self, section)
  
    :param section: a section name
    :type section: a string
    :rtype: an HTML ElementTree
    :returns: the post-render document output of the tailoring engine
    :raises: :exc:`MissingSectionError` if no section exists in the document.
  

