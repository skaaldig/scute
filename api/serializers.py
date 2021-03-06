from rest_framework import serializers

from expenses import models


class PrincipalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Principal
        fields = "__all__"


class ActivityCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ActivityCategory
        fields = '__all___'


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Activity
        fields = "__all__"


class ObjectCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ObjectCode
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Expense
        fields = "__all__"

    activity = ActivitySerializer()

    def create(self, validated_data):
        activity_data = validated_data.pop("activity")
        activity = models.Activity.objects.create(**activity_data)
        expense = models.Expense.objects.create(**validated_data, activity=activity)
        return expense