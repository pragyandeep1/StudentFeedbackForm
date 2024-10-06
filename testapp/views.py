from django.shortcuts import render
from testapp.forms import FeedBackForm

# Create your views here.
def feedback_view(request):
    submitted = False
    name = ''
    form = FeedBackForm()
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print('Form validation successful. Now printing..')
            print('='*50)
            print('Name:', form.cleaned_data['name'])
            print('Roll No:', form.cleaned_data['rollno'])
            print('Email:', form.cleaned_data['email'])
            print('Feedback:', form.cleaned_data['feedback'])
            submitted = True
        else:
            print('Some field validation failed.')
    return render(request, 'testapp/feedback.html', {'form': form, 'submitted': submitted, 'name': name})