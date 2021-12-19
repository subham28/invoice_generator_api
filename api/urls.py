from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="apiOverview"),
    path("invoice-list/", views.getAll, name="getAll"),
    path("create-invoice/", views.createInvoice, name="createInvoice"),
]
