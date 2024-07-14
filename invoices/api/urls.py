# posts/api/urls.py
# from django.urls import path
# from .views import PostListAPIView

# urlpatterns = [
#     path('posts/', PostListAPIView.as_view(), name='post-list'),
# ]


from django.urls import path
from .views import getRoutes, getInvoices, getInvoice

urlpatterns = [
    path('', getRoutes, name='routes'),
    path('invoices/', getInvoices, name='invoices'),
    path('invoices/<str:pk>/', getInvoice, name='invoice-detail'),
]
