from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from django import forms


# class CustomSignupForm(SignupForm):
#     # first_name = forms.CharField(max_length=25, label='First Name')
#     # last_name = forms.CharField(max_length=25, label='Last Name')
#     age = forms.IntegerField(min_value=0 , label='Age')
#
#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         print(user)
#         # user.first_name = self.cleaned_data['first_name']
#         # user.last_name = self.cleaned_data['last_name']
#         user.age = self.cleaned_data['age']
#         user.save()
#         return user


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        print(self.fields)
    class Meta:
        model = get_user_model()
        fields = ('email',)





class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'age')

