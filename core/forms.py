from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Larry Gigli",
        })
    )
    email = forms.EmailField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "deuce_bigalow@aol.com"
        })
    )
    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Oh, hi Mark."
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Ace Ventura, Pet Detective! How are you this afternoon? Alrighty Then!"
        })
    )
