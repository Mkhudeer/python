from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Listing


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:

        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]


class ListingForm(forms.ModelForm):

    class Meta:

        model = Listing

        fields = [
            'title',
            'description',
            'category',
            'price',
            'location',
            'contact_details',
            'image'
        ]

    def clean_price(self):

        price = self.cleaned_data.get('price')

        if price <= 0:

            raise forms.ValidationError(
                'Price must be greater than 0'
            )

        return price