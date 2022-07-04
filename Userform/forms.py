from django import forms


class Pick_and_Drop(forms.Form):
    pick=forms.CharField(max_length=256)
    drop=forms.CharField(max_length=256)
    
    