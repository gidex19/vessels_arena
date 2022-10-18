# import datetime
# from .models import Devotional

# # d = datetime.datetime.now()
# # day =  datetime.date.strftime(d, "%d")
# # month = datetime.date.strftime(d, "%B")
# # year = datetime.date.strftime(d, "%Y")
# # print(day)
# # print(month)
# # print(year)

# d = Devotional.objects.filter(id=6).first()
# print(d.date)