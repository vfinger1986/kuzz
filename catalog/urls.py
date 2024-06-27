from django.urls import path
from catalog import views



app_name = 'catalog'

urlpatterns = [
    path('',views.catalog, name='catalog' ),
    
    path('service-request/', views.ServiceRequestView.as_view(), name='service-request'),
    path('thank-you/', views.ThanksForRequestView.as_view(), name='thank_you'),

]
