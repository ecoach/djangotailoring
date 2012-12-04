***************************
``djangotailoring.surveys``
***************************

.. module:: djangotailoring.surveys

.. toctree::

  views/index
  models
  templatetags
.. fields

Background
==========

The survey application wraps the tailoring2 Survey Engine in a Django support
structure, providing interfaces and features for MTS Survey documents.

The ``djangotailoring`` survey infrastructure involves a fairly complex View
class, a SurveyState Model type, and some template tags to make survey
management as straightforward as it can be.

States and Views
================

Surveys themselves are broken down into one to several pages. For this
application, it is assumed that each user’s page is backed by a
:class:`SurveyState <djangotailoring.surveys.models.SurveyState>` model
object. Access to a page is denied unless one is available.

:class:`SurveyState`\s are linked together in a chain where each state points
to the previous state in the user’s survey path. If a user backs up and
re-submits to a page, a new state is created, and the old one is invalidated.
This way, whole dead branches of a survey tree can be avoided when attempting
to restart a user.
