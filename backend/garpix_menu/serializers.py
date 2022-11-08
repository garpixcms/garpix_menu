from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import MenuItem


class MenuItemSerializer(ModelSerializer):

    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuItemWithChildrenSerializer(ModelSerializer):
    children = SerializerMethodField()

    def get_children(self, instance):
        items = instance.get_active_children()
        return MenuItemWithChildrenSerializer(items, many=True).data

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

    class Meta:
        model = MenuItem
        exclude = ('title_for_admin',)
        extra_fields = ['children']
