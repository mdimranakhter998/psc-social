from django.contrib import admin
from .models import Contact,SignUp,Profile
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','message']


# signup models register
@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','password']

# token model register
@admin.register(Profile)
class TokenAdmin(admin.ModelAdmin):
    list_display=['user','token','is_verified','created_date']
