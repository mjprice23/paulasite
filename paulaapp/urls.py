from django.urls import path
from .views import ProspectListView, ProspectDetailView, ProspectAddView, HomePageView, ProspectDeleteView


urlpatterns = [
    path('', ProspectListView.as_view(), name='prospect-list'),
    path('add/', ProspectAddView.as_view(), name='prospect-add'),
    path('<uuid:pk>/', ProspectDetailView.as_view(), name='prospect-detail'),
    #path('<uuid>/delete/'), ProspectDeleteView.as_view(), name='prospect-delete'),
]

homepatterns = [
    path('home/', HomePageView.as_view(), name='home'),
]