import logging
from django.conf import settings
from ..tasks.notify_admin_task import notifyAdminTask


class TelegramBotAlertHandler(logging.Handler):

    # def __init__(self, bot_token, chat_id):
    #     super().__init__()
    #     self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        notifyAdminTask(message=log_entry)
        # if settings.DEBUG:
        # else:
        #     notifyAdminTask.delay(message=log_entry)
        