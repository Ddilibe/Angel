from django import forms
from .models import Audit

class AuditForm(forms.ModelForm):
    class Meta:
        model = Audit
        fields = ('first_name','last_name','image','email','gender','phone_number','address','state','guardian_name','guardian_phone_number','guardian_email','role_interested','list_any_talent_or_performing_experience','do_you_have_any_physical_limitation','will_you_consider_being_an_extra','will_you_consider_other_roles','will_you_help_with_production')
        


