from django import forms
from .models import Post
from .validators import validate_title



# class PostForm(forms.Form):
#     title = forms.CharField()
#     price = forms.IntegerField()
#     date = forms.CharField(widget=forms.DateInput(attrs={
#         "type": "date", "id": "date", "class": "form-control"}))

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields["date"].widget.attrs.update({"type": "date"})


class PostForm(forms.ModelForm):
    # title = forms.CharField(validators=[validate_title, ])

    class Meta:
        model = Post
        fields = "__all__"
    

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update({"rows": 2})
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


    def clean(self, attrs):
        title = attrs.get("title")

        if title == 'Hello':
            raise forms.ValidationError({"error": "{} is not valid title".format(title)})
        return attrs

    def save(self, validated_data):
        title = validated_data.get("title")
        return validated_data
