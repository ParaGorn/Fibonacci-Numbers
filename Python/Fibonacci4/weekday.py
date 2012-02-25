import datetime

now = datetime.datetime.now()

print ("Current date and time:", str(now))
print ("Current day:", now.strftime("%A"))
print ("Current year:", str(now.strftime("%Y %H:%M")))
