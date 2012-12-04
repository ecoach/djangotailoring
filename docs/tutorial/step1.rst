********************
Step 1: Installation
********************

Install
=======

.. hint::
   Consider using `virtualenv <http://www.virtualenv.org/>`_ for this process.
   It keeps your installed packages isolated from the system python install,
   and is generally a best-practice when it comes to developing multiple
   projects on the same machine.

Django
------

Download and install `Django <http://www.djangoproject.org/>`_ version 1.3 or
greater. The easiest way to do this is using pip::

  pip install Django

If you have an earlier version of Django installed, use::

  pip install -U Django

``tailoring2``
--------------

While you aren't able to pip-install tailoring2, it does come with a
setuptools ``setup.py`` script, making the install process fairly painless
otherwise.

The current best option is to check out the trunk of ``tailoring2``, as the
i18n features were added since the latest release was made. Assuming you have
subversion installed, check out the tailoring2 bundle::

  svn co https://yertle.chcr.med.umich.edu/svn/NextGenTailoring/engine/trunk/tailoring2

In the tailoring2 folder, you can execute the following command to install::

  python setup.py install

``surveytracking``
------------------

As the least mature dependency, ``surveytracking`` will have to be manually
installed. By “installed” it means “checking out a revision directly into the
site-packages folder”. This is, of course, a very sloppy way of doing things,
but as of now, this is what we have.

In your python installation (hopefully a virtualenv, as hinted at above), go
to the folder ``lib/python2.x/site-packages``. In there, execute::

  svn co https://yertle.chcr.med.umich.edu/svn/NextGenTailoring/engine/trunk/surveytracking

Gross, right? At least it’s installed.

``djangotailoring``
-------------------

On to the app itself. As with tailoring2, you should be able to check out the
app bundle and run ``setup.py``::

  svn co https://yertle.chcr.med.umich.edu/svn/djangotailoring/branches/django1.3-dev/django-tailoring

Once again, from the django-tailoring folder, run::

  python setup.py install

Now that that's complete, you should have all the packages necessary for using
djangotailoring in your project. From here, let's move on to :doc:`step2`.
