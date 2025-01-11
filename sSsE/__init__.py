import traceback, datetime, os, pyautogui, pygetwindow, win32gui, win32con, sys
import subprocess as s, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def takeSS(capWindow, path):
    import pyautogui, pygetwindow, time, win32gui, win32con, sys, subprocess as s
    windowTitle=capWindow
    window=pygetwindow.getWindowsWithTitle(windowTitle)[0]
    hwnd=win32gui.FindWindow(None, windowTitle)
    if hwnd==0:
        hwnd=None
        def windowEnumHandler(handle, context):
            if windowTitle in win32gui.GetWindowText(handle):
                global hwnd
                hwnd=handle
                return False
            return True
        win32gui.EnumWindows(windowEnumHandler, None)

    while True:
        try:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(hwnd)
            break
        except:
            pass
    time.sleep(.25)
    
    left=window.left
    top=window.top
    width=window.width
    height=window.height

    sS=pyautogui.screenshot(region=(left, top, width, height))
    
    try:
        sS.save(path)
    except:
        folder=os.path.abspath(sys.argv[0])
        folder=folder.rstrip('alert.py')
        folder=folder.rstrip('motionSensor.py')
        folder=folder.rstrip('motionSensor.exe')
        print(folder)
        s.run(['mkdir', folder+'screenShot'], shell=True)
        sS.save(path)
        
def sendEmail(message, image):
    emails=os.path.abspath('receivers.txt') 
    port=465
    password=''
    sender='motionSensor798@gmail.com'
    receivers=[]
    context=ssl.create_default_context()
    msg=MIMEMultipart()
    msg.attach(MIMEText(message, 'plain'))

    try:
        with open(image, 'rb') as img:
            mimeImage=MIMEImage(img.read(), name=os.path.basename(image))
            msg.attach(mimeImage)
    except:
        pass

    with open(emails, 'r') as file:
        for line in file:
            line=line.rstrip(' ')
            receivers.append(line)

    if len(receivers)==0:
        receivers=int('No emails listed in receivers.txt')

    for i in range(len(receivers)):
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login('motionSensor798@gmail.com', password)
            server.sendmail(sender, receivers[i], msg.as_string())
