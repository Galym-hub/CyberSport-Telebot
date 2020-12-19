import telebot
from telebot import types
import config

bot = telebot.TeleBot('1486784639:AAHL_GMS0MTdnJsPz5z2IAB1qbKZkc3DqtE')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Компьютерные Игры')
    btn2 = types.KeyboardButton('Мобильные Игры')
    btn3 = types.KeyboardButton("Платформа для Геймеров")
    btn4 = types.KeyboardButton("Топ 10 игр в Steam")
    btn5 = types.KeyboardButton("Топ 10 игр в EpicGames")
    btn6 = types.KeyboardButton("Новости Киберспорта")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    send_mess = f"Добро пожаловать, {message.from_user.first_name}!\nЯ - <b>{bot.get_me().first_name}</b>, бот созданный для Киберспорта"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    if message.text == 'Компьютерные Игры':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Dota 2", url="https://store.steampowered.com/app/570/Dota_2/")
        url_btn2 = types.InlineKeyboardButton(text="Cyberpunk 2077", url="https://store.steampowered.com/agecheck/app/1091500/")
        url_btn3 = types.InlineKeyboardButton(text="PLAYERUNKNOWN`S BATTLEGROUND", url="https://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/")
        url_btn4 = types.InlineKeyboardButton(text="Counter-Strike: Global Offensive", url="https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/")
        url_btn5 = types.InlineKeyboardButton(text="Grand Theft Auto V", url="https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/")
        url_btn6 = types.InlineKeyboardButton(text="Fortnite", url="https://www.epicgames.com/fortnite/ru/home")
        keyboard.add(url_btn1, url_btn2, url_btn3, url_btn4, url_btn5, url_btn6)
        bot.send_message(message.chat.id, "Здесь собраны ссылки для скачивания лучших Компьютерных игр", parse_mode="html", reply_markup=keyboard)

    elif message.text == 'Мобильные Игры':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="League of Legends: Wild Rift", url="https://wildrift.leagueoflegends.com/")
        url_btn2 = types.InlineKeyboardButton(text="Mobile Legends: BANG BANG", url="https://m.mobilelegends.com/en")
        url_btn3 = types.InlineKeyboardButton(text="PLAYERUNKNOWN`S BATTLEGROUND Mobile", url="http://www.pubgmobile.com/en/event/frostfestival/#page2")
        keyboard.add(url_btn1, url_btn2, url_btn3)
        bot.send_message(message.chat.id, "Здесь собраны ссылки для скачивания лучших Мобильных игр", parse_mode="html", reply_markup=keyboard)

    elif message.text == "Платформа для Геймеров":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn1 = types.InlineKeyboardButton(text="Steam", url="https://store.steampowered.com/?l=russian")
        url_btn2 = types.InlineKeyboardButton(text="EpicGames", url="https://www.epicgames.com/store/en-US/")
        keyboard.add(url_btn1, url_btn2)
        bot.send_message(message.chat.id, "Игровые платформы - онлайн-сервис цифрового распространения компьютерных игр и программ\nЗдесь собран самые распространенные платформы", parse_mode="html", reply_markup=keyboard)

    elif message.text == "Топ 10 игр в Steam":
        s_mess = "Лучшие игры Steam\n\nCounter-Strike: Global Offensive\nSekiro: Shadows Die Twice\nDestiny 2\nMonster Hunter: WorldDota 2\nThe Elder Scrolls OnlineWarframe\nTotal War: Three Kingdoms\nTom Clancy’s Rainbow Six Siege\nPlayerUnknown’s Battlegrounds"
        bot.send_message(message.chat.id, s_mess)

    elif message.text == "Топ 10 игр в EpicGames":
        s_mess = "Лучшие игры Epic Games Store\n\nFortnite\nRocket League\nGrand Theft Auto: Premium Edition\nMudRunner\nRogue Company\nFootball Manager 2020\nCave Story+\nSid Meier's Civilization® VI\nRead Dead Redemption 2\nDauntless"
        bot.send_message(message.chat.id, s_mess)

    elif message.text == "Новости Киберспорта":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_btn = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.cybersport.ru/")
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, "Новости, интервью и обзоры из мира киберспорта и онлайн игр. ", parse_mode="html", reply_markup=keyboard)
        

bot.polling(none_stop=True)

