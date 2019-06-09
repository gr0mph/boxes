#!/usr/bin/python
# -*- encoding: utf-8 -*-

from threading import RLock

from Model.Data import Data
from Model.Output import Output

class Sender:

    def __init__(self, writeM_readS_lock):
        self.writeM_readS_lock = writeM_readS_lock

        data = Data()
        data.data["output"] = Output()
        self.output = data.data["output"]

        print("[OK] Sender started")
        self.write()

    def write(self):
        i = 0
        while i < 100:
            with self.writeM_readS_lock:
                i = i + 1
                self.output.nombre = self.output.nombre - 1
                print("Sender Nombre " + str(self.output.nombre))
