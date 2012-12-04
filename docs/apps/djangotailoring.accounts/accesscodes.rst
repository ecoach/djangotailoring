****************************************
``djangotailoring.accounts.accesscodes``
****************************************

.. module:: djangotailoring.accounts.accesscodes

Access Codes are often structured in such a way that they are easily
generated, and validated. The base class :class:`Code` contains most of the
functionality.

Also part of the standard set of Code generators is the pair of Basic code
classes. A Basic code consists of two letters followed by four digits. Regular
versions of the Basic codes have their letters drawn from A-T, while the test
versions have their letters drawn from the range W-Z. This way, codes can be
distinguished at a glance.

Classes
=======

.. class:: Code(accesscode)
  
  :param accesscode: an access code
  :type accesscode: a string
  
  Represents a single access code object. Can be queried for validity and
  existence in the authentication system. Class methods exist for new code
  generation. Codes that are generated are random strings of 15 letters and
  numbers.
    
  .. method:: is_valid(self)
  
    :rtype: a boolean
  
    Identifies whether the current Code is valid per the rules defined by the
    class.
    
  .. method:: get_user(self)
  
    :rtype: a :mod:`django.contrib.auth` User
    :returns: User model associated with this code. If no such user exists,
      raises :exc:`User.DoesNotExist`.
    
  .. method:: create_user(self)
  
    :rtype: a :mod:`django.contrib.auth` User
    :returns: a new User for this new access code, set without a password or
      last_login time. ``None`` if the code already exists.
  
  .. method:: get_or_create_user(self)
    
    :rtype: a tuple of (:mod:`django.contrib.auth` User, boolean)
    :returns: a User for this code, along with a boolean indicating whether
      the user was created or not.
    
  .. classmethod:: generate_new_code(cls)
  
    :rtype: an instance of ``cls``
  
    Subclasses should implement this class method to customize how access
    codes strings are built. This method should not attempt to check whether a
    code it generated was already used.
    
  .. classmethod:: code_generator(cls)
  
    An iterator that will contiunously yield new codes per
    :meth:`generate_new_code`
  
  .. classmethod:: codes_in_database(cls, codes)
  
    :param codes: a set of access codes
    :type codes: a collection of strings
    :rtype: a list of strings
    :returns: all access codes in ``codes`` that are currently in use in the
      Users table.
  
  .. classmethod:: new_code(cls)
  
    :rtype: an instance of ``cls``
    :returns: an instance that does not have an associated User in the
      database.
  
  .. classmethod:: new_codes(cls, size)
  
    :param size: the number of codes you wish to generate.
    :type size: a positive integer
    :rtype: an iterable of ``cls`` instances
    :returns: a collection of instances of size ``size``. Instances returned
      are guaranteed not to have Users in the database at the time of
      generation.

Basic Codes
-----------

.. class:: BasicAccessCode

  A code class that generates codes in the format "LLDDDD", where L is
  an uppercase ASCII letter from the set containing A-T, and D is a
  base-10 digit.  

.. class:: BasicTestCode

  A BasicAccessCode whose letters will only be in the set of letters
  containing W-Z rather than A-T. This distinguishes them from regular
  BasicAccesCodes easily.
