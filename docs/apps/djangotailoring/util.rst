************************
``djangotailoring.util``
************************

A smattering of helpful functions that havn’t any other natural home.

Formatting
==========

.. function:: lazyformat(s, f)
  
  :param s: the format string
  :type s: unicode
  :param f: the formatting dictionary
  :type f: a dictionary
  :rtype: a lazy-unicode object

  This is a lazy version of the ``%`` operator. This allows string formatting
  using dictionaries to be postponed until necessary. It is important when
  using lazy-unicode objects as either the format string itself, or values in
  the formatting dictionary.

.. function:: nowrapper(value[, tagnames=None])

  :param value: the string to be modified
  :type value: str or unicode
  :param tagnames: a list of tag names that are qualified for removal
  :type tagnames: a list of str or unicode objects
  :rtype: str or unicode
  
  Given a Unicode or String object `value`, locate a surrounding
  html/xml-style tag surrounding `value`, and remove it.
  Tags found with names not in the tagnames list are left intact. If the list
  is empty, or not provided, tags with any name are removed.


Path Manipulation
=================

.. function:: namebase(pth)

    :param pth: a path
    :type pth: str or unicode
    :returns: pth without its extension and without its enclosing path
    
