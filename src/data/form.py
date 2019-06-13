from django import forms
from .models import info
from django.core.exceptions import ValidationError
DEPARTMENTAL= (
    ('I.T.','information technology'),
    ('MECH','MECHANICAL'),
    ('E.E.','electrical')
)

class info1(forms.ModelForm):
    department=forms.ChoiceField(choices=DEPARTMENTAL,required=True)
    class Meta:
        model = info
        fields = [
            'name',
            'email',
            'phone',
            'department',
            'pic' 
        ]

    def clean_phone(self,*args,**kwargs):
        ph = self.cleaned_data.get( "phone")
        if len(ph)==10:
            return ph 
        else:
            raise ValidationError("this is incorrect")    