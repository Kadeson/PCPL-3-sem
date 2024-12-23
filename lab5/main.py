import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

bot = telebot.TeleBot("7890336716:AAEBYqOCADBQpDDfXpz-WRdR7xKxqP1LOKI")

notes = {}


def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Добавить заметку", callback_data="add_note"),
        InlineKeyboardButton(text="Мои заметки", callback_data="view_notes"),
    )
    return keyboard


@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(message.chat.id,"Бот для заметок. Выберите действие:",reply_markup=get_main_keyboard())

@bot.callback_query_handler(func=lambda call: call.data in ["add_note", "view_notes"])
def process_callback(call: CallbackQuery):
    user_id = call.from_user.id

    if call.data == "add_note":
        msg = bot.send_message(user_id, "Введите текст заметки:")
        bot.register_next_step_handler(msg, add_note_handler)
        bot.answer_callback_query(call.id)

    elif call.data == "view_notes":
        if user_id in notes and notes[user_id]:
            text = "Ваши заметки:\n" + "\n".join([f"{i + 1}. {note}" for i, note in enumerate(notes[user_id])])
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(InlineKeyboardButton("Удалить заметку", callback_data="delete_note"))
            bot.send_message(user_id, text, reply_markup=keyboard)
        else:
            bot.send_message(user_id, "У вас пока нет заметок.")
        bot.answer_callback_query(call.id)


def add_note_handler(message):
    user_id = message.from_user.id
    if user_id not in notes:
        notes[user_id] = []
    notes[user_id].append(message.text)
    bot.send_message(user_id, "Заметка успешно добавлена!", reply_markup=get_main_keyboard())


@bot.callback_query_handler(func=lambda call: call.data == "delete_note")
def delete_note_handler(call: CallbackQuery):
    user_id = call.from_user.id
    if user_id in notes and notes[user_id]:
        keyboard = InlineKeyboardMarkup(row_width=1)
        for i, note in enumerate(notes[user_id]):
            keyboard.add(InlineKeyboardButton(text=note, callback_data=f"del_{i}"))
        bot.send_message(user_id, "Выберите заметку для удаления:", reply_markup=keyboard)
    else:
        bot.send_message(user_id, "У вас пока нет заметок.")
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("del_"))
def confirm_delete_handler(call: CallbackQuery):
    user_id = call.from_user.id
    note_index = int(call.data.split("_")[1])

    if user_id in notes and 0 <= note_index < len(notes[user_id]):
        deleted_note = notes[user_id].pop(note_index)
        bot.send_message(user_id, f"Заметка '{deleted_note}' удалена!", reply_markup=get_main_keyboard())
    else:
        bot.send_message(user_id, "Ошибка: заметка не найдена.")
    bot.answer_callback_query(call.id)


if __name__ == "__main__":
    bot.infinity_polling()
