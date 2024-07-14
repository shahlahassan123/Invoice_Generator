# # views.py
# # from rest_framework import generics
# from rest_framework.viewsets import ModelViewSet
# from posts.models import Post
# from .serializers import PostSerializer

# # class PostListCreate(generics.ListCreateAPIView):
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from posts.models import Post
# from .serializers import PostSerializer

# class PostListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import getInvoicesList, createInvoice, getInvoiceDetail, updateInvoice, deleteInvoice

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/invoices/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of invoices'
        },
        {
            'Endpoint': '/invoices/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single invoice object'
        },
        {
            'Endpoint': '/invoices/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new invoice with data sent in post request'
        },
        {
            'Endpoint': '/invoices/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing invoice with data sent in put request'
        },
        {
            'Endpoint': '/invoices/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing invoice'
        },
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getInvoices(request):
    if request.method == 'GET':
        return getInvoicesList(request)
    if request.method == 'POST':
        return createInvoice(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getInvoice(request, pk):
    if request.method == 'GET':
        return getInvoiceDetail(request, pk)
    if request.method == 'PUT':
        return updateInvoice(request, pk)
    if request.method == 'DELETE':
        return deleteInvoice(request, pk)

