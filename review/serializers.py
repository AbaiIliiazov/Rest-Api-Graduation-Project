from rest_framework import serializers
from review.models import Review
from my_user.models import User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',)


class ReviewSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

    def get_items(self, obj):
        return obj.product.id

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user_name = self.context["request"].user
        product_id = self.context["request"].data["product"]
        method = self.context["request"].stream.method
        reviews = Review.objects.filter(product=product_id).filter(creator=user_name).count()
        if reviews and method == 'POST':
            raise ValidationError({"Error": "You cannot leave more than one review per one product"})
        return data