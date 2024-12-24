import traceback, datetime, os
error=os.path.abspath(r'checks\errorLogs.txt')
try:
    import smtplib, ssl, time, subprocess as s
    name=os.path.basename(__file__)
    check=os.path.abspath(r'checks\timer.txt')
    with open(check, 'w') as file:
        file.write('stop')
        
    delay=os.path.abspath('delay.txt')
    with open(delay, 'r') as file:
        delay=file.read()
        delay=delay.rstrip(' ')
        
    delay=int(delay)

    if name.endswith('.py'):
        sendEmail=os.path.abspath('sendEmail.py')
        takeSS=os.path.abspath('takeScreenShot.py')
    else:
        sendEmail=os.path.abspath('sendEmail.exe')
        takeSS=os.path.abspath('takeScreenShot.exe')

    s.run(['start', takeSS], shell=True)
    time.sleep(2)
    s.run(['start', sendEmail], shell=True)

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
        file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n')



