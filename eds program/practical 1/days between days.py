from datetime import datetime
date1_str = input()
date2_str = input()
date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")
difference = date2 - date1
print(difference.days)