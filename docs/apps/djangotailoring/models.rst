**************************
``djangotailoring.models``
**************************

.. module:: djangotailoring.models

Djangotailoring provides a set of model classes that can be used for subject
data storage, one of which is abstract.

Models
======

.. class:: SubjectData
  
  An abstract model class that is useful for storing subject data as columns
  in a wide table. Subclasses can be used in concert with
  :class:`djangotailoring.subjects.DjangoSubjectLoader` to make fetching and
  updating subjects in such a fashion straightforward.
  
  .. attribute:: user_id
  
    A 40-character text field that is unique per table this is what's used
    to identify the subject; it can be anything. It is conventionally the same
    as the user id of the auth.User objects, if used.
  
  .. attribute:: modified
    
    A timestamp indicating the last time that the table was modified by any
    Django-level `.save()` command
    
  .. method:: as_json(self)
  
    :rtype: a string
    :returns: the JSON representation of :meth:`as_dict()`.
  
  .. method:: as_dict(self)
    
    :rtype: a dictionary
    :returns: a dictionary of instance attribute names to their values.
  

.. class:: SerializedSubjectData

  A concrete model class that is used for subject storage. All data is stored
  as a text blob, and it is up to clients to encode and decode the
  primary_data for each instance. It is used by
  :class:`djangotailoring.subjects.SerializedSubjectLoader` as its storage
  mechanism.
  
  .. attribute:: user_id
  
    A 40-character text field that is unique per table this is what's used
    to identify the subject; it can be anything. It is conventionally the same
    as the user id of the auth.User objects, if used.
  
  .. attribute:: primary_data
  
    A sizeless text blob used to store subject data.
  
  .. attribute:: updated
    
    A timestamp indicating the last time that the primary_data was changed by
    any Django-level `.save()` command
  
