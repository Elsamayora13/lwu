from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('course/', views.course_view, name='course'),
    path('ebook/', views.ebook_view, name='ebook'),
    path('riwayat-pembelian/', views.purchase_history_view, name='purchase_history'),
]