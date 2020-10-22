from Meeting import *
from datetime import date, time
from Validation import Validation as v

class MeetingColection:

    def __init__(self):
        self.__coll = []
    
    def __str__(self):
        strcoll = ''
        for i in self.__coll:
            strcoll += str(i) + '\n'
        return strcoll
    
    def __len__(self):
        return len(self.__coll)

    def find(self, key):
        key = str(key)
        res = MeetingColection()
        
        for i in self.__coll:
            for a in i.getGetters():
                if str(getattr(i, a)()).find(key) != -1:
                    res.add(i)

        return res if len(res) != 1 else res._MeetingColection__coll[0]

    def sort(self, atr):
        lst = self.__coll
        try:
            if isinstance(getattr(lst[0], _atr)(), str):
                lst.sort(key=lambda p: getattr(p, _atr)().lower())
            else:
                lst.sort(key=lambda p: getattr(p, _atr)())
        except AttributeError: 
            raise AttributeError('Object has no atribut')