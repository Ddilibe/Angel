from django.urls import path
from .views import HomePageView, AboutPageView,AuditFormView,LatestView


urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('about/', AboutPageView.as_view(), name='about'),
        path('blacktears/audition/form/', AuditFormView, name='audition'),
        path('latest/', LatestView.as_view(), name='latest'),
]