#!/usr/bin/python
# -*- encoding: utf-8 -*-

from threading import RLock

from Model.Data import Data
from Model.Input import Input

class Receiver:

    def __init__(self, writeR_readM_lock):
        self.writeR_readM_lock = writeR_readM_lock

        data = Data()
        data.data["input"] = Input()
        self.input = data.data["input"]

        print("[OK] Receiver started")
        self.read()

    def read(self):
        i = 0
        while i < 100:
            with self.writeR_readM_lock:
                i = i + 1
                self.input.nombre = self.input.nombre + 1
                print("Receiver Nombre " + str(self.input.nombre))
