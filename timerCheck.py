import time, os, traceback

while True:
    check=os.path.abspath(r'checks\timerCheck.txt')
    timer=os.path.abspath(r'checks\timer.txt')

    with open(check, 'r') as file:
        status=file.read()

    if status=='active':
        with open(check, 'w') as file:
            file.write('stopped')
        time.sleep(2)
    else:
        with open(timer, 'w') as file:
            file.write('go')
        break
    
