********************
Step 5: Adding Users
********************

One thing that needs to happen before users can log into the site is to make
user accounts. For the sake of brevity, you will make users in the shell. The
process can be automated, but for this tutorial, you will be doing it the hard
way.

AccessCodes
===========

As you saw in :doc:`step3`, the site will use a djangotailoring feature of
access codes. In particular, the easiest way of doing this is using the
``BasicAccessCode`` class. ``BasicAccessCode`` provides an interface for
generating users with usernames with the format *CC####*, where 'C' is a
letter, and '#' is a base-10 digit.

* Start up a python shell by running::
  
    $ python manage.py shell
  
This launches a python interactive shell with the django ``settings`` module
values preloaded and configured.

* Import the ``BasicAccessCode`` class::
  
    >>> from djangotailoring.accounts.accesscodes import BasicAccessCode
  
* Play around a bit::
  
    >>> code = BasicAccessCode.new_code()
    >>> code
    <BasicAccessCode: FC9384>
    >>> codes = BasicAccessCode.new_codes(3)
    >>> codes
    set([<BasicAccessCode: FC9384>, <BasicAccessCode: EG2934>, <BasicAccessCode: JB0532>])

  
As you can see, there are two class methods that will create instances of
``BasicAccessCode``. Note that code instances do not automatically create
users in the database. So, how do you do that?

  >>> for code in codes:
  ...     code.create_user()
  ...
  <User: FC9384>
  <User: EG2934>
  <User: JB0532>
  
At this point, there are three users in the system, ready to go. So, go to
:doc:`step6`.
