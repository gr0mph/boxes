#!/usr/bin/python
# -*- encoding: utf-8 -*-

import socket
import time
import sys

from threading import RLock

from Model.Data import Data
from Model.Input import Input
from Model.Output import Output

class Main:

    def __init__(self, writeR_readM_lock,writeM_readS_lock):
        self.writeR_readM_lock = writeR_readM_lock
        self.writeM_readS_lock = writeM_readS_lock

        data = Data()
        data.data["input"] = Input()
        self.input = data.data["input"]
        data.data["output"] = Output()
        self.output = data.data["output"]

        print("[OK] Main started")
        self.main()

    def main(self):
        index_input = 0
        index_output = 0
        while index_input < 100 and index_output < 100:
            with self.writeR_readM_lock:
                index_input = index_input + 1
                self.input.nombre = self.input.nombre - 1
                print("Main Input Nombre " + str(self.input.nombre))
            with self.writeM_readS_lock:
                index_output = index_output + 1
                self.output.nombre = self.output.nombre + 1
                print("Main Output Nombre " + str(self.output.nombre))
