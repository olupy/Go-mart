from rest_framework import serializers
from .models import Item, OrderItem,Category
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
    class Meta:
        model = Item
        ordering = ['-id']
    
    def create(self,validated_data):
        item_name = self.validated_data.get('item_name')
        price = self.validated_data.get('price')
        discount_price = self.validated_data.get('discount_price')
        category = self.validated_data.get('category')
        label = self.validated_data.get('label')
        description = self.validated_data.get('description')
        image = self.validated_data.get('image')

        item = Item.objects.create(
            item_name = item_name,
            price = price,
            discount_price = discount_price,
            category = category,
            label = label,
            description = description,
            image = image
        )

        item.save()
        return item
        


