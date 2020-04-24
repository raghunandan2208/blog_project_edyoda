from django import forms
from django.forms import ModelForm
from blog.models import Post
from tinymce.widgets import TinyMCE
from accounts.models import User


class PostForm(ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    author = forms.CharField(disabled=True)

    class Meta:
        model = Post
        fields = ['title', 'status', 'content', 'category', 'image']


class ContactForm(forms.Form):
    countries = [("IN","INDIA"),("CH","CHINA"),("US","UNITED STATES")]
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    phone = forms.RegexField(regex="^[6-9][0-9]{9}$", error_messages={"invalid":"Please provide valid Indian phone number"},required=False)
    message = forms.CharField(widget=forms.Textarea)
    city = forms.CharField()
    country = forms.ChoiceField(choices=countries)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")

        if email == "" and phone == "":
            self.add_error("email","Atleast Email or Phone number should be provided")

    def clean_email(self):
        data = self.cleaned_data.get("email")
        if "gmail" not in data:
            raise forms.ValidationError("Email domain must be gmail", code="invalid")
        else:
            return data
