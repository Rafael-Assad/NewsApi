from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def listNews(request):

    return Response({'message': 'ta funfando'}, status=status.HTTP_200_OK)
