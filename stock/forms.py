from django import forms
from .widgets import CustomClearableFileInput
from .models import Item, Category


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = "__all__"

    image = forms.ImageField(
        label="Image",
        required=False,
        widget=CustomClearableFileInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields["category"].choices = display_names
        for field_name, field in self.fields.items():
            if field_name != "image":
                field.widget.attrs["class"] = "product-form-item"
        self.fields["price"].widget.attrs["min"] = 0
        self.fields["price"].widget.attrs["step"] = 1
