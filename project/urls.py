from django.urls import path
from project.views import EventListCreateView, EventRetrieveView, RepoEventsListView, UserEventsListView

urlpatterns = [
  path('events/', EventListCreateView.as_view(), name='event-list-create'),
  path('events/<int:event_id>/', EventRetrieveView.as_view(), name='event-retrieve'),
  path('repos/<int:repo_id>/events/', RepoEventsListView.as_view(), name='repo-event-list'),
  path('users/<int:user_id>/events/', UserEventsListView.as_view(), name='user-event-list'),
]