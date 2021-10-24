import os
import logging
from typing import Set
from random import randint

import sqlite3
from vk_api import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from . import BOTS_CACHE_DIR
from configs import ProjConfig

logger = logging.getLogger(__name__)


def insert_db(u_id, question, table):
    with sqlite3.connect('reqs.db') as db:
        pass


class VkBot:
    current_users_filename = "nowUsers"

    logger = logging.getLogger(__name__ + ".VkBot")
    used_uids: Set[int] = {}  # used user ids

    def __init__(self, proj_config: ProjConfig):
        logger.debug("Starting init of VkBot")
        self.vk = vk_api.VkApi(token=proj_config.vk_token)
        self.longpoll = VkLongPoll(self.vk)
        logger.debug("End init of VkBot")

    def write_msg(self, user_id, message):
        self.vk.method(
            'messages.send',
            {'user_id': user_id, 'message': message, "random_id": randint(1, 1000)})

    def msg(self, i, yot):
        """
        Метод, пишущий сообщение на основе входящей переменной yot и возвращающий событие

        Args:
            i:
            yot:

        Returns:

        """
        if i != 0:
            self.write_msg(i, yot)
            return

        for event in self.longpoll.listen():
            if event.type != VkEventType.MESSAGE_NEW:  # Если не пришло новое сообщение:
                continue
            # Иначе: пришло новое сообщение

            if not event.to_me:  # Если оно имеет метку для бота:
                continue
            # Иначе: имеет метку для бота

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request.lower() == "привет":
                self.write_msg(event.user_id, yot)
            else:
                self.write_msg(event.user_id, yot)
            return event

    def answer(self, user_id):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.user_id == user_id and event.to_me:
                return event

    def quant(self, user_id):
        pass

    def req_repeat(self, user_id):
        logger.debug(f'[#{user_id}] Starting of req_repeat()')
        question2 = 'Хотели бы вы посетить еще что-то?'
        _ = self.msg(user_id, question2)
        req = self.answer(user_id)
        logger.info(f'[#{user_id}] Got answer: "{req.text}"')
        if req.text.lower() == 'нет':
            self.quant(user_id)  # Start of route processing with quantum computer
        else:
            self.count_req(user_id)

    def count_req(self, user_id):
        logger.debug(f'[#{user_id}] Starting of count_req()')
        question1 = "Какое место вы бы хотели посетить?"
        self.write_msg(user_id, question1)
        req = self.answer(user_id)
        logger.info(f'[#{user_id}] Got answer: "{req.text}"')

        # insert_db(req.user_id, req.text, 0)

        # Дозапись информации в файл с именем пользователя
        user_history_path = os.path.join(BOTS_CACHE_DIR, f"{user_id}.txt")
        with open(user_history_path, 'a') as f:
            f.write(req.text + '\n')

        self.req_repeat(user_id)
        # question2 = 'Хотели бы вы посетить еще что-то?'
        # req = self.msg(user_id, question2)
        # req = self.answer(user_id)
        # print('wrotenIF', req.text)
        # if req.text.lower() == 'нет':
        #     self.quant(user_id)
        # else:
        #     self.count_req(user_id)

    def start_vk_bot(self):
        """
        Первый метод бота, пишет первое сообщение

        Returns:

        """
        logger.debug(f'Starting of start_vk_bot(). Waiting for active user and messages ...')
        t = self.msg(
            0,
            "Это первый (или не очень первый) квантовый навигатор. \n"
            "Введите название станции, с которой вы начнете свое путешествие, "
            "и алгоритм построит вам кратчайший маршрут 5-ти достопримечательностям Москвы внутри кольцевой линии "
            "(и это с помощью квантового компьютера!)")

        with open(os.path.join(BOTS_CACHE_DIR, self.current_users_filename), 'a+') as f:
            users = f.read()
            use = users.split('\n')
            b = True
            for u in use:
                if u == t.user_id:
                    b = False
            if b:
                f.write(f"{t.user_id}\n")
                # os.system("vk_bot.py")  # FIXME question: зачем вызывать скрипт еще раз?

        t = self.answer(t.user_id)
        logger.info(f'[#{t.user_id}] Got answer: "{t.text}"')
        uid_filename = f"{t.user_id}.txt"
        uid_filepath = os.path.join(BOTS_CACHE_DIR, uid_filename)
        logger.debug(f'[#{t.user_id}] Creating new user\'s working file: "{uid_filename}". Start adding answers')
        with open(uid_filepath, 'w') as new_user_f:
            new_user_f.write(t.text + '\n')
        self.count_req(t.user_id)

        # insert_db(t.user_id, t.text, table)

