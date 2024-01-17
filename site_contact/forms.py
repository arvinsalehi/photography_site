from django import forms
from django.core import validators


class ContactUsFrom(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Name', 'id': "fname", 'class': 'form-control'}),
        label=False,
        validators=[validators.MaxLengthValidator(150, "نام باید کمتر ۱۵۰ کاراکتر باشد")]
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "LastName", 'id': 'lname', 'class': 'form-control'}
        ),
        label=False,
        validators=[validators.MaxLengthValidator(150, "نام خانوادگی باید کمتر ۱۵۰ کاراکتر باشد")]
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'id': 'email', 'class': 'form-control'}
    ),
        label=False,
        validators=[validators.MaxLengthValidator(150, "ایمیل باید کمتر ۱۵۰ کاراکتر باشد")]
    )

    subject = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Subject', 'id': 'subject', 'class': 'form-control'}
    ),
        label=False,
        validators=[validators.MaxLengthValidator(150, "عنوان باید کمتر ۱۵۰ کاراکتر باشد")]
    )

    text = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Enter your thought', 'id': 'message', 'name': 'message', 'cols': '30', 'rows': '7',
               'class': 'form-control'}
    ),
        label=False
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_ext = ["gmail.com", "yahoo.com"]
        if email.split("@", 1)[1] not in email_ext:
            raise forms.ValidationError("ایمیل معتبر نیست")
        return email
