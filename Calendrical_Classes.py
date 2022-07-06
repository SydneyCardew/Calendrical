class Year:

    def __init__(self, year):
        self.year = year
        self.week_days = ("Fr", "Sa", "Su", "Mo", "Tu", "We", "Th")
        self.month_ids = {
            'January': 31,
            'February': (28, 29),
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31
        }
        self.year_calculation(self.year)

    def year_calculation(self, year):
        leap_years_since_1582 = (i for i in range(1583, self.year) if i % 4 == 0 and i % 100 != 0 or i % 400 == 0)
        days_to_year_start = ((year - 1582) * 365) + len(list(leap_years_since_1582)) + 78
        self.jan_one_day = (days_to_year_start % 7) - 1
        self.leap_year = True if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0 else False
        year_days = 366 if self.leap_year else 365
        self.year_dict = {}
        day_index = self.jan_one_day
        week = 1
        for x in range(1, year_days + 1):
            self.year_dict[x] = (day_index, week)
            day_index += 1
            if day_index == 7:
                day_index = 0
                week += 1
        self.months = [Month(None, None, None, None, None)]
        year_counter = 1
        for month, length in self.month_ids.items():
            current_length = length if isinstance(length, int) else (length[1] if self.leap_year else length[0])
            self.months.append(Month(self.year_dict[year_counter][0], current_length, month,
                                     self.year_dict[year_counter][1], self.week_days))
            year_counter += current_length


class Month:

    def __init__(self, start, length, name, start_week, week_days):
        self.array_offsets = {0: 4, 1: 5, 2: 6, 3: 0, 4: 1, 5: 2, 6: 3}
        self.start = start
        self.length = length
        self.name = name
        self.start_week = start_week
        self.week_days = week_days
        self.calendar_array = []
        self.start_week = start_week
        if self.start is not None:
            self.make_month()
            self.get_calendar_array()

    def make_month(self):
        self.days = {}
        day_index = self.start
        for x in range(1, self.length + 1):
            self.days[x] = self.week_days[day_index]
            day_index += 1
            if day_index >= 7:
                day_index = 0

    def get_calendar_array(self):
        week = self.start_week
        try:
            offset = self.array_offsets[self.start]
        except KeyError:
            offset = self.array_offsets[0]
        calendar_array = [week]
        calendar_array.extend([''] * offset)
        accumulator = offset
        for index, day in enumerate(self.days.items(), start=1):
            if accumulator == 7:
                week += 1
                calendar_array.append(week)
                accumulator = 0
            calendar_array.append(day[0])
            accumulator += 1
        self.calendar_array.extend(calendar_array)
        try:
            if self.calendar_array[-1] < 20:
                del self.calendar_array[-1]
        except TypeError:
            pass
        while len(self.calendar_array) < 48:
            self.calendar_array.append('')

    def view(self):
        return f"{self.name} {self.length} {self.calendar_array} {len(self.calendar_array)}"

    def __repr__(self):
        return self.view()

    def __str__(self):
        return self.view()









