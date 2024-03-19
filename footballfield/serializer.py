from rest_framework import serializers
from .models import Foodballfield, Bron

class FoodballfieldSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Foodballfield
        fields = "__all__"

class UpdatefoodballfildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodballfield
        fields = ['name','address', 'contact', 'image', 'booking_an_hour']
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.image = validated_data.get('image', instance.image)
        instance.booking_an_hour = validated_data.get('booking_an_hour', instance.booking_an_hour)
        instance.save()
        return instance



class BronSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Bron
        fields = "__all__"

class BronCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bron
        fields = ['foodballfield_id','user_id', 'start_time', 'end_time']

class UpdateBronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bron
        fields = ['foodballfield_id','user_id', 'start_time', 'end_time']

    def update(self, instance, validated_data):
        instance.foodballfield_id = validated_data.get('foodballfield_id', instance.foodballfield_id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.save()
        return instance

class FillterSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField(format='%Y-%m-%dT%H:%M')
    end_time=serializers.DateTimeField(format='%Y-%m-%dT%H:%M')
    x=serializers.IntegerField()
    y=serializers.IntegerField()