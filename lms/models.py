from django.db import models
from extentions import utils
class Term(models.Model):
    TERM_STATUS = (
        ('a', 'فعال'),
        ('d', 'غیرفعال')
    )
    name = models.CharField(max_length=64)
    begin_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=1, choices=TERM_STATUS, default='d')

    def __str__(self):
        return self.name

    def begin_date_jalali(self):
        return utils.to_jalali(self.begin_date)

    def end_date_jalali(self):
        return utils.to_jalali(self.end_date)

    def term_status(self):
        if self.status == 'a':
            return 'فعال'
        else:
            return 'غیرفعال'