from django import forms
from django.db.models import Q
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Password COnfirmation', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name', 'email', 'phone_no')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")

        return password2   

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()

        return user   


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'name','email','password', 'phone_no', 
            'is_active', 'is_staff', 'is_admin' 
        )

    def clean_password(self):
        return self.initial['password']


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Name'
            }
        )
    )
    email = forms.EmailField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : 'email',
                # 'pattern':"[a-z]+@[bcc]+\.[gov]+\.[.bd]",
                'placeholder':'ahasanul.hadi@bcc.gov.bd'
            }
        )
    )
    phone_no = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'pattern':"[0-9]{3}[0-9]{4}[0-9]{4}",
                'placeholder': '01722512814'
            }
        )
    )    
    password1 = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : 'password',
                'pattern':".{8,}",
                'placeholder': 'Password'
            }
        )
    ) 
    password2 = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : 'password',
                'pattern':".{8,}",
                'placeholder': 'Confirm Password'
            }
        )
    )   

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'phone_no',
            'password1',
            'password2'
        ]
    
    def cleaned_email(self):
        error_message = {
            'duplicate_email' : 'email is already taken'
        }
        email = self.cleaned.data.get('email')

        try:
            User.objects.get(email = email)
            raise forms.ValidationError(
            error_message['duplicate_email'],
            code='duplicate_email'
        )
        except User.DoesNotExist:
            return email

    def cleaned_phone_no(self):
        error_message = {
            'duplicate_phone_no' : 'Number is already taken'
        }
        phone_no = self.cleaned.data.get('phone_no')

        try:
            User.objects.get(phone_no = phone_no)
            raise forms.ValidationError(
            error_message['duplicate_phone_no'],
            code='duplicate_phone_no'
        )
        except User.DoesNotExist:
            return phone_no    
    
    
class UserLoginForm(forms.Form):
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'type':'email',
                'placeholder': 'Email',
                'required':True
            }
        ) 
    )
    password = forms.CharField(
        label='Password',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'type':'password',
                'placeholder': 'Password',
                'required':True
            }
        ) 
    )

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user_qs_final = User.objects.filter(Q(email__iexact = email)).distinct()
        if not user_qs_final.exists() or user_qs_final.count() != 1:
            raise forms.ValidationError("User does not exist")    
        user_obj = user_qs_final.first() 
        if not user_obj.check_password(password):
            raise forms.ValidationError("Credentails are not correct")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)

class CustomUserSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserSuperForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_no'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enter your Phone Number'})
        self.fields['user_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_admin'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_staff'].widget.attrs.update({'class': 'form-control'})

        
    class Meta:
        model = CustomUser
        fields = ['name','phone_no', 'user_type','is_active','is_admin', 'is_staff'] 

class CustomUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_no'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enter your Phone Number'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_admin'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_staff'].widget.attrs.update({'class': 'form-control'})

        
    class Meta:
        model = CustomUser
        fields = ['name','phone_no','is_active','is_admin', 'is_staff']         


class EmployeeUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeUserForm, self).__init__(*args, **kwargs)
        self.fields['phone_no'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enter your Phone Number'})

    class Meta:
        model = CustomUser
        fields = ['phone_no', ]