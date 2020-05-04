import pyautogui

# Faster: Moves mouse pointer by 200 pixels
# SLOWER: Moves mouse pointer by 20 pixels
FASTER=200
SLOWER=20


class gui_control:
    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        pyautogui.size()

    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer UPWARDS from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------
    def mouse_up(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse up :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, -1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
            
    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer DOWNWARDS from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------        
    def mouse_down(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, 1*SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse down :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, 1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, 1*SLOWER, duration=0.25)

    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer LEFTWARD from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------ 
    def mouse_left(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse left :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(-1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)

    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer RIGHTWARD from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------ 
    def mouse_right(self,recognizer, src):
        #print("Move mouse right")
        pyautogui.moveRel(100, 0, duration=0.25)
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse right :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
    
    #------------------------------------------------------------------------------------
    # CLICKS the LEFT Mouse button it's current position 
    #------------------------------------------------------------------------------------    
    def left_click(self):
        pyautogui.click()
 
    #------------------------------------------------------------------------------------
    # CLICKS the RIGHT Mouse button it's current position 
    #------------------------------------------------------------------------------------  
    def right_click(self):
        print("Right Clicking")
        pyautogui.click(button='right', clicks=2, interval=0.25)
 
    #------------------------------------------------------------------------------------
    # DOUBLE CLICKS the LEFT Mouse button it's current position 
    #------------------------------------------------------------------------------------  
    def double_click(self):
        print("Double Clicking")
        pyautogui.click(button='left', clicks=2, interval=0.25)

    #------------------------------------------------------------------------------------
    # CLICKS the CHROME icon (if present in taskbar)
    # A screenshot needs to be captured and stored in 'screenshots' folder, before the 
    # program is run.
    #------------------------------------------------------------------------------------       
    def open_chrome(self):
        print("Opening Chrome")
        icon_location = pyautogui.locateOnScreen(r'screenshots\Chrome.PNG')
        #print(type(icon_location))
        if icon_location is not None:
            if len(icon_location) == 4:
                #Box(left=446, top=1023, width=74, height=52)
                #Calculate point x,y position to click based on above location
                #pyautogui.moveTo(icon_location.left, icon_location.top, duration=0.25)
                pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
        else:
            print("Could not locate Chrome Icon on screen")

    #------------------------------------------------------------------------------------
    # CLICKS the NOTEPAD icon (if present in taskbar)
    # A screenshot needs to be captured and stored in 'screenshots' folder, before the 
    # program is run.
    #------------------------------------------------------------------------------------           
    def open_notepad(self):
        print("Opening Notepad")
        icon_location = pyautogui.locateOnScreen(r'screenshots\Notepad.PNG')
        if icon_location is not None:
            if len(icon_location) == 4:
                #Box(left=446, top=1023, width=74, height=52)
                #Calculate point x,y position to click based on above location
                #pyautogui.moveTo(icon_location.left, icon_location.top, duration=0.25)
                pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
        else:
            print("Could not locate Notepad Icon on screen")
 

    #------------------------------------------------------------------------------------
    # Simulates the MUTE/UNMUTE key press
    #------------------------------------------------------------------------------------ 
    def mute_unmute(self):
        print("Pressing Mute/Unmute Key")
        pyautogui.typewrite(['volumemute'])
 
    #------------------------------------------------------------------------------------
    # Simulates the SPACE key press
    #------------------------------------------------------------------------------------ 
    def play_pause(self):
        print("Pressing SPACE Key")
        pyautogui.typewrite(['space'])

    #------------------------------------------------------------------------------------
    # Simulates the VOLUME UP key press
    #------------------------------------------------------------------------------------       
    def volume_up(self):
        pyautogui.typewrite(['volumeup'])
 
    #------------------------------------------------------------------------------------
    # Simulates the VOLUME DOWN key press
    #------------------------------------------------------------------------------------ 
    def volume_down(self):
        pyautogui.typewrite(['volumedown'])

