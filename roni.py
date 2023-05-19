# using packages
import telebot
from telebot import types

# Bot token from the Telegram-BotFather
TOKEN = '6100195221:AAEYF4e4gMJVGZQz6jC3iiIUODnD1Kmrgbg'

# first questions and answers
first_questions = {
    'Angst-/ Panikstörungen': 'Tut mir leid zu hören, dass du eventuell Angst-/ Panikstörungen hast.',
    'Depressionen': 'Tut mir leid zu hören, dass du eventuell Depressionen hast',
    'Erschöpfungssyndrom': 'Tut mir leid zu hören, dass du eventuell das Erschöpfungssyndrom hast',
    'Konzentrationsstörungen': 'Tut mir leid zu hören, dass du eventuell Konzentrationsstörungen hast',
}

# following questions for Angst-/ Panikstörungen
angst_questions = {
    'Soforthilfe/ Notfall für Angst-/ Panikstörungen': 'Hier findest du schnell Hilfe:\n- Telefonnummer für eine Seelensorge: 0800/1110111\n- Du willst mit keinem persönlich reden? Kein Problem!\nHier kannst du mit Ärzten ganz schnell und einfach chatten: https://www.justanswer.de/sip/arzt?r=ppc|ga|8|||&JPKW=angst%20und%20panikattacken&JPDC=S&JPST=&JPAD=614454087033&JPMT=b&JPNW=g&JPAF=txt&JPRC=1&JPCD=&JPOP=&cmpid=51512544&agid=19388943984&fiid=&tgtid=kwd-110514724&ntw=g&dvc=c&gclid=CjwKCAjwiOCgBhAgEiwAjv5whKYwKeo_JqAGJo6e6dIouOK0xvka3Dgb25Rd50_qN_dCxx_KWEZdKxoCiA0QAvD_BwE \n\nIch hoffe sehr, dass ich dir helfen konnte und dass es dir schon bald besser geht!',
    'Definition von Angst-/ Panikstörungen': 'Die Angst-/Panikstörung definiert sich dadurch, dass Angstreaktionen in eigentlich ungefährlichen Situationen auftreten. Die Angst steht in keinem angemessenen Verhältnis zur tatsächlichen Bedrohung. Betroffene erleben die Angst dennoch psychisch und körperlich sehr intensiv. \n\nFolgende Symptome können auftreten:\n- Angst vor der Angst selbst \n- Vermeidungsverhalten\n- Isolierung von anderen',
    'Behandlung von Angst-/ Panikstörungen': 'Die Behandlung einer Angststörung besteht meist aus einer Psychotherapie und Medikamenten. Je nach Ausprägung der Erkrankung kann zudem eine klinisch-psychologische Behandlung hilfreich sein. Die Symptome können durch eine Behandlung gemildert werden bzw. auch komplett wegfallen.\nFolgende Therapien könnten in einer Klinik in Betracht gezogen werden:\n- Indikative Gruppen, wie Angstbewältigungsgruppe oder Post-Covid-Syndrom-Folgen einer Covid-Erkrankung (Hier können sich Betroffene zu ihren Erfahrungen austauschen und sich gegenseitig unterstützen).\n- Einzelpsychotherapie\n- Hirnleistungstraining\n- Sport- oder Bewegungsprogramme\n- Entspannungstherapien\n- Kreativtherapie, z. B. Kunst- oder Musiktherapie\n\nWenn dich irgendwas davon anspricht, nimm gerne den Kontakt zu MEDICLIN auf. Zu MEDICLIN gehören bundesweit 34 Kliniken, sechs Pflegeeinrichtungen und elf Medizinische Versorgungszentren: https://www.seepark-klinik.de/fachbereiche-krankheitsbilder/krankheitsbilder-a-z/psychische-folgen-der-corona-pandemie/#wer-sie-behandelt.',
}
# following questions for Depression
depression_questions = {
    'Soforthilfe/ Notfall für Depressionen': 'tbd',
    'Definition von Depressionen': 'Depri',
    'Behandlung von Depressionen': 'tbd',
}

# following questions for Erschöpfungssyndrom
erschoepfung_questions = {
    'Soforthilfe/ Notfall für das Erschöpfungssysndrom': 'tbd',
    'Definition von dem Erschöpfungssyndrom': 'tbd',
    'Behandlung von dem Erschöpfungssyndrom': 'tbd',
}

# following questions for Konzentrationsstörungen
konzentration_questions = {
    'Soforthilfe/ Notfall für Konzentrationsstörungen': 'tbd',
    'Definition von Konzentrationsstörungen': 'tbd',
    'Behandlung von Konzentrationsstörungen': 'tbd',
}
# creates the bot using the Token from Telegram-BotFather
bot = telebot.TeleBot(TOKEN)

# function to start the program with the /start command in Telegram
@bot.message_handler(commands=['help', 'start'])
def telegram_start(message):
    markup = types.ReplyKeyboardMarkup()
    for question in first_questions:
        markup.add(types.KeyboardButton(question))
    bot.send_message(message.chat.id, 'Hallo \N{smiling face with smiling eyes} \n\nIch heiße Roni und bin ein Bot. Ich kenne mich sehr gut mit den psychosomatischen Störungen aus, die durch die Pandemie mit Covid-19 verursacht wurden. Hoffentlich kann ich Dir bei der Beantwortung Deiner Fragen behilflich sein. \n\nZu welcher psychosomatischen Störung möchtest Du mehr Informationen?\n\nBitte klicke auf eine der zur Auswahl stehenden Antworten \N{speech balloon}.', reply_markup=markup)



# function to handle the second questions
@bot.message_handler(func=lambda message: message.text in first_questions)
def handle_first_messages(message):
    question = message.text
# for choosing or writing the possible questions
    # if question in first_questions:
    if question == 'Angst-/ Panikstörungen':
        answer = first_questions[question]
        markup = types.ReplyKeyboardMarkup()
        for q in angst_questions:
            markup.add(types.KeyboardButton(q))
        bot.reply_to(message, answer + '\n\nWelche Informationen benötigst du zu Angststörungen?', reply_markup=markup)
    elif question == 'Depressionen':
        answer = first_questions[question]
        markup = types.ReplyKeyboardMarkup()
        for q in depression_questions:
            markup.add(types.KeyboardButton(q))
        bot.reply_to(message, answer + '\n\nWelche Informationen benötigst du zu Depressionen?', reply_markup=markup)
    elif question == 'Erschöpfungssyndrom':
        answer = first_questions[question]
        markup = types.ReplyKeyboardMarkup()
        for q in erschoepfung_questions:
            markup.add(types.KeyboardButton(q))
        bot.reply_to(message, answer + '\n\nWelche Informationen benötigst du zum Erschöpfungssyndrom?', reply_markup=markup)
    elif question == 'Konzentrationsstörungen':
        answer = first_questions[question]
        markup = types.ReplyKeyboardMarkup()
        for q in konzentration_questions:
            markup.add(types.KeyboardButton(q))
        bot.reply_to(message, answer + '\n\nWelche Informationen benötigst du zu Konzentrationsstörungen?', reply_markup=markup)
    else:
        # If the user wrote something else than the possible questions
        bot.reply_to(message, 'Bitte wähle eine der vorgeschlagenen Fragen aus. Nur so kann ich dir behilflich sein.', reply_markup=telebot.types.ReplyKeyboardRemove())


# function to handle the third questions
@bot.message_handler(func=lambda message: True)
def handle_second_messages(message):
    question = message.text
# for choosing or writing the possible questions
    if question in angst_questions:
        answer = angst_questions[question]
        markup = types.ReplyKeyboardMarkup()
        for question in angst_questions:
            markup.add(types.KeyboardButton(question))
        bot.reply_to(message, answer + '\n\nHast du weitere Fragen zu Angststörungen?', reply_markup=markup)
    elif question in depression_questions:
        answer = depression_questions[question]
        markup = types.ReplyKeyboardMarkup()
        for question in depression_questions:
            markup.add(types.KeyboardButton(question))
        bot.reply_to(message, answer + '\n\nHast du weitere Fragen zu Depressionen?', reply_markup=markup)
    elif question in erschoepfung_questions:
        answer = erschoepfung_questions[question]
        markup = types.ReplyKeyboardMarkup()
        for question in erschoepfung_questions:
            markup.add(types.KeyboardButton(question))
        bot.reply_to(message, answer + '\n\nHast du weitere Fragen zum Erschöpfungssyndrom?', reply_markup=markup)
    elif question in konzentration_questions:
        answer = konzentration_questions[question]
        markup = types.ReplyKeyboardMarkup()
        for question in konzentration_questions:
            markup.add(types.KeyboardButton(question))
        bot.reply_to(message, answer + '\n\nHast du weitere Fragen zu Konzentrationsstörungen?', reply_markup=markup)
    else:
        # If the user wrote something else than the possible questions
        bot.reply_to(message, 'Bitte wähle eine der vorgeschlagenen Fragen aus. Nur so kann ich dir behilflich sein.', reply_markup=telebot.types.ReplyKeyboardRemove())


# Start the bot
bot.polling()
