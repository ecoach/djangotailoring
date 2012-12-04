*****************************************
Step 2: Bootstrapping your Django project
*****************************************

In this step, you will create an MTS project, as well as a Django project and
enable djangotailoring linking the two together.

Making Your MTS Project
=======================

For this walkthrough, it will be easiest to simply use the built-in
MTS Sample Project.

* In MTS, go to the *File* menu and select ‘New’ ► ‘MTS - Project Sample’.
  
Feel free to name it whatever you'd like.

Now, you need to find the path to the MTS project. This is simple enough:

* Right-/Control-click on the project folder in the MTS Project Explorer and
  select the ‘Properties…’ option at the bottom of the menu.

On the right side of the information dialog that appears, there will be a
*Location* field. You can select the full path to the project listed there,
and use ⌘-C to copy it to the clipboard to save for our next step.

Making Your Django Project
==========================

Create a Django project using the standard bootstraping method Django
provides::

  django-admin.py startproject dttutorial

You may call your project anything you wish, for this tutorial, it’s assumed
that it is named as above: `dttutorial`.

* Dive into the project folder.

Create Your Main Django App
---------------------------

In this tutorial, there will be very little code that you have to write on
your own. Great, right? However, you will need to at least set up an
application to house at least one thing for the whole system to work.

* Begin by starting an app the usual way::

    python manage.py startapp main
  
  It could have been named anything you’d like, but for this tutorial, it will
  be called ‘main’.

* Edit ``main/models.py`` and drop in the following code::
  
    from django.db import models

    from djangotailoring.userprofile import (BaseUserProfile,
        register_profile_post_save_handler)

    class UserProfile(BaseUserProfile):
        pass

    register_profile_post_save_handler(UserProfile)
    
  Wait, what did you just do? You created a class, but didn’t define anything
  in it? You are creating a Model class that will be used as the profile in
  the Django Auth framework. Feel free to
  `read up on it <http://docs.djangoproject.com/en/1.3/topics/auth/#auth-profiles>`_.
  ``djangotailoring`` provides a base class and utility function to make
  tailoring on the logged-in user as simple as possible.  The utility function
  ``register_profile_post_save_handler``, ensures that whenever a user is
  created, your ``UserProfile`` object is automatically created and associated
  with that user without any other intervention.

Tweeking ``settings.py``
------------------------

Now is the time when you enable ``djangotailoring`` in your project, and hook
it up to your MTS project. Start by opening the ``settings.py`` file.

* Ammend the INSTALLED_APPS to include the
  applications::

    INSTALLED_APPS = (
      ...
      'djangotailoring',
      'djangotailoring.accounts',
      'djangotailoring.surveys',
      'djangotailoring.tracking',
      'main',
    )

* Re-define the AUTHENTICATION_BACKENDS::
  
    AUTHENTICATION_BACKENDS = ('djangotailoring.accounts.backends.AccessCodeBackend',)

  This allows us to log users in with just an access code.

* Choose the a database backend::
  
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dttutorial.db',
        ...      
      }

    }
  
  Like the project name, the database name can be anything you’d like, and
  placed anywhere on your disk, if it's a sqlite3 database. If you’re feeling
  adventurous, and want to use MySQL, for instance, go for it.

* Tell ``djangotailoring`` where your MTS project is::
  
    TAILORING2_PROJECT_ROOT = '<path to your MTS project (⌘-V to paste)>'
  
  This is the magic that informs ``djangotailoring`` where your MTS project is
  and where to locate its resources.

* Tell Django’s Auth framework where your Profile Model class is::
  
    AUTH_PROFILE_MODULE = 'main.UserProfile'
  
* Tell Django where to send non-logged-in users::
  
    LOGIN_URL = '/login/'
  
  Whenever a user requests a resource that is protected, they will be
  redirected to this url for authentication.

* Tell Django where to send users once they're logged-in::
  
    LOGIN_REDIRECT_URL = '/survey/'
  


Running ``syncdb``
------------------

* Run syncdb on your project::
  
    python manage.py syncdb
  
.. warning::
   Don’t create a superuser yet. Due to the way you created the UserProfile
   model above, creating a user while generating the database may not work.

.. attention::
   If you have `South <http://south.aeracode.org/>`_ installed (good for you,
   by the way), you need to take the extra step and run the ``migrate``
   command, as djangotailoring is developed with South migrations.

Now that you’ve set up your projects, you can go on to :doc:`step3`.
