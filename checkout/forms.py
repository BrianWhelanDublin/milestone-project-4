from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "contact_number",
            "street_address_1",
            "street_address_2",
            "town_or_city",
            "county",
            "eircode",
            "country",
        )

    def __init__(self, *args, **kwargs):
        ''' add placeholder and classes '''

        super().__init__(*args, **kwargs)

        placeholders = {
            "full_name": "Full Name",
            "email": "Email",
            "contact_number": "Contact Number",
            "street_address_1": "Address",
            "street_address_2": "Address",
            "town_or_city": "Town or City",
            "county": "County",
            "eircode": "Eircode",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'checkout-input'
