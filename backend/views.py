from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import BasePermission
from django.contrib.auth import authenticate, login, logout
from .models import BlackListedToken
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .scraping import GmailScraping


# Create your views here.
class IsTokenValid(BasePermission):
    """Api will be used in the permission class of APIs
      permission_class = (IsAuthenticated, IsTokenValid)
    """

    def has_permission(self, request):
        user_id = request.user.id
        is_allowed_user = True
        token = request.auth.decode("utf-8")
        try:
            is_blackListed = BlackListedToken.objects.get(user=user_id, token=token)
            if is_blackListed:
                is_allowed_user = False
        except BlackListedToken.DoesNotExist:
            is_allowed_user = True
        return is_allowed_user


class Login(TokenObtainPairView):
    """login rest api"""
    serializer_class = TokenObtainPairSerializer


def logout_request(request):
    logout(request)
    return JsonResponse({"response": "logout successfully!!"}, status=200)


# Gmail Scraping API view
class GmailScrapingAPIView(APIView):
    """
    List all messages scrap data
    Request Params::
        email_limit : 20
        query_text: invoice OR subscription OR bill OR amount
    """
    permission_classes =(AllowAny,)

    def get(self, request, format=None):
        email_limit = int(request.GET.get('email_limit', 20))
        query_text = request.GET.get('query_text', 'invoice OR subscription OR bill OR amount')
        gmail_scraping = GmailScraping()
        result = gmail_scraping.get_email_content(email_limit=email_limit, query_text=query_text)
        return Response(result)