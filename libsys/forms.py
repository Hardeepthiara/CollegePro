



from django.forms import ModelForm
from libsys.models import Student
from crispy_forms.helper import FormHelper

class StudentForm(ModelForm):
	class Meta:
		model=Student
		fields=['name', 'regno', 'accno']
	def __init__(self, *args, **kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.form_class='form-horizontal'
		self.helper.label_class='col-md-offset-1 col-md-2'
		self.helper.field_class='col-md-8'




