import time, traceback, datetime, os, pyfiglet as pF
error=os.path.abspath(r'checks\errorLogs.txt')
try:
    import pyfiglet as pF, pygetwindow, win32gui, win32con, subprocess as s, sys
    import msops as m
    timer=0
    delay=os.path.abspath('delay.txt')
    check=os.path.abspath(r'checks\timer.txt')
    windowTitle='Video Feed'
    window=pygetwindow.getWindowsWithTitle(windowTitle)[0]
    name=os.path.abspath(sys.argv[0])
    timerCheckTxt=os.path.abspath(r'checks\timerCheck.txt')

    if name.endswith('.py'):
        timerCheck=os.path.abspath('timerCheck.py')
    else:
        timerCheck=os.path.abspath('timerCheck.exe')
        
    with open(delay, 'r') as file:
        delay=file.read()
    with open(timerCheckTxt, 'w') as file:
        file.write('active')

    m.bringToFront(windowTitle)

    s.run(['start', '/min', timerCheck], shell=True)

    while True:
        if timer==int(delay)-1:
            with open(check, 'w') as file:
                file.write('go')
            break
        print('\n'*50)
        timer=int(timer)+1
        number=pF.figlet_format(str(timer))
        print(number)
        time.sleep(1)

        with open(timerCheckTxt, 'w') as file:
            file.write('active')

except:
    with open(error, 'a') as file:
        file.write(f'An error occured in timer on {datetime.datetime.now()}:\n{traceback.format_exc()}\n')
