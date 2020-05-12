import vk_api
from lilly import Lilly
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, s):
    vk.method('messages.send', {'peer_id': user_id, 'message': s, 'random_id':123456})


# Авторизуемся как сообщество
vk = vk_api.VkApi(token='7f96a10670be2276b0caf5c76cbabe515095b92a6e8befcd4f0f80cabd982598d02b44528895be13232b2')

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Словарь, где будут хранится разные объекты бота для разных пользователей
users_bot_class_dict = {}


def run():
    print("Server started")
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:

                print('New message:')
                print('For me by: ', end='')

                print(event.user_id)

                user_id = event.user_id
                if user_id not in users_bot_class_dict:
                    users_bot_class_dict[user_id] = Lilly()

                # Checking to welcome message send
                if users_bot_class_dict[user_id].WELCOME_MSG_SEND:
                    write_msg(event.user_id, users_bot_class_dict[user_id].update_screen(event.text))
                else:
                    write_msg(event.user_id, users_bot_class_dict[user_id].get_welcome_msg(event.user_id))

                print('Text: ', event.text)
                print()


print("Lilly_Test is ready")
