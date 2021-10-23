from vk_api import vk_api
from random import randint
from vk_api.longpoll import VkLongPoll, VkEventType
import sys, string, os

def InsertDB(u_id, question, table):
    with sqlite3.connect('reqs.db') as db:
        pass


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id":randint(1, 1000)})
token = ''

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)
def msg(i, yot):#метод, пишущий сообщение на основе входящей переменной yot и возвращающий событие
    if i != 0:
        write_msg(i, yot)
    else:
        for event in longpoll.listen():

            # Если пришло новое сообщение
            if event.type == VkEventType.MESSAGE_NEW:
    
                # Если оно имеет метку для меня( то есть бота)
                if event.to_me:
        
                    # Сообщение от пользователя
                    request = event.text
            
                    # Каменная логика ответа
                    if request.lower() == "привет":
                        write_msg(event.user_id, yot)
                    else:
                        write_msg(event.user_id, yot)
                    return event

def answ(id):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.user_id == id and event.to_me:
            return event
def quant(user_id):
    pass

def req_repeat(user_id):
    print('req_repeat')
    question2 = 'Хотели бы вы посетить еще что-то?'
    req = msg(user_id, question2)
    req = answ(user_id)
    print('wrotenIF', req.text)
    if req.text.lower() == 'нет':
        quant(user_id)
    else:
        count_req(user_id)

def count_req(user_id):
    print('count_req')
    question1 = "Какое место вы бы хотели посетить?"
    write_msg(user_id, question1)
    req = answ(user_id)
    #InsertDB(req.user_id, req.text, 0)
    f = open(str(user_id) + '.txt', 'a')#дозапись информации в файл с именем пользователя
    f.write(req.text + '\n')
    f.close()
    print('wroten', req.text)
    #req_repeat(req.user_id)
    question2 = 'Хотели бы вы посетить еще что-то?'
    req = msg(user_id, question2)
    req = answ(user_id)
    print('wrotenIF', req.text)
    if req.text.lower() == 'нет':
        quant(user_id)
    else:
        count_req(user_id)

def begin():#первый метод бота, пишет первое сообщение
    
    
    print('waitMSG')
    t = msg(0, "Это первый (или не очень первый) квантовый навигатов, введите название станции, с которой вы начнете свое путешествие и алгоритм, с помощью квантового компьютера построит вам кратчайший маршурут по всем достопримечательностям Москвы!")
    #f = open('nowUsers', 'a+')
    #users = f.read()
    #use = users.split('\n')
    #b = True
    #for u in use:
    #    if u == t.user_id:
    #        b = False
    #if b:
    #    f.write(str(t.user_id) + '\n')
    #    os.system("quant_chat.py")
    t = answ(t.user_id)
    print('readANSW', t.text)
    fileNewUser = open(str(t.user_id) + '.txt', 'w')
    fileNewUser.write(t.text + '\n')
    fileNewUser.close()
    print('wroteANSW', t.text)
    #count_req(t.user_id)
    #InsertDB(t.user_id, t.text, table)
    write_msg(t.user_id, 'Ваше сообщение будет обработано через 3, 2, 1..')
    begin()
    
begin()
