import traceback, datetime, os, sys
error=os.path.abspath(r'checks\errorLogs.txt')

def sendAlert():
    try:
        import time, subprocess as s, sSsE as SE

        name=os.path.basename(sys.argv[0])
        if name.endswith('.py'):
            timer=os.path.abspath('timer.py')
        else:
            timer=os.path.abspath('timer.exe')
        check=os.path.abspath(r'checks\timer.txt')
        with open(check, 'r') as file:
            status=file.read()

        if status=='go':
            SE.takeSS('Video Feed')
            s.run(['start', timer], shell=True)
            with open(check, 'w') as file:
                file.write('stop')
               
    except:
        with open(error, 'a') as file:
            file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n')

sendAlert()

