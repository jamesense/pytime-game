import time

time_epoch = time.gmtime()

print("The second is:", time_epoch.tm_sec)

if time_epoch.tm_sec == 15:
    print("You lucky duck")
else:
    print("Better luck next time")