# models.py
# from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()

#     def __str__(self):
#         return self.title


from django.db import models
from django.utils import timezone

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postCode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postCode}, {self.country}"

class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('draft', 'Draft')
    ]

    id = models.CharField(max_length=20, primary_key=True)
    # createdAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(auto_now_add=True)
    paymentDue = models.DateField()
    description = models.CharField(max_length=255)
    paymentTerms = models.IntegerField()
    clientName = models.CharField(max_length=255)
    clientEmail = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    senderAddress = models.ForeignKey(Address, related_name='sender_invoices', on_delete=models.CASCADE)
    clientAddress = models.ForeignKey(Address, related_name='client_invoices', on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id
