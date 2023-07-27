# Create your views here.
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from project.models import Event
from rest_framework.views import APIView
from project.serializers import EventSerializer


class EventListCreateView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            # Check if the event type is valid (one of 'PushEvent', 'ReleaseEvent', or 'WatchEvent')
            event_type = serializer.validated_data['type']
            if event_type not in ['PushEvent', 'ReleaseEvent', 'WatchEvent']:
                return Response({"error": "Invalid event type"}, status=status.HTTP_400_BAD_REQUEST)

            # Save the valid event and assign a unique integer id to it
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        events = Event.objects.filter()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EventRetrieveView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        events = Event.objects.filter(id=int(kwargs.get('event_id'))).last()
        if not events:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(events)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RepoEventsListView(APIView):
    def get(self, request, *args, **kwargs):
        events = Event.objects.filter(repo_id=int(kwargs.get('repo_id')))
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserEventsListView(APIView):
    def get(self, request, *args, **kwargs):
        events = Event.objects.filter(actor_id=kwargs.get('user_id'))
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
