from datetime import datetime, timedelta

data_fmt = '%Y-%m-%d %H:%M:%S'

date_start = datetime.strptime('2023-4-23 14:12:30', data_fmt)
date_end = datetime.strptime('1993-10-13 00:00:00', data_fmt)

delta = date_end - date_start

print(delta)
print(delta.days)
print(delta.seconds)
print(delta.total_seconds())

td = timedelta(days=10, hours=2)
print(date_start + td)