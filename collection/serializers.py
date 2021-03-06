from rest_framework import serializers
from collection.models import Collection, ProductInCollection
from product.models import Product

class ProductInCollectionSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),
    source="product.id")
    name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = ProductInCollection
        fields = ('product_id','name')

class CollectionSerializer(serializers.ModelSerializer):
    collections = ProductInCollectionSerializer(many=True,
    read_only=False)

    class Meta:
        model = Collection
        fields = ('id', 'title', 'text', 'collections', 'created_at','updated_at',)

    def update(self, instance, validated_data):
        collections = validated_data.pop('collections',[])
        instance = super().update(instance,validated_data)
        for collection in collections:
            ProductInCollection.objects.update_or_create(
                product = collection["product"]["id"],collection=instance,
            )
        instance.save()
        return instance