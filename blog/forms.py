from django import forms
from .models import Post, Comment
from stock.widgets import CustomClearableFileInput


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


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            "title",
            "content",
            "image",
        }

    image = forms.ImageField(
        label="Image",
        required=True,
        widget=CustomClearableFileInput,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs["placeholder"] = "Post Title"
        self.fields["content"].widget.attrs["placeholder"] = "Post Content"
