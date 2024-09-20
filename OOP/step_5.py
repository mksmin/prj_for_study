class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_date_string(cls, date_string: str):
        """
        Checks date strings and creates a new Date

        :param date_string: example: '2022-11-25'
        :return:
        """
        year, month, day = map(int, date_string.split('-'))
        date = cls(year=year, month=month, day=day)
        return date

    @staticmethod
    def is_date_string_valid(date_string: str):
        if date_string.count('-') != 2:
            return False
        year, month, day = map(int, date_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

    def copy(self):
        return Date(year=self.year, month=self.month, day=self.day)

    def __str__(self):
        return (f"{self.__class__.__name__}(year = {self.year}, "
                f"month = {self.month}, "
                f"day = {self.day})")


date1 = Date(2020, 11, 21)
print(date1)

date2 = date1

print(date2 is date1)

date2.year = 2019
date1.month = 5
print(date1)
print(date2)

date3 = date1.copy()
print(date1)
print(date3)
print(date1 is date3)

date1.day = 10
date3.month = 7
print(date1)
print(date3)

date4 = Date.from_date_string('2023-3-18')
print(date4)

print(Date.is_date_string_valid("2020-12-30-"))
print(Date.is_date_string_valid("2020-12-32"))
print(Date.is_date_string_valid("2020-12-31"))