#multithreading = used to perform multiple task concurrently(multi tasking)
        #good for I/O bound task like reading file or fetching data from api threading
import threading
import time

def walking_dog(first, last):
    time.sleep(8)
    print(f"You finished walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print(f"you take out the trash")

def get_mail():
    time.sleep(5)
    print("you get the mail")

chore1 = threading.Thread(target=walking_dog,args=("scooby","doo"))   # if some function is taking parameter then
chore1.start()                                                #we need to add tuple by args and add the (,)
                                                                    #if one argument pass
chore2 = threading.Thread(target=take_out_trash())
chore2.start()
chore3 = threading.Thread(target=get_mail())
chore3.start()

chore1.join()       #wait until this thready completed then show print statement
chore2.join()
chore3.join()

print("all the completed")