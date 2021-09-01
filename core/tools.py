import time


# define the countdown func.
def countdown(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
