import re
from urllib.parse import urlparse
from datetime import date, time

class Validation:
    def __init__(self): 
        pass

    @staticmethod
    def validInt(check):
        try:
            check = int(check)
        except ValueError:
            raise ValueError('ID incorect')
        return check

    @staticmethod
    def validStr(val):
        if isinstance(val, str):
            return val
        else:
            raise ValueError('Incorrect string')

    @staticmethod
    def validID(id_check):
        if id_check!=None:
            id_check= Validation.validInt(id_check)
        try:
            len(id_check)==8
        except ValueError:
            raise ValueError('ID checking incorrect')
        return id_check

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
    def validTime(val):
        try:
            if isinstance(val, str):
                [hh, mm] = val.split('-')
                val = time(int(hh), int(mm))
        except ValueError:
            raise ValueError('incorrect time')
        return val

    @staticmethod
    def validName(val):
        if re.search(r'[^a-zA-Z ]+', val) is not None: 
            raise ValueError('incorrect name')
        
        return val   

    @staticmethod
    def validURL(val):
        try:
            result = urlparse(val)
            if all([result.scheme, result.netloc, result.path])==True:
                return val
        except:
            return print('incorrect URL adress')
            
        # val = Validation.validStr(val)
        # regexSrch = re.search(r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', val)
        # if regexSrch is None: 
        #     raise ValueError('Bad URL for ')
        
        # return val 

    @staticmethod
    def validFile(val):
        if not isinstance(val):
            raise ValueError('problem with file')

        return val


    @staticmethod
    def validateMeeting(val):
        Validation.validID(val.get_ID())
        Validation.validDate(val.get_date())
        Validation.validTime(val.get_start_time())
        Validation.validTime(val.get_end_time())
        Validation.validURL(val.get_meeting_url())
        Validation.validStr(val.get_owner())
        Validation.validStr(val.get_participant())
        return val