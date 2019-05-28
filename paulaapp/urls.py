from django.urls import path
from .views import ProspectListView


urlpatterns = [
    path('', ProspectListView.as_view(), name='prospect-list'),
]