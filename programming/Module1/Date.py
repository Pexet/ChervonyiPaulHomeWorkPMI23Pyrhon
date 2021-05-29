


class Date:
    def __init__(self, year, mounth, day):
        self.set_year(year)
        self.set_mounth(mounth)
        self.set_day(day)

    def set_year(self, year):
        self.year = year

    def set_mounth(self, mounth):
        self.mounth = mounth
    
    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year
    
    def get_mounth(self):
        return self.mounth

    def get_day(self):
        return self.day