import traceback, datetime, os
error=os.path.abspath(r'checks\errorLogs.txt')
try:
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage

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
        receivers+=1

    for i in range(len(receivers)):
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login('motionSensor798@gmail.com', password)
            server.sendmail(sender, receivers[i], msg.as_string())
except:
    with open(error, 'a') as file:
        file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n')
