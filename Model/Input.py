#!/usr/bin/python
# -*- encoding: utf-8 -*-

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Input:

    def __init__(self):
        self.nombre = 0

    def print_(self):
        print(str(self.nombre))
