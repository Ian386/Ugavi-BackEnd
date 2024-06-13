from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('locations/', views.LocationList.as_view(), name='locations'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='location-detail'),
    path('locations/<str:label>/', views.LabelTypeView.as_view(), name='location-type')
]

urlpatterns = format_suffix_patterns(urlpatterns)