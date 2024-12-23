import traceback, datetime, os
error=os.path.abspath(r'checks\errorLogs.txt')
try:
    import pyautogui, pygetwindow, time, win32gui, win32con

    windowTitle='Video Feed'
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
except:
    with open(error, 'a') as file:
        file.write(f'Error occured on {datetime.datetime.now()}:\n{traceback.format_exc()}\n\n')
