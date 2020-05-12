from editor.editor import Edit
from lilly import Lilly
import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

vk = vk_api.VkApi(token='7f96a10670be2276b0caf5c76cbabe515095b92a6e8befcd4f0f80cabd982598d02b44528895be13232b2')
vk_s = vk.get_api()

lilly = Lilly()  # Ядро бота

longpoll = VkBotLongPoll(vk, 193285257)  # VkApi, group_id

# Слушаем сервер
for event in longpoll.listen():

    # Новое сообщение
    if event.type == VkBotEventType.MESSAGE_NEW:
        print('Новое сообщение:')

        if event.group_id:
            print(event.object.from_id, 'пишет: ')

            vk_s.messages.send(peer_id=event.object.peer_id,
                               message=lilly.update_screen(
                                   Edit.clean_str_from_symbol(event.object.text, "[", "]")[1::]),
                               random_id=event.object.random_id)

            print('Текст: ', event.object.text, end="\n")
