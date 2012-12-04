****************************
``djangotailoring.subjects``
****************************

.. module:: djangotailoring.subjects

Part of ``djangotailoring``’s core functionality is to load data from various
data sources and create :class:`tailoring2.Subject` instances. Additional
applications may wish to reverse the process and store said subject instances
for later retrieval. This module handles both of these scenarios.

The functionality is broken down into three parts:

* :ref:`Serialization <serialization-functions>`
* :ref:`Infrastructure <subject-loader-infrastructure>`
* :ref:`Built-in Subject Loaders <built-in-loaders>`

.. _serialization-functions:

Functions
=========

.. function:: encode_subject(subject)
  
  :param subject: the Subject to encode
  :type subject: a tailoring2 Subject instance
  :rtype: a JSON string
  :returns: a serialized string of the ``subject``’s primary chars. 
  
.. function:: decode_subject(subject_data, project)
  
  :param subject_data: the data to decode into a Subject
  :param project: the Project class used to calculate the derived values.
  :type subject_data: a JSON string of serialized Subject data
  :type project: a tailoring2.BaseProject instance
  :rtype: a tailoring2 Subject instance
  :returns: a fully constructed Subject object.
  
Exceptions
==========

.. exception:: SubjectDoesNotExist
  
  Indicates that a subject for the ID requested is not available by the given
  loader.
  
.. _subject-loader-infrastructure:

SubjectLoader interface
=======================

The subject loader interface is any object that has callables with the
following call signatures:

  * ``empty_subject()``
  * ``all_subject_ids()``
  * ``subject_exists(subjectid)``
  * ``get_subject(subjectid)``
  * ``store_subject(subjectid, subject)``
  * ``delete_subject(subjectid)``

Djangotailoring requires that at least ``empty_subject``, and ``get_subject``
are implemented. If your application modifies subjects, you must implement
``store_subject`` as well. All unimplemented features should raise
:exc:`NotImplementedError`.

.. class:: SubjectLoader
  
  .. classmethod:: empty_subject(cls)
  
    :rtype: a tailoring2 Subject instance
    :returns: a new Subject instance that was built with no input data.
  
  .. classmethod:: all_subject_ids(cls)
    
    :rtype: a list of strings
    :returns: a list of all ids that this subject loader can successfully
      produce when calling :meth:`get_subject`.
  
  .. classmethod:: subject_exists(cls, userid)
    
    :param userid: a string identifying a subject
    :type userid: a string
    :rtype: a boolean
    :returns: True if a subject is available for loading, otherwise False.
  
  .. classmethod:: get_subject(cls, userid)
    
    :param userid: a string identifying a subject
    :type userid: a string
    :rtype: a tailoring2 Subject instance
    :returns: a Subject built with data values for the given userid
    :raises: :exc:`SubjectDoesNotExist`
  
  .. classmethod:: store_subject(cls, userid, subject)
  
    :param userid: a string identifying a subject
    :param subject: the Subject to store
    :type userid: a string
    :type subject: a tailoring2 Subject instance
    
    The given Subject should be stored in a format that can later be loaded
    by the same SubjectLoader object. The only promise is that the
    primary characteristics of the Subject be stored.
    
    If a subject exists, it will be overwritten with the latest subject data.
    If the subject does not exist, a new subject will be created with the
    given subject’s data.
  
  .. classmethod:: delete_subject(cls, userid)
    
    :param userid: a string identifying a subject
    :type userid: a string
    :raises: :exc:`SubjectDoesNotExist`
    
    Removes a subject from the data store such that a subsequent call to
    :meth:`get_subject` raises :exc:`SubjectDoesNotExist`.
    
  
  
.. _built-in-loaders:

Built-in Subject Loaders
========================

.. class:: SerializedSubjectLoader
  
  A subclass of :class:`SubjectLoader` that implements the complete interface.
  Subjects are stored and accessed as objects of
  :class:`djangotailoring.models.SerializedSubjectData`.

  There is one attribute used by the class:

  .. attribute:: project
  
    A reference to the project instance that this loader will use when
    decoding subjects.  The default is the project returned by
    :func:`djangotailoring.project.getproject`


.. class:: DjangoSubjectLoader
  
  A subclass of :class:`SubjectLoader` that implements the complete interface.
  Subject data is stored in one or more instances of
  :class:`djangotailoring.models.SubjectData` as wide-tables. Clients should
  subclass this and modify :attr:`sources` as necessary for their project.
  As a convenience, a Django management command, :ref:`makemtsmodels-command`,
  will automatically build the skeleton of these model subclasses for the
  active tailoring2 dictionary.
  
  .. attribute:: sources
    
    A dictionary mapping source names to
    :class:`djangotailoring.models.SubjectData` subclasses. When
    :meth:`get_subject` is called, a query is made looking for user data in
    each source data model type. If an object is found, its fields and values
    will be used to generate the characteristics for the associated source.
    
    For multi-value characteristics, the loader expects there to be a set of
    NullBoolean fields, one for each possible value of the characteristic.
    They are named as ``<characteristic name>__<value name>``.
    
  .. attribute:: project
  
    A reference to the project instance that this loader will use when
    decoding subjects.  The default is the project returned by
    :func:`djangotailoring.project.getproject`
    
