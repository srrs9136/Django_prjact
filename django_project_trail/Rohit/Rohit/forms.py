from django import forms
# first one
class AddForm(forms.Form):
    addend0 = forms.IntegerField()
    addend1 = forms.IntegerField()
    
#secound wala   
    
class calForm(forms.Form):
    number1 = forms.IntegerField()
    number2 = forms.IntegerField()
    # number3 = forms.IntegerField()
    
    