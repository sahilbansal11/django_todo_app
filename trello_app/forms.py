from django import forms
from .models import Task

class TaskFormOld(forms.Form):
  # fields map to the inputs
  name = forms.CharField(max_length=50)
  desc = forms.CharField(widget=forms.Textarea)
  # created_at = forms.CharField(widget=forms.DateTimeInput)
  # due_date = forms.CharField(widget=forms.DateTimeInput)

class TaskForm(forms.ModelForm):
  # allows you to connect with the model directly
  class Meta:
    model = Task
    # fields = '__all__'
    fields = ['name', 'desc', 'due_date', 'list']
    widgets = {
      'due_date': forms.DateTimeInput(attrs = {'type': 'datetime-local'})
    }