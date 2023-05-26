from datetime import datetime
from pytz import timezone

# Ano, mês e dia
data = datetime(2023, 4, 23)
# print(data)

# Ano, mês, dia, hora, minuto, segundo, microsegundo
data = datetime(2023,4, 23, 14, 9)
# print(data)

# strptime
data_str = '2023-4-23 14:12:30'
data_fmt = '%Y-%m-%d %H:%M:%S'
data = datetime.strptime(data_str, data_fmt)
# print(data)

agora = datetime.now()
print(agora)
print(agora.timestamp())
print(agora.fromtimestamp(1682380788.819833))

# Com timezone:
agora = datetime.now(timezone('Asia/Tokyo'))
print(agora)