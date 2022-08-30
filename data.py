import datetime

d = datetime.date(2001, 9, 11)
tday = datetime.date.today()
print(tday, d)
print(tday - d)

tdelta = datetime.timedelta(hours=12)
print(tday + tdelta)

bday = datetime.date(2022, 10, 3)
till_bday = bday - tday
print(till_bday.days)

dt_agora = datetime.datetime.now()
print(dt_agora.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)