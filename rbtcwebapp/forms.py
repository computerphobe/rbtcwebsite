from django import forms
from .models import IssuedComponent

class IssueComponentForm(forms.ModelForm):
    class Meta:
        model = IssuedComponent
        fields = ['quantity', 'purpose']
    
    quantity = forms.IntegerField(min_value=1, label="Quantity", required=True)
    purpose = forms.CharField(widget=forms.Textarea, label="Purpose", required=True)