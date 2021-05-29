from Validation import Validation as v

turtle={0:'name: ',1:'salary: ',2:'firstday: ',3:'lastday: '}

class Employee:
    def __init__(self, name, salary, firstday, lastday):
        for i in range(len(turtle)):
            setattr(self, turtle[i], None)
        self.__name= v.validName(name)
        self.__salary= v.validFloat(salary)
        self.__firstday= v.validDate(firstday)
        self.__lastday= v.validDate(lastday)
    
    def __str__(self):
        res=' '
        for i in range(len(turtle)):
            res += turtle[i] + str(getattr(self, turtle[i]))+'\n'
        return res

    def get_name(self):
        return self.__name
    def get_salary(self): 
        return self.__salary
    def get_firstday(self): 
        return self.__firstday
    def get_lastday(self): 
        return self.__lastday

    def getAttr(self):
        return [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
    def getGettr(self):
        return [a for a in dir(self) if a.startswith('get') and callable(getattr(self, a))]

    def set_name(self, val):
        self.__name = val

    def set_salary(self, val):
        self.__salary = val

    def set_firstday(self, val):
        self.__firstday = val
    
    def set_lastday(self, val):
        self.__lastday = val
    