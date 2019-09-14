from django.urls import path
from .views import ProspectListView, ProspectDetailView, ProspectAddView, HomePageView, ProspectDeleteView, ToDoListView, ProspectEditView


urlpatterns = [
    path('', ProspectListView.as_view(), name='prospect-list'),
    path('add/', ProspectAddView.as_view(), name='prospect-add'),
    path('<uuid:pk>/edit', ProspectEditView.as_view(), name='prospect-edit'),
    path('<uuid:pk>/', ProspectDetailView.as_view(), name='prospect-details'),
    path('<uuid:pk>/delete/', ProspectDeleteView.as_view(), name='prospect-delete'),
    path('to-do/', ToDoListView.as_view(), name='to-do-list'),
]