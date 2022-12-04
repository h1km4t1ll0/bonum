import telebot.types
from .models import *
from .statuses import *


def init_group(admin_list: list[telebot.types.ChatMember],
               group_chat: telebot.types.Chat) -> Status | str:
    """
    New group initialization
    """
    try:
        if Group.objects.filter(group_chat_id=int(group_chat.id)):
            return 'model exists'

        group = Group(group_chat_id=int(group_chat.id))
        group.save()

        for admin in admin_list:
            AdminBotUser(telegram_id=int(admin.user.id),
                         nickname=admin.user.username,
                         full_name=f'{admin.user.first_name} {admin.user.last_name}').save()
            group.admins.add(AdminBotUser.objects.get(telegram_id=int(admin.user.id)))

        group.save()
        return SuccessStatus()

    except Exception as e:
        return ExceptionStatus(e)


def check_existence(model: models.Model,
                    instance: models.Model) -> Existence:
    if len(model.objects.filter(id=instance.id)):
        return Exists()
    return NotExists()
