class Time:
    def __init__(self, init_hr = 12, init_min = 0, init_ampm = "AM"):
        if init_hr < 1 or init_hr > 12:
            raise Exception("Error: Invalid hour for Time object")
        if init_min < 0 or init_min > 59:
            raise Exception("Error: Invalid minute for Time object")
        init_ampm = init_ampm.upper()
        if init_ampm != "AM" and init_ampm != "PM":
            raise Exception("Error: Invalid am/pm flag for Time object")

        self.hr = init_hr
        self.min = init_min
        self.ampm = init_ampm

    def hour(self):
        return self.hr

    def minute(self):
        return self.min
        
    def am_pm(self):
        return self.ampm

    def total_minutes(self):
        if self.am_pm()== 'AM':
            if self.hr != 12:
                totalmin= self.hr * 60 + self.min
            else:
                totalmin = self.min
        else:
            if self.hr == 12:
                totalmin = (self.hr +12)* 60 + self.min
            else:
                totalmin = (self.hr + 12)* 60 + self.min
        return totalmin

    def __str__(self):
        if self.min <10:
            minutes = '0' + str(self.min)
        else:
            minutes = str(self.min)
        hour = str(self.hr)
        return hour + ':' + minutes + self.ampm

    def __repr__(self):
        if self.min <10:
            minutes = '0' + str(self.min)
        else:
            minutes = str(self.min)
        hour = str(self.hr)
        return hour + ':' + minutes + self.ampm
