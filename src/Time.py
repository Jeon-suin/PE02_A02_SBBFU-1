import datetime

def time():
    now = datetime.datetime.now()
    num = now.strftime('%Y%m%d-%H%M%S')
    version = str(num)
    return version

