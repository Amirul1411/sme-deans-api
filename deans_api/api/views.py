from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, mixins, generics
from django.contrib.auth.models import User
from .models import Crisis, CrisisAssistance, CrisisType
from .serializer import CrisisSerializer, UserSerializer, CrisisAssistanceSerializer, CrisisTypeSerializer
# from .serializer import CrisisListSerializer, CrisisDeleteSerializer, UserSerializer#, CrisisUpdateSerializer
from .permissions import IsAuthorOrReadOnly

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
)


class CrisisViewSet(viewsets.ModelViewSet):
	queryset = Crisis.objects.all()
	serializer_class = CrisisSerializer

	def get_permissions(self):
		"""
		Instantiates and returns the list of permissions that this view requires.
		"""
		if self.action == 'list':
			permission_classes = [AllowAny]
		elif self.action == 'retrieve':
			permission_classes = [AllowAny]
		elif self.action == 'create':	
			permission_classes = [AllowAny]
		else:
			permission_classes = [IsAdminUser]
		return [permission() for permission in permission_classes]

class CrisisAssistanceViewSet(viewsets.ModelViewSet):
	queryset = CrisisAssistance.objects.all()
	serializer_class = CrisisAssistanceSerializer

	def get_permissions(self):
		"""
		Instantiates and returns the list of permissions that this view requires.
		"""
		if self.action == 'list':
			permission_classes = [AllowAny]
		elif self.action == 'retrieve':
			permission_classes = [AllowAny]
		elif self.action == 'create':	
			permission_classes = [AllowAny]
		else:
			permission_classes = [IsAdminUser]
		return [permission() for permission in permission_classes]

class CrisisTypeViewSet(viewsets.ModelViewSet):
	queryset = CrisisType.objects.all()
	serializer_class = CrisisTypeSerializer

	def get_permissions(self):
		"""
		Instantiates and returns the list of permissions that this view requires.
		"""
		if self.action == 'list':
			permission_classes = [AllowAny]
		elif self.action == 'retrieve':
			permission_classes = [AllowAny]
		elif self.action == 'create':	
			permission_classes = [AllowAny]
		else:
			permission_classes = [IsAdminUser]
		return [permission() for permission in permission_classes]


class UserCreateView(generics.CreateAPIView):
	model = User
	permission_classes = [AllowAny]
	serializer_class = UserSerializer