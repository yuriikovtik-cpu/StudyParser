from django.http import Http404
from rest_framework.response import Response
from rest_framework import views
from .requestsApp import getTools
from .serializers import ToolSerializer
from .models import Tool


class ToolAPIView(views.APIView):
    def get(self,request):
        message = {
            'message': 'hello',
        }
        return Response(message)
    def post(self,request):
        product = getTools()
        return Response(product)

class ToolListAPIView(views.APIView):
    def get(self,request):
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)

class ToolRetrieveAPIView(views.APIView):
    def get(self, request, id):

        if Tool.object.id():
            tools = Tool.objects.get(id=id)
            serializer = ToolSerializer(tools)
            return Response(serializer.data)
        else :
            raise Http404

