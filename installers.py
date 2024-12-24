import traceback, datetime, os, sys, subprocess as s
error=os.path.abspath(r'checks\errorLogs.txt')
try:
    s.call([sys.executable, '--version'])
except:
    print(r'Install python3 on your system: https://www.python.org/downloads/')
    input()
try:
    s.call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    s.call([sys.executable, '-m', 'pip', 'install', 'opencv-python-headless'])
    s.call([sys.executable, '-m', 'pip', 'install', 'pyfiglet'])
    s.call([sys.executable, '-m', 'pip', 'install', 'opencv-contrib-python'])
    s.call([sys.executable, '-m', 'pip', 'install', 'pywin32'])
    s.call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
    s.call([sys.executable, '-m', 'pip', 'install', 'MIME'])
    s.call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pillow'])
except:
    with open(error, 'a') as file:
        file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n')
    
