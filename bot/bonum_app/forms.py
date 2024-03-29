from django import forms
from .models import *
from .widgets import *


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name',
                  'second_name',
                  'last_name',
                  'contact'
                  )
        widgets = {
            'first_name': forms.TextInput,
            'second_name': forms.TextInput,
            'last_name': forms.TextInput,
            'contact': forms.TextInput,
        }


class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = ('short_name',
                  'full_name',
                  'teacher',
                  'default_room'
                  )
        widgets = {
            'short_name': forms.TextInput,
            'full_name': forms.TextInput,
            'default_room': forms.TextInput,
        }


class TimeBotForm(forms.ModelForm):
    class Meta:
        model = TimeBot
        fields = ('name',
                  'start',
                  'start1',
                  )
        widgets = {
            'name': forms.TextInput,
            'start': TimePickerInput(),
            'end:': TimePickerInput(),
            'start1': TimePickerInput(),
            'start2': TimePickerInput()
        }


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ('discipline',
                  'room',
                  'week_day',
                  'week_type',
                  'time',
                  'group',
                  )
        widgets = {
            'room': forms.TextInput,
            'contact': forms.TextInput,
        }


class HomeworkTypeForm(forms.ModelForm):
    class Meta:
        model = HomeworkType
        fields = ['name']
        widgets = {
            'name': forms.TextInput,
        }


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('exp_date',
                  'type',
                  'subject',
                  'description',
                  'group',
                  )
        widgets = {
            'exp_date': DatePickerInput(),
            'description': forms.TextInput,
        }


class AdminBotUserForm(forms.ModelForm):
    class Meta:
        model = AdminBotUser
        fields = ('telegram_id',
                  'nickname',
                  'full_name',
                  )
        widgets = {
            'telegram_id': forms.TextInput,
            'nickname': forms.TextInput,
            'full_name': forms.TextInput,
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_chat_id',
                  'admins',
                  'name',
                  )
        widgets = {
            'group_chat_id': forms.TextInput,
            'name': forms.TextInput,
        }
