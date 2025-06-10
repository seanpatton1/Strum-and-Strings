from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, label='First Name *')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name *')
    email = forms.EmailField(required=True, label='Email Address *')
    phone = forms.CharField(max_length=20, required=True, label='Phone Number *')
    street_address1 = forms.CharField(max_length=255, required=True, label='Street Address *')
    street_address2 = forms.CharField(max_length=255, required=False, label='Address Line 2 (Optional)')
    country = forms.CharField(max_length=100, required=True, label='Country *')
    postal_code = forms.CharField(max_length=20, required=True, label='Postal Code *')
    town_or_city = forms.CharField(max_length=100, required=True, label='Town or City *')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
