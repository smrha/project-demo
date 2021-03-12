from . import jalali

def to_jalali(date):
    # list of jalali months
    months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", " دی", " بهمن", " اسفند", ]

    # convert georgian date to string and convert that string to jalali as tuple
    date_to_string = f"{date.year},{date.month},{date.day}"
    date_to_tuple = jalali.Gregorian(date_to_string).persian_tuple()
    
    # format jalali date
    output = f"{date_to_tuple[2]} {months[date_to_tuple[1]-1]} {date_to_tuple[0]}"
    return output