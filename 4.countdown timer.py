import time

my_time =  int(input("Enter the time in sec: "))

for x in range(my_time, 0, -1): #reversed(range(0, my_time +1)):
    seconds = x % 60    # 5% 60 will give 5 reminder.so less than 60 cal calculate as second
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's UP! Boom")