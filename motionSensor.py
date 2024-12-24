import traceback, datetime, os
error=os.path.abspath(r'checks\errorLogs.txt')
try:
    import cv2, ctypes, sys, time, subprocess as s, pyfiglet as pF

    if __name__=='__main__':
        name=os.path.basename(__file__)
        banner=pF.figlet_format('Initializing...', font='slant')
        print(banner)
        if name.endswith('.py'):
            sendAlert=os.path.abspath('alert.py')
        else:
            sendAlert=os.path.abspath('alert.exe')
        timer=os.path.abspath(r'checks\timer.txt')   

        with open(timer, 'w') as file:
            file.write('go')
        
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, ''.join(sys.argv), None, 1)
        else:
            video=cv2.VideoCapture(0)
            capFrames=[None, None]
            frameDiff=None
            ogFrameDiff=None

            for i in range(50):
                print()
            
            ret, frame1=video.read()
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

                cont,_=cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for cur in cont:
                    if cv2.contourArea(cur)<1000:
                        continue
                    (x, y, w, h)=cv2.boundingRect(cur)
                    cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

                cv2.imshow('Video Feed', frame2.copy())
                    
                if cv2.countNonZero(thresh)>500:
                    with open(timer, 'r') as file:
                        timeCheck=file.read()
                    if timeCheck=='go':
                        s.run(['start', sendAlert], shell=True)
                        print(f'Motion Detected: {datetime.datetime.now().strftime("%H:%M:%S")}')
                        time.sleep(.5)
                   
                if cv2.waitKey(1)&0xFF==ord('q'):
                    break

                time.sleep(0.05)
                
            video.release()
            cv2.destroyAllWindows()
except:
    with open(error, 'a') as file:
        file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n')

