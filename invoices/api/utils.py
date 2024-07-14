from invoices.models import Invoice
from .serializers import InvoiceSerializer
from rest_framework.response import Response
from rest_framework import status

def generate_invoice_id():
    last_invoice = Invoice.objects.order_by('-id').first()
    if not last_invoice:
        return 'INV001'
    
    last_id = last_invoice.id
    last_num = int(last_id.split('INV')[-1])
    new_num = last_num + 1
    new_id = f'INV{new_num:03}'
    
    return new_id

def getInvoicesList(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

def createInvoice(request):
    data = request.data
    new_id = generate_invoice_id()
    data['id'] = new_id
    serializer = InvoiceSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getInvoiceDetail(request, pk):
    try:
        invoice = Invoice.objects.get(id=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = InvoiceSerializer(invoice, many=False)
    return Response(serializer.data)

def updateInvoice(request, pk):
    try:
        invoice = Invoice.objects.get(id=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = InvoiceSerializer(invoice, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteInvoice(request, pk):
    try:
        invoice = Invoice.objects.get(id=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    invoice.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
