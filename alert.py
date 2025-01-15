import traceback, datetime, os, sys
import msops as m
def sendAlert(window):
   import time, subprocess as s
   name=os.path.basename(sys.argv[0])
   if name.endswith('.py'):
      timer=os.path.abspath('timer.py')
   else:
      timer=os.path.abspath('timer.exe')
   check=os.path.abspath(r'checks\timer.txt')
   sS=os.path.abspath(r'screenShot\screenShot.png')
   image=os.path.abspath(r'screenShot\screenShot.png')
   message=f'''\
Motion Detected at {datetime.datetime.now().strftime('%H:%M:%S')}.

<do not respond to this email>'''
   with open(check, 'r') as file:
      status=file.read()

   if status=='go':
      m.takeSS(window, sS)
      m.sendEmail(message, image)
      s.run(['start', timer], shell=True)
      with open(check, 'w') as file:
         file.write('stop')

#sendAlert('motionSensor')
