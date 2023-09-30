from django.urls import path
from .views import WorkListCreateView, ArtistRegistrationView

urlpatterns = [
    path('api/works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('api/register/', ArtistRegistrationView.as_view(), name='artist-register'),
]
