from django.urls import path

urlpatterns = [
  path('events/'. EventListCreateView.as_view(), name='event-list-create'),
  path('events/<int:pk>/'. EventRetrieveView.as_view(), name='event-retrieve'),
  path('events/<int:repo_id>/events/'. RepoEventsListView.as_view(), name='repo-event-list'),
  path('events/<int:user_id>/events/'. UserEventsListView.as_view(), name='user-event-list'),
]