import traceback, datetime, os, pyautogui, pygetwindow, win32gui, win32con, sys
import subprocess as s, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
error=os.path.abspath(r'checks\errorLogs.txt')

def takeSS(capWindow):
    try:
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

        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(.25)
        
        left=window.left
        top=window.top
        width=window.width
        height=window.height

        sS=pyautogui.screenshot(region=(left, top, width, height))
        sS.save(r'screenShot\screenShot.png')

        sendEmail()
    except:
        with open(error, 'a') as file:
            file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n')

def sendEmail():
    try:
        image=os.path.abspath(r'screenShot\screenShot.png')
        emails=os.path.abspath('receivers.txt') 
        port=465
        password=''
        sender='motionSensor798@gmail.com'
        receivers=[]
        context=ssl.create_default_context()
        message=f'''\
    Motion Detected at {datetime.datetime.now().strftime('%H:%M:%S')}.

    <do not respond to this email>'''
        msg=MIMEMultipart()
        msg.attach(MIMEText(message, 'plain'))

        with open(image, 'rb') as img:
            mimeImage=MIMEImage(img.read(), name=os.path.basename(image))
            msg.attach(mimeImage)

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
    except:
        with open(error, 'a') as file:
            file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n')
