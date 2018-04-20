from django.http import HttpResponse
from django.shortcuts import render
# from rest_framework.viewsets import ReadOnlyModelViewSet
from Main.models import Object
from Main.serializers import ObjectSerializer
from rest_framework import generics


class ObjectView(generics.ListAPIView):
    serializer_class = ObjectSerializer
    object = Object

    def get_queryset(self):
        return Object.objects.filter(name=self.request.query_params.get('name'))
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


def main(request):
    return HttpResponse("Here's the text of the Web page.")