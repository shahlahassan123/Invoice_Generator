
# from rest_framework import serializers
# from posts.models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'body']


from rest_framework import serializers
from invoices.models import Address, Item, Invoice


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    senderAddress = AddressSerializer()
    clientAddress = AddressSerializer()
    items = ItemSerializer(many=True)


    class Meta:
        model = Invoice
        fields = '__all__'


    def create(self, validated_data):
        sender_address_data = validated_data.pop('senderAddress')
        client_address_data = validated_data.pop('clientAddress')
        items_data = validated_data.pop('items')


        sender_address, created = Address.objects.get_or_create(**sender_address_data)
        client_address, created = Address.objects.get_or_create(**client_address_data)
        invoice = Invoice.objects.create(senderAddress=sender_address, clientAddress=client_address, **validated_data)


        for item_data in items_data:
            item, created = Item.objects.get_or_create(**item_data)
            invoice.items.add(item)


        return invoice


    def update(self, instance, validated_data):
        sender_address_data = validated_data.pop('senderAddress')
        client_address_data = validated_data.pop('clientAddress')
        items_data = validated_data.pop('items')


        instance.senderAddress.street = sender_address_data.get('street', instance.senderAddress.street)
        instance.senderAddress.city = sender_address_data.get('city', instance.senderAddress.city)
        instance.senderAddress.postCode = sender_address_data.get('postCode', instance.senderAddress.postCode)
        instance.senderAddress.country = sender_address_data.get('country', instance.senderAddress.country)
        instance.senderAddress.save()


        instance.clientAddress.street = client_address_data.get('street', instance.clientAddress.street)
        instance.clientAddress.city = client_address_data.get('city', instance.clientAddress.city)
        instance.clientAddress.postCode = client_address_data.get('postCode', instance.clientAddress.postCode)
        instance.clientAddress.country = client_address_data.get('country', instance.clientAddress.country)
        instance.clientAddress.save()


        instance.description = validated_data.get('description', instance.description)
        instance.paymentTerms = validated_data.get('paymentTerms', instance.paymentTerms)
        instance.clientName = validated_data.get('clientName', instance.clientName)
        instance.clientEmail = validated_data.get('clientEmail', instance.clientEmail)
        instance.status = validated_data.get('status', instance.status)
        instance.total = validated_data.get('total', instance.total)
        instance.save()


        instance.items.clear()
        for item_data in items_data:
            item, created = Item.objects.get_or_create(**item_data)
            instance.items.add(item)


        return instance
