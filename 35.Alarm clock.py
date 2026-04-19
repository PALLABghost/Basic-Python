import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm is set at {alarm_time}")
    music_file = "35. music for alarm clock.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("WAKE UP!!")
            pygame.mixer.init()
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()
            if pygame.mixer.music.get_busy():
                time.sleep(1)
            return False
        time.sleep(1)



if __name__ == "__main__":
    alarm_time = input("Set the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)