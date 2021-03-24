from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user", )

    def __init__(self, *args, **kwargs):
        ''' add placeholder and classes '''

        super().__init__(*args, **kwargs)

        placeholders = {
            "user_contact_number": "Contact Number",
            "user_street_address_1": "Address",
            "user_street_address_2": "Address",
            "user_town_or_city": "Town or City",
            "user_county": "County",
            "user_eircode": "Eircode",
        }

        self.fields["user_contact_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "user_country":
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'userprofile-input'
