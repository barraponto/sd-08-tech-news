from datetime import datetime
date = '23-11-2020'
format = "%Y-%m-%d"
format_data = datetime.strptime(date, format)
print(format_data)
