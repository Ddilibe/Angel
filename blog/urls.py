from django.urls import path
from .views import HomePageView, AboutPageView,AuditFormView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('about/', AboutPageView.as_view(), name='about'),
        path('blacktears/audition/form/', AuditFormView, name='audition'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)