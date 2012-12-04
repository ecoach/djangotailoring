***********************************
Step 4: Attaching the Views to URLs
***********************************

Now that you hvae the views in place, it’s time to hook them up to URLs. In
some cases, you didn't have to write any view code to get the functionality.

URLconfs
========

Since this is such a simple project, all of the URLs will be defined in the
root ``urls.py`` file.

Login
-----

The login system leverages the built-in
`django.contrib.auth <http://docs.djangoproject.com/en/1.3/topics/auth/>`_
framework, making life easy.

* Modify ``urls.py`` to contain the following::
  
    from djangotailoring.accounts.forms import AccessCodeForm
    
    urlpatterns = patterns('',
      (r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html',
        'authentication_form': AccessCodeForm
      }, 'login'),
    )
  
The first option is fairly obvious. The second option, ``authentication_form``
directs the view to use an ``AccessCodeForm`` instance instead of auth’s
built-in Username/Password-style form. ``AccessCodeForm`` has a single field
that users can use to authenticate.

Logout
------

For this site, logout leverages the same system as login, and is even simpler.
The django-provided ``logout_then_login`` view does essentially what it says:
if a logged-in user accesses this url, the user will be logged out, and
redirected to your login page.

* Below the login pattern in ``urls.py`` add the following::
  
    urlpatterns = patterns('',
      # ...,
      (r'^logout/$', 'django.contrib.auth.views.logout_then_login', {}, 'logout'),
    )
  

Home
----

To simplify things, any user requesting the root URL of the project should be
forwarded to the login page. To do that, you can leverage the built-in Django
``RedirectView``.

1. Import the ``RedirectView`` in ``urls.py``::
  
    from django.views.generic import RedirectView
  
2. Create the URL pattern for the view::
  
    urlpatterns = patterns('',
      (r'^$', RedirectView.as_view(url='/login/'), 'home'),
      # ...,
    )
  

The Survey
----------

To include the survey in your project, you’ll need to import the view class
that you created in ``views.py``, and then attach it to a URL. The trick about
the survey is that there is a required URL parameter,  ``page_id``, that needs
to be present for some magic to occur. You’ll see that below.

1. Import your SurveyView class in ``urls.py``::
  
    from main.views import SleepSurveyView
  
2. Create a URL pattern with the ``page_id`` parameter connected to your
   view::
   
     urlpatterns = patterns('',
       # ...,
       (r'^survey/(?P<page_id>.*)/$', SleepSurveyView.as_view(), {}, 'survey'),
     )
  

That Message Document
---------------------

To use the built-in ``TailoredDocView`` class without writing the view code
you can attach it directly within the URLconf itself.

1. Import ``TailoredDocView`` in ``urls.py``::
  
    from djangotailoring.views import TailoredDocView
  
2. Create a URL pattern attached to a customized view::
  
    urlpatterns = patterns('',
      # ...,
      (r'^intro/$',
        TailoredDocView.as_view(
          template_name='sleepintro.html',
          message_document='Messages/SleepIntro.messages'),
        {}, 'intro'),
    )
  
  Once again, the ``template_name`` option is straight-forward. The only other
  required option for a TailoredDocView is ``message_document``, which, come
  to think of it, is fairly obvious as well.

With that in place, logged-in users visiting ``/intro/`` should see tailored
content.

Oh, right. That whole logged-in users part…

Protecting the Views
--------------------

One last thing to do before you go is to force users to log in if they attempt
to load the tailored document and survey. You can use Django’s built-in
``login_required`` wrapper function to protect these precious views.

1. Import the ``login_required`` ‘decorator’::
  
    from django.contrib.auth.decorators import login_required
  
2. Wrap the view functions with said function::
  
    urlpatterns = patterns('',
      # ...,
      (r'^survey/(?P<page_id>.*)$', login_required(SleepSurveyView.as_view()),
        {}, 'survey'),
      (r'^intro/$',
        login_required(TailoredDocView.as_view(
        # ...
    )
  
In the End
----------

After all of that work, ``urls.py`` should look something like this::

  from django.conf.urls.defaults import patterns
  from django.views.generic import RedirectView
  from django.contrib.auth.decorators import login_required
  from djangotailoring.accounts.forms import AccessCodeForm
  from djangotailoring.views import TailoredDocView
  
  from main.views import SleepSurveyView
  
  urlpatterns = patterns('',
    (r'^$', RedirectView.as_view(url='/login/'), {}, 'home'),
    (r'^login/$', 'django.contrib.auth.views.login', {
      'template_name': 'login.html',
      'authentication_form': AccessCodeForm
    }, 'login'),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login', {}, 'logout'),
    (r'^survey/(?P<page_id>.*)/$',
      login_required(SleepSurveyView.as_view()),
      {}, 'survey'),
    (r'^intro/$',
      login_required(TailoredDocView.as_view(
        template_name='sleepintro.html',
        message_document='Messages/SleepIntro.messages'
      )), {}, 'intro'),
  )
  
  
Now that our site is complete, it’s time to move on to :doc:`step5`.