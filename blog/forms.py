from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "comment",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["comment"].widget.attrs[
            "placeholder"] = "Add a Comment here"
        self.fields["comment"].widget.attrs['class'] = "comment-form-input"
