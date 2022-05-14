from sys import maxsize
from unittest.util import _MAX_LENGTH
#from typing_extensions import Required
from django import forms
import typing_extensions 

class regerstrationInput(forms.Form):

	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	email = forms.EmailField()
	mobile_no = forms.IntegerField()


