import requests
from django.conf import settings


def send_bot_message(message: str):

    if len(message) > 4096:
        message = message[:4096]

    message = message.replace("@", "")
    if settings.THREAD_ID is not None:
      url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.ADMIN_CHAT_ID}&message_thread_id={settings.THREAD_ID}&text={message}"
    else:
      url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.ADMIN_CHAT_ID}&text={message}"
    res = requests.get(f"{url}&parse_mode=HTML")
    if res.status_code == 400:
        res = requests.get(url)
    return res