from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = (
            "review",
            "stars"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["stars"].widget.attrs["min"] = 1
        self.fields["stars"].widget.attrs["max"] = 5
        self.fields["stars"].widget.attrs["value"] = 1
