import re
from datetime import date

class Validation:
    def __init__(self): 
        pass

    @staticmethod
    def validFloat(val):
        try:
            val = round(float(val), 2)
        except ValueError: 
            raise ValueError('incorrect float')
        
        return val        

    @staticmethod
    def validDate(val):
        try:
            if isinstance(val, str):
                [yyyy, mm, dd] = val.split('-')
                val = date(int(yyyy), int(mm), int(dd))      
        except ValueError:
            raise ValueError('incorrect date')
        return val

    @staticmethod
    def validName(val):
        if re.search(r'[^a-zA-Z ]+', val) is not None: 
            raise ValueError('incorrect name')
        
        return val   


    @staticmethod
    def validFile(val):
        if not isinstance(val):
            raise ValueError('problem with file.')

        return val

