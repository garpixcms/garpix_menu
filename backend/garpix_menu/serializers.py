from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import MenuItem


class MenuItemSerializer(ModelSerializer):
    link = SerializerMethodField()

    def get_link(self, instance):
        request = self.context.get('request', None)
        return instance.get_link(request)

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

    class Meta:
        model = MenuItem
        exclude = ('title_for_admin', 'sites', 'page')
        extra_fields = ['link']


class MenuItemWithChildrenSerializer(MenuItemSerializer):
    children = SerializerMethodField()

    def get_children(self, instance):
        items = instance.get_active_children()
        return MenuItemWithChildrenSerializer(items, many=True, context=self.context).data

    class Meta(MenuItemSerializer.Meta):
        extra_fields = MenuItemSerializer.Meta.extra_fields + ['children']
