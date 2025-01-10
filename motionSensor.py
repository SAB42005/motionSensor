import traceback, datetime, os, atexit
error=os.path.abspath(r'checks\errorLogs.txt')
try:
    import cv2, ctypes, sys, time, subprocess as s, pyfiglet as pF, sys, alert
    import sSsE as SE
    
    if __name__=='__main__':  
        if not ctypes.windll.shell32.IsUserAnAdmin():
            banner=pF.figlet_format('Grabbing Permissions...', font='slant')
            print(banner)
            ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable,
                                                ''.join(sys.argv), None, 1)
        else:
            name=os.path.abspath(sys.argv[0])
            banner=pF.figlet_format('Initializing...', font='slant')
            print(banner)
            print('connecting to camera...')

            video=cv2.VideoCapture(0)
            capFrames=[None, None]
            frameDiff=None
            ogFrameDiff=None
            videoBuffer=0
            
            check=os.path.abspath(r'checks\timer.txt')
            
            with open(check, 'w') as file:
                file.write('go')

            ret, frame1=video.read()
            
            print('\n'*50)

            while True:
                ret, frame2=video.read()
                cv2.imshow('Video Feed', frame2)
                frameDiff=cv2.absdiff(frame1, frame2)

                grayFrame=cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
                grayDiff=cv2.cvtColor(frameDiff, cv2.COLOR_BGR2GRAY)
                grayDiff=cv2.GaussianBlur(grayDiff, (3, 3), 0)
                frame1=frame2.copy()
                
                _,thresh=cv2.threshold(grayDiff, 25, 255, cv2.THRESH_BINARY)
                thresh=cv2.dilate(thresh, None, iterations=2)

                cont,_=cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
                for cur in cont:
                    if cv2.contourArea(cur)<500:
                        continue
                    (x, y, w, h)=cv2.boundingRect(cur)
                    cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    time.sleep(0.05)

                cv2.imshow('Video Feed', frame2.copy())
                    
                if cv2.countNonZero(thresh)>500:
                    with open(check, 'r') as file:
                        status=file.read()
                    if videoBuffer!=0:
                        if status=='go':
                            alert.sendAlert('Video Feed')
                            print(f'Motion Detected: {datetime.datetime.now().strftime("%H:%M:%S")}')
                    else:
                        videoBuffer+=1
                        time.sleep(2)
                        
                if cv2.waitKey(1)&0xFF==ord('q'):
                    break
    
            video.release()
            cv2.destroyAllWindows()
except:
    with open(error, 'a') as file:
        file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n')
    SE.sendEmail(f'Motion sensor error. Check errorLogs.txt for more information: {datetime.datetime.now().strftime("%H:%M:%S")}', None)
    exit(1)
    
