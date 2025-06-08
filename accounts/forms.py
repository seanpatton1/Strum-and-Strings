from django import forms
from .models import UserProfile
from .models import NewsletterSubscriber
from orders.models import Order


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    postcode = forms.CharField(max_length=20, required=False)
    country = forms.CharField(max_length=100, required=False)

    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'address',
            'city',
            'postcode',
            'country',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['address'].initial = self.instance.address
            self.fields['city'].initial = self.instance.city
            self.fields['postcode'].initial = self.instance.postcode
            self.fields['country'].initial = self.instance.country

    def save(self, commit=True):
        profile = super().save(commit=False)

        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        profile.address = self.cleaned_data['address']
        profile.city = self.cleaned_data['city']
        profile.postcode = self.cleaned_data['postcode']
        profile.country = self.cleaned_data['country']

        if commit:
            user.save()
            profile.save()
        return profile


class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),
        }


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'})
        }
