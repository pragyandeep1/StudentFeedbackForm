from django import forms
from django.core import validators

# def starts_with_s(value):
#     print('starts_with_s function execution')
#     if value[0].upper() != 'S':
#         raise forms.ValidationError('Name should start with S')

class FeedBackForm(forms.Form):
    # name = forms.CharField(validators=[starts_with_s])
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])

    def clean_name(self):
        print('Validating name field')
        input_name = self.cleaned_data['name']
        if len(input_name)<4:
            raise forms.ValidationError('The minimum number of characters in the name field should be four')
        if input_name.lower() == 'test':
            raise forms.ValidationError('Name "Test" is not allowed.')
        return input_name

    def clean_rollno(self):
        print('Validating roll number field')
        input_rollno = self.cleaned_data['rollno']
        if input_rollno and input_rollno < 0:
            raise forms.ValidationError('Roll number must be a positive integer.')
        return input_rollno

    def clean_email(self):
        print('Validating email field')
        input_email = self.cleaned_data['email']
        return input_email

    def clean_feedback(self):
        print('Validating feedback field')
        input_feedback = self.cleaned_data['feedback']
        return input_feedback