from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UserProfile
from .serializer import UserProfileSerializer


@api_view(["GET"])
def List_Profile(request):
    obj = UserProfile.objects.all()
    serializer = UserProfileSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['POST', 'PATCH'])
@permission_classes([IsAuthenticated])
def create_and_update_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    serializer = UserProfileSerializer(
        profile, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED if profile else status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
