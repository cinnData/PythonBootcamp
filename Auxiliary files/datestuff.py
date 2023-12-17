month_list = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December']

def convert(date):
    year = date[:4]
    month_no = int(date[5:7])
    month = month_list[month_no - 1]
    day = str(int(date[8:]))
    return month + ' ' + day + ', ' + year