from django.contrib import admin
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse

from .models import *
from .forms import *

# Register your models here.


@admin.register(Teacher)
class TeacherAmin(admin.ModelAdmin):
    list_display = ['first_name',
                    'second_name']

    list_filter = ('first_name',
                   'second_name',
                   'last_name')

    form = TeacherForm


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['short_name',
                    'teacher',
                    'default_room']

    list_filter = ('short_name',
                   'full_name')

    form = DisciplineForm


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ['discipline',
                    'room',
                    'week_day',
                    'week_type',
                    'time']

    list_filter = ('room',
                   'week_day',
                   'week_type')

    form = TimetableForm




@admin.register(HomeworkType)
class HomeworkTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

    form = HomeworkTypeForm


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    change_form_template = "custom_change_form.html"
    list_display = [
                    'exp_date',
                    'type',
                    'subject',
                    'description',
    ]

    list_filter = ('exp_date',
                   'type',
                   'subject')

    form = HomeworkForm

    def response_change(self, request, obj: Homework):
        if "next_pair" in request.POST:
            self.message_user(request, "Подставлена дата следующей пары")
            # from pprint import pp
            # pp(Homework.objects.filter(subject=obj.subject))
            # obj.exp_date = "2022-02-09"
            # obj.save()
            # print(request.POST)
            # form = HomeworkForm(initial=request.POST)
            # form.save()
            # print(form.is_valid())
            # return render(request, 'custom_change_form.html', {'form': form,
            #                                                    'opts': Homework._meta,
            #                                                    'change': True,
            #                                                    'is_popup': False,
            #                                                    'save_as': False,
            #                                                    'has_delete_permission': True,
            #                                                    'has_add_permission': True,
            #                                                    'has_change_permission': True,
            #                                                    'add': True,
            #                                                    'has_view_permission': True,
            #                                                    'has_editable_inline_admin_formsets': True,
            #                                                    })
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


@admin.register(AdminBotUser)
class AdminBotUserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id',
                    'nickname',
                    'full_name',
                    'group_']

    list_filter = ('nickname',
                   'full_name')

    form = AdminBotUserForm

    def group_(self, admin: AdminBotUser):
        return admin.groups.all()[0]

    group_.short_description = 'Группа'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_chat_id',
                    'admins_']

    list_filter = ('group_chat_id',)

    form = GroupForm

    def admins_(self, group):
        admins = [str(admin_.full_name) for admin_ in group.admins.all()]

        if len(admins) > 1:
            return ', '.join(admins)
        elif len(admins) == 1:
            return admins[0]


@admin.register(TimeBot)
class TimeBotAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'start',
                    'end']

    form = TimeBotForm
