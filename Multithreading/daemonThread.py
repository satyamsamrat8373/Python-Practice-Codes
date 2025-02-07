import threading
import time
def background_task():
    print(threading.current_thread())
    while True:
        print("Background task running...")
        time.sleep(1)

thread = threading.Thread(target = background_task,name = "Daemon")
thread.daemon = True
thread.start()

time.sleep(1.75)
print("Main Thread is dead.")