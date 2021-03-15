from django import forms

from .models import Item, Category


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields["category"].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "product-form-item"
