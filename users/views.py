from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from rest_framework.views import APIView

@api_view(['GET', 'POST'])
def profile_list(request):

    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
