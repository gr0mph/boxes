#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
from threading import Thread, RLock

from Sender import Sender
from Receiver import Receiver
from Main import Main

writeR_readM_lock = RLock()
writeM_readS_lock = RLock()

class Boxes(Thread):

    """
    |-----------------------------------------------------------------|
    |  Boxes                                                          |
    |       |----------|        |----------|        |----------|      |
    |       | Receiver |        |   Main   |        |  Sender  |      |
    |       |----------|        |----------|        |----------|      |
    |                                                                 |
    |-----------------------------------------------------------------|
    """

    def __init__(self, f_from_thread):
        Thread.__init__(self)
        self.f_from_thread = f_from_thread


    def run(self):
        if self.f_from_thread.__name__ == "Receiver":
            return self.f_from_thread(writeR_readM_lock)
        if self.f_from_thread.__name__ == "Main":
            return self.f_from_thread(writeR_readM_lock,writeM_readS_lock)
        if self.f_from_thread.__name__ == "Sender":
            return self.f_from_thread(writeM_readS_lock)

# Thread creation
thread_receiver = Boxes(Receiver)
thread_sender = Boxes(Sender)
thread_main = Boxes(Main)

# Thread started
thread_receiver.start()
thread_sender.start()
thread_main.start()

# On thread stopping, join finish
thread_receiver.join()
thread_sender.join()
thread_main.join()
