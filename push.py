from win10toast import ToastNotifier
import time

while True:
    curr_time = time.strftime("%H:%M:%S")
    if curr_time == "03:12:40":
        print(curr_time)
        break
    else:
        pass

hr = ToastNotifier()

hr.show_toast("alarm", "sdfgh")