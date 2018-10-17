from django.db import models

Sunday = 'Sunday'
Monday = 'Monday'
Tuesday = 'Tuesday'
Wednesday = 'Wednesday'
Thursday = 'Thursday'
Friday = 'Friday'
Saturday = 'Saturday'

DAYS_OF_WEEK = (
    (Sunday, 'Sunday'),
    (Monday, 'Monday'),
    (Tuesday, 'Tuesday'),
    (Wednesday, 'Wednesday'),
    (Thursday, 'Thursday'),
    (Friday, 'Friday'),
    (Saturday, 'Saturday'),
)

Holiday = 'Holiday'
NotHoliday = 'NotHoliday'

STATUS = (
    (Holiday, 'Holiday'),
    (NotHoliday, 'NotHoliday'),
)


class Entry(models.Model):
    day = models.IntegerField(primary_key=True)
    date = models.DateField(null=False, blank=False)
    weekday = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    status = models.CharField(max_length=10, choices=STATUS)
    description = models.TextField()

    def __str__(self):
        return str(self.day)
