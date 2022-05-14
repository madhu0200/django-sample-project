from usersignin.models import register
from django import forms
  
# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = register
        fields =[
            "fname",
            "lname",
            "email",
            "mobileno",
            "password"
        ]