from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import AuditForm
from .models import Audit
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
def AuditFormView(request):
    sent = False
    if request.method == 'POST':
        audit_form = AuditForm(request.POST, request.FILES)
        if audit_form.is_valid():
            image = audit_form.cleaned_data.get("image")
            first_name = audit_form.cleaned_data.get("first_name")
            last_name = audit_form.cleaned_data.get("last_name")
            email = audit_form.cleaned_data.get("email")
            gender = audit_form.cleaned_data.get("gender")
            phone_number = audit_form.cleaned_data.get("phone_number")
            address = audit_form.cleaned_data.get("address")
            state = audit_form.cleaned_data.get("state")
            guardian_name = audit_form.cleaned_data.get("guardian_name")
            guardian_email = audit_form.cleaned_data.get("guardian_email")
            guardian_phone_number = audit_form.cleaned_data.get("guardian_phone_number")
            role_interested = audit_form.cleaned_data.get("role_interested")
            list_any_talent_or_performing_experience = audit_form.cleaned_data.get("list_any_talent_or_performing_experience")
            do_you_have_any_physical_limitation = audit_form.cleaned_data.get("do_you_have_any_physical_limitation")
            will_you_consider_being_an_extra = audit_form.cleaned_data.get("will_you_consider_being_an_extra")
            will_you_consider_other_roles = audit_form.cleaned_data.get("will_you_consider_other_roles")
            will_you_help_with_production = audit_form.cleaned_data.get("will_you_help_with_production")
            obj = Audit.objects.create(
                image=image,
                first_name=first_name,
                last_name=last_name,
                email=email,
                gender=gender,
                phone_number=phone_number,
                address=address,
                state=state,
                guardian_name=guardian_name,
                guardian_email=guardian_email,
                guardian_phone_number=guardian_phone_number,
                role_interested=role_interested,
                list_any_talent_or_performing_experience=list_any_talent_or_performing_experience,
                do_you_have_any_physical_limitation=do_you_have_any_physical_limitation,
                will_you_consider_being_an_extra=will_you_consider_being_an_extra,
                will_you_consider_other_roles=will_you_consider_other_roles,
                will_you_help_with_production=will_you_help_with_production
            )
            obj.save()
            sent = True
    else:
        audit_form = AuditForm()
    return render(request, 'audit_form.html',{'audit_form':audit_form,'sent':sent})
            
    
 
