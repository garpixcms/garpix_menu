from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import MenuItem


class MenuItemSerializer(ModelSerializer):
    link = SerializerMethodField()
    is_current = SerializerMethodField()
    is_current_full = SerializerMethodField()

    def get_link(self, instance):
        request = self.context.get('request', None)
        return instance.get_link(request)

    def get_is_current(self, instance):
        current_path = self.context.get('current_path', None)

        if current_path:
            return instance.get_is_current(current_path)
        return False

    def get_is_current_full(self, instance):
        current_path = self.context.get('current_path', None)

        if current_path:
            return instance.get_is_current_full(current_path)
        return False

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

    class Meta:
        model = MenuItem
        exclude = (
            'title_for_admin',
            'subpage_url',
            'sites',
            'page',
            'lft',
            'rght',
            'tree_id',
            'level',
            'created_at',
            'updated_at',
        )
        extra_fields = ['link', 'is_current', 'is_current_full']


class MenuItemWithChildrenSerializer(MenuItemSerializer):
    children = SerializerMethodField()

    def get_children(self, instance):
        items = instance.get_active_children()
        return MenuItemWithChildrenSerializer(items, many=True, context=self.context).data

    class Meta(MenuItemSerializer.Meta):
        extra_fields = MenuItemSerializer.Meta.extra_fields + ['children']
