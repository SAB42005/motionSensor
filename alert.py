import traceback, datetime, os
error=os.path.abspath(r'checks\errorLogs.txt')
try:
    import smtplib, ssl, time, subprocess as s

    check=os.path.abspath(r'checks\timer.txt')
    with open(check, 'w') as file:
        file.write('stop')
        
    delay=os.path.abspath('delay.txt')
    with open(delay, 'r') as file:
        delay=file.read()
        delay=delay.rstrip(' ')
        
    delay=int(delay)

    sendEmail=os.path.abspath('sendEmail.py')
    takeSS=os.path.abspath('takeScreenShot.py')
    
    s.run(['pythonw', takeSS], shell=True)
    time.sleep(1)
    s.run(['pythonw', sendEmail], shell=True)

    timer=0

    while True:
        if timer==delay-1:
            break
        timer+=1
        print(timer)
        time.sleep(1)

    with open(check, 'w') as file:
        file.write('go')
except:
    with open(error, 'a') as file:
        file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n\n')



