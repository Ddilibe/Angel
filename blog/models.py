from django.db import models
from phone_field import PhoneField


class Audit(models.Model):
    gen = (
        ('Male', 'Male'),
        ('Female','Female'),
    )
    diff = (
        ('Yes','Yes'),
        ('No','No'),
    )
    image = models.ImageField(upload_to = 'auditionpic/')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.CharField(max_length=8, choices=gen)
    phone_number = PhoneField(blank=False, help_text='Your Phone Number')
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    guardian_name = models.CharField(max_length = 250)
    guardian_email = models.CharField(max_length=100 )
    guardian_phone_number = PhoneField(blank=False,help_text = 'Parent Phone Number')
    role_interested = models.TextField()
    list_any_talent_or_performing_experience = models.TextField()
    do_you_have_any_physical_limitation = models.TextField()
    will_you_consider_being_an_extra = models.CharField(max_length=4, choices=diff)                     
    will_you_consider_other_roles = models.CharField(max_length=4, choices=diff)
    will_you_help_with_production = models.CharField(max_length=4, choices=diff)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name
        
        
        
