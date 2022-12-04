import telebot.types
from models import *
from statuses import *


def init_group(admin_list: list[telebot.types.ChatMember],
               group_chat: telebot.types.Chat) -> SuccessStatus:
    """
    New group initialization
    """

    group = Group(group_chat_id=int(group_chat.id))

    for admin in admin_list:
        new_admin = AdminBotUser(telegram_id=admin.user.id,
                                 nickname=admin.user.username,
                                 full_name=f'{admin.user.first_name} {admin.user.last_name}')
        group.admin.add()

    return SuccessStatus()
