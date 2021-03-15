from django import forms
from .models import NewsletterSubscriber, Message


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["email"].widget.attrs['class'] = "newsletter-form-input"


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "subject": "Subject",
            "user_email": "Email",
            "message": "Message"
            }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "contact-form-field"
