import telebot
import json
import os
from telebot import types

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)


def load_karting_data(period):
	with open(f'karting_data_{period}.json', 'r') as json_file:
		return json.load(json_file)


def load_users_data():
	if os.path.exists('users_log.json'):
		with open('users_log.json', 'r') as user_log_file:
			return json.load(user_log_file)
	return {}


def format_top10_message(period):
	karting_data = load_karting_data(period)
	period_text = {
		"1d": "за последний день",
		"7d": "за последние 7 дней",
		"14d": "за последние 14 дней"
	}
	count = len(karting_data)
	top_10_message = f"Топ {count if count < 10 else 10} лучших картов {period_text[period]}:\n"
	for kart in karting_data[:10]:
		spaces = "    " if len(kart['kart_number']) == 2 else "      "
		top_10_message += f"*{kart['kart_number']}*{spaces}*{kart['lap_time']}*\n"
	return top_10_message


def update_user_messages():
	users_data = load_users_data()
	for user_id, user_info in users_data.items():
		chat_id = user_info['user_id']
		message_id = user_info['message_id']

		top_10_message = format_top10_message('1d')
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("1 day", callback_data="1d"))
		markup.add(types.InlineKeyboardButton("7 days", callback_data="7d"))
		markup.add(types.InlineKeyboardButton("14 days", callback_data="14d"))

		try:
			bot.edit_message_text(top_10_message, chat_id, message_id, reply_markup=markup, parse_mode='Markdown')
		except telebot.apihelper.ApiTelegramException as e:
			if 'message is not modified' in str(e):
				pass
			else:
				print(f"Не удалось обновить сообщение для пользователя {chat_id}: {e}")


update_user_messages()
