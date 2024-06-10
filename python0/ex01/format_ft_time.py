import time
from datetime import date

curr = round(time.time(), 4)

# https://www.scaler.com/topics/python-scientific-notation/
sc_notation = "{:.2e}".format(curr)

print("Seconds since January 1, 1970:",
      f'{curr:,}', "or", sc_notation, "in scientific notation", )

# https://www.programiz.com/python-programming/datetime/current-datetime

today_date = date.today().strftime("%b %d %Y")

print(today_date)
