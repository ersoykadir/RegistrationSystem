from django import forms

instructorFormFields = ["username", "email", "password", "name", "surname", "department","title"]
studentFormFields = ["username", "email", "password", "name", "surname", "department","studentId"]

class AddUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
    surname = forms.CharField(widget=forms.TextInput())
    department = forms.CharField(widget=forms.TextInput())

class AddStudentForm(forms.Form):
    studentId = forms.IntegerField()
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
    surname = forms.CharField(widget=forms.TextInput())
    department = forms.CharField(widget=forms.TextInput())

class AddInstructorForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
    surname = forms.CharField(widget=forms.TextInput())
    department = forms.CharField(widget=forms.TextInput())
    title= forms.CharField(widget=forms.TextInput())

class GetStudentForm(forms.Form):
    studentId = forms.IntegerField()

class UpdateInstructorForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    title = forms.CharField(widget=forms.TextInput())
class GetInstructorForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())

class GetCourseForm(forms.Form):
    courseId = forms.CharField(widget=forms.TextInput())