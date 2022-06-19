import random

import telebot

token = '1636750747:AAHUpWHP7_V_2AoosLG6fF7zXBrsIO01lDY'


bot = telebot.TeleBot(token)

todos = {} # todos: list -> dict

RANDOM_TASKS = ['Заняться портфелем активов', 'Учить Python', 'Читать умные книги', 'Смотреть сериалы']

HELP = '''
Список доступных команд:
* /print  - напечать все задачи на заданную дату
например: /print 2020-06-03
* /add - добавить задачу
например: /add 2020-06-03 Записаться к стоматологу
* /help - Напечатать help
* /random - Добавить на сегодня случайную задачу

'''

# dict().keys() -> Список ключей
# dict().values() -> Список значений
# value in dict().values()


# 1. Привязка к датам
# Дата
# (в любом формате, 30-11-2020, Сегодня, завтра, когда-нибудь)
# Для каждой даты N задач (N >= 0)

# {"Дата"(string) : [Задачи](list)}

def add_todo(date, task):
  # Проверяем, есть ли такая дата в нашем словаре
  if date in todos:
  # Если дата есть - добавляем в список, который ей соответствует задачу
    # todos[d] -> ['task1', ...]
    # .append('input_task')
    todos[date].append(task)
  else:
    # Если нет - создаем в словаре пару ключ: значение -> Дата: [Задачу]
    todos[date] = [task]
    # todos[d] -> [1 одна задача]
  print(f'Задача {task} добавлена на дату {date}')



@bot.message_handler(commands=["help"])
def help(message):
  bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add"])
def add(message):
  splitted_command = message.text.split(maxsplit=2)
  date = splitted_command[1].lower()
  task = splitted_command[2]
  add_todo(date, task)
  bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(commands=["print"])
def print_tasks(message):
  # /print Дата
  splitted_command = message.text.split()
  date = splitted_command[1].lower()
  text = ''
  if date in todos:
    for task in todos[date]:
      text = text + f"[ ] {task}\n"
  else:
    text = 'Такой даты нет'
  bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_task(message):
  task = random.choice(RANDOM_TASKS)
  add_todo('сегодня', task)
  bot.send_message(message.chat.id, f'Задача {task} добавлена на дату сегодня')


@bot.message_handler(commands=["start"])
def help(message):
  bot.send_message(message.chat.id, HELP)


bot.polling(none_stop=True)
