import telebot
from telebot import types

bot = telebot.TeleBot("1435672237:AAEZ8eSPiXxSPlodlprLVFZDgp6bCyk5QbA")


@bot.message_handler(commands=['start'])
def wellcome(message):
    markup = types.ReplyKeyboardMarkup()
    buti = types.KeyboardButton('Tenses')
    markup.add(buti)
    bot.send_message(message.chat.id, 'Hi, learner!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == 'Tenses':
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton('Present Simple')
        button2 = types.KeyboardButton('Past Simple')
        button3 = types.KeyboardButton('Future')
        button4 = types.KeyboardButton('Present Perfect')
        button5 = types.KeyboardButton('Past Perfect')
        button6 = types.KeyboardButton('Future Perfect')
        button7 = types.KeyboardButton('Present Continuous')
        button8 = types.KeyboardButton('Past continuous')
        button9 = types.KeyboardButton('Future Continuous')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
        bot.send_message(message.chat.id, 'Here are Tenses', reply_markup=markup)

    if message.text == 'Present Simple':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Practice', callback_data='Present Simple1')
        item2 = types.InlineKeyboardButton('The short lesson', callback_data='Present Simple2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         '''S + V + Obj     (The simple present is a verb tense with two main uses. We use the simple present tense when an action is happening right now, or when it happens regularly (or unceasingly, which is why it’s sometimes called present indefinite). Depending on the person, the simple present tense is formed by using the root form or by adding ‑s or ‑es to the end.)''',
                         reply_markup=markup)



    elif message.text == 'Past Simple':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Practice', callback_data='Past Simple1')
        item2 = types.InlineKeyboardButton('The short lesson', callback_data='Past Simple2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         "S + V(2) + Obj    (The simple past is a verb tense that is used to talk about things that happened or existed before now. Imagine someone asks what your brother Wolfgang did while he was in town last weekend.)",
                         reply_markup=markup)

    elif message.text == 'Future':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Practice', callback_data='Future1')
        item2 = types.InlineKeyboardButton('The short lesson', callback_data='Future2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         "S + will + V  (The simple future tense is used when an action is promised/thought to occur in the future.)",
                         reply_markup=markup)


    elif message.text == 'Present Perfect':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Practice', callback_data='Present Perfect1')
        item2 = types.InlineKeyboardButton('The short lesson', callback_data='Present Perfect2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         "S + have/has + V(3)    (The present perfect tense refers to an action or state that either occurred at an indefinite time in the past (e.g., we have talked before) or began in the past and continued to the present time)",
                         reply_markup=markup)

    elif message.text == 'Past Perfect':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Practice', callback_data='Past Perfect1')
        item2 = types.InlineKeyboardButton('The short lesson', callback_data='Past Perfect2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         "S + had + V(3)    (The past perfect tense is for talking about something that happened before something else. Imagine waking up one morning and stepping outside to grab the newspaper.  The past perfect, also called the pluperfect, is a verb tense used to talk about actions that were completed before some point in the past.)",
                         reply_markup=markup)

    elif message.text == 'Future Perfect':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Practice', callback_data='Future Perfect1')
        item2 = types.InlineKeyboardButton('The short lesson', callback_data='Future Perfect2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         "S + will have + V(3)    (The future perfect tense expresses action that will be finished at some point in the future.)",
                         reply_markup=markup)

    elif message.text == 'Present Continuous':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Practice', callback_data='Present Continuous1')
        item2 = types.InlineKeyboardButton('The short lesson', callback_data='Present Continuous2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         "S + to be(am,is,are) + V+ing    (The present continuous (also called present progressive) is a verb tense which is used to show that an ongoing action is happening now, either at the moment of speech or now in a larger sense. The present continuous can also be used to show that an action is going to take place in the near future.)",
                         reply_markup=markup)

    elif message.text == 'Past continuous':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Practice', callback_data='Past Continuous1')
        item2 = types.InlineKeyboardButton('The short lesson', callback_data='Past Continuous2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         "S + was/were + V+ing   (The past continuous tense is used to describe actions that began in the past and often continued for a short period of time after the action started. This tense describes actions or events that happened at a specific time in the past.)",
                         reply_markup=markup)

    elif message.text == 'Future Continuous':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Practice', callback_data='Future Continuous1')
        item2 = types.InlineKeyboardButton('The short lesson', callback_data='Future Continuous2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         "S + will + be + V+ing     (The future continuous tense, sometimes also referred to as the future progressive tense, is a verb tense that indicates that something will occur in the future and continue for an expected length of time.)",
                         reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data == 'Present Simple1':
            bot.send_message(call.message.chat.id, 'https://www.ego4u.com/en/cram-up/tests/simple-present-1')
        elif call.data == 'Present Simple2':
            bot.send_message(call.message.chat.id, "PRESENT SIMPLE - https://youtu.be/XkY4mo0VcIQ")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message, reply_mark=None)
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='это тестовое уведомление')
        if call.data == 'Past Simple1':
            bot.send_message(call.message.chat.id, 'https://www.ego4u.com/en/cram-up/tests/simple-past-1')
        elif call.data == 'Past Simple2':
            bot.send_message(call.message.chat.id, 'PAST SIMPLE - https://youtu.be/xLA58CSIf3M')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message, reply_mark=None)
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='это тестовое уведомление')

        if call.data == 'Future1':
            bot.send_message(call.message.chat.id,
                             'https://www.englishclub.com/grammar/verb-tenses_future-simple-quiz.htm')
        elif call.data == 'Future2':
            bot.send_message(call.message.chat.id, 'FUTURE TENSE- https://youtu.be/qMKEgZ7SKwY')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message, reply_mark=None)
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='это тестовое уведомление')
        if call.data == 'Present Perfect1':
            bot.send_message(call.message.chat.id, 'https://www.ego4u.com/en/cram-up/tests/present-perfect-simple-1')
        elif call.data == 'Present Perfect2':
            bot.send_message(call.message.chat.id, 'PRESENT PERFECT - https://youtu.be/5vJOJrVIgek')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message, reply_mark=None)
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='это тестовое уведомление')

        if call.data == 'Past Perfect1':
            bot.send_message(call.message.chat.id,
                             'https://www.englishclub.com/grammar/verb-tenses_past-perfect-quiz.htm')
        elif call.data == 'Past Perfect2':
            bot.send_message(call.message.chat.id, 'PAST PERFECT - https://youtu.be/mOQ_VnC6dtU')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message, reply_mark=None)
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='это тестовое уведомление')

        if call.data == 'Future Perfect1':
            bot.send_message(call.message.chat.id,
                             'https://www.englishclub.com/grammar/verb-tenses_future-perfect-quiz.htm')
        elif call.data == 'Future Peerfect2':
            bot.send_message(call.message.chat.id, 'FUTURE PERFECT - https://youtu.be/JBmsega_fgE')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message, reply_mark=None)
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='это тестовое уведомление')

        if call.data == 'Present Continuous1':
            bot.send_message(call.message.chat.id,
                             'https://www.englishclub.com/grammar/verb-tenses_present-continuous_quiz.htm')
        elif call.data == 'Present Continuous2':
            bot.send_message(call.message.chat.id, 'PRESENT CONTINUOUS - https://youtu.be/oBbJNjjSYBo''')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message, reply_mark=None)
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='это тестовое уведомление')

        if call.data == 'Past Continuous1':
            bot.send_message(call.message.chat.id,
                             'https://www.englishclub.com/grammar/verb-tenses_past-continuous-quiz.htm')
        elif call.data == 'Past Continuous2':
            bot.send_message(call.message.chat.id, 'PAST CONTINUOUS - https://youtu.be/Lm7BJV3sizM')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message, reply_mark=None)
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='это тестовое уведомление')

        if call.data == 'Future Continuous1':
            bot.send_message(call.message.chat.id,
                             'https://www.englishclub.com/grammar/verb-tenses_future-continuous-quiz.htm')
        elif call.data == 'Future Continuous2':
            bot.send_message(call.message.chat.id, 'FUTURE CONTINUOUS - https://youtu.be/dWwwfyOD4rw')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message, reply_mark=None)
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='это тестовое уведомление')

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)