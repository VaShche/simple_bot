"""

+ хранить историю пользователя

+ имел вложенное меню

отвечать изображениями

отправлять уведомления

умел обрабатывать голосовые сообщения
"""

import telebot as tg
import settings
import user
import func
import datetime
import time
import threading

data_file_name = 'data.data'

bot = tg.TeleBot(settings.token)

users_dict = func.load_dict_from_file(data_file_name)


def create_buttons(cur_user):
    buttons = cur_user.get_user_buttons()
    markup = tg.types.InlineKeyboardMarkup(row_width=2)
    for button in buttons:
        itembtn = tg.types.InlineKeyboardButton(button[0], callback_data=button[1])
        markup.add(itembtn)
    bot.send_message(cur_user.id, cur_user.message, reply_markup=markup)


def remind(bot):
    while True:
        for cur_user in users_dict.values():
            print(cur_user.name)
            delta = datetime.datetime.now() - cur_user.our_date
            delta = delta.total_seconds()
            print(delta)
            for i in [100, 1000, 10000, 100000, 1000000]:
                if delta > i and (i not in cur_user.celebrated):
                    cur_user.celebrated.append(i)
                    bot.send_message(cur_user.id, 'мы знакомы уже больше {0} секунд'.format(i))
            print(delta)
        time.sleep(10)


@bot.message_handler(content_types=["text"])
def text_message(message):
    print('haha')
    print(users_dict)

    cur_user = users_dict.get(message.from_user.id, user.MyUserStory(message.from_user.id, message.from_user.username))

    if cur_user.state == 2:
        cur_user.set_user_reaction(message.text)

    create_buttons(cur_user)

    #записать стейт в словарь
    users_dict[message.from_user.id] = cur_user
    func.save_dict_to_file(data_file_name, users_dict)


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    print(users_dict)

    cur_user = users_dict.get(call.from_user.id, user.MyUserStory(call.from_user.id, call.from_user.username))
    cur_user.set_user_reaction(call.data)
    create_buttons(cur_user)
    #записать стейт в словарь
    users_dict[call.from_user.id] = cur_user
    func.save_dict_to_file(data_file_name, users_dict)


@bot.message_handler(content_types=["audio"])
def text_message(message):
    print('audio')  # TODO Do it!


print('zzz')
threading.Thread(target=remind, args=[bot]).start()
print('zzzzzz')
bot.polling()



