from Validation import Validation as v

turtle={0:'ID: ',1:'date: ',2:'start_time: ',3:'end_time: ',4:'meeting_url: ',5:'owner: ',6:'participant: '}

class Meeting:
    def __init__(self, ID, date, start_time, end_time, meeting_url, owner, participant):
        self.__ID = v.validID(ID)
        self.__date = v.validDate(date)
        self.__start_time = v.validTime(start_time)
        self.__end_time = v.validTime(end_time)
        self.__meeting_url = v.validURL(meeting_url)
        self.__owner = v.validName(owner)
        self.__participant = v.validName(participant)
    
    def __str__(self):
        res=''
        for i in range(len(turtle)):
            res += turtle[i] + str(getattr(self, turtle[i]))+'\n'
        return res
    
    #all getters
    def get_ID(self):
        return self.__ID
    def get_date(self): 
        return self.__date
    def get_start_time(self): 
        return self.__start_time
    def get_end_time(self): 
        return self.__end_time
    def get_meeting_url(self): 
        return self.__meeting_url
    def get_owner(self):
        return self.__owner
    def get_participant(self): 
        return self.__participant

    def getAttributes(self):
        return [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
    def getGetters(self):
        return [a for a in dir(self) if a.startswith('get') and callable(getattr(self, a))]

    #all setters
    def set_date(self, val):
        val = v.validDate(val)
        self.__date = val
    def set_start_time(self, val):
        val = v.validTime(val)
        self.__start_time = val
    def set_end_time(self, val):
        val = v.validTime(val)
        self.__end_time = val
    def set_meeting_url(self, val):
        val = v.validURL(val)
        self.__meeting_url = val
    def set_owner(self, val):
        val = v.validName(val)
        self.__owner = val
    def set_participant(self, val):
        val = v.validName(val)
        self.__participant = val