import webbrowser as web
import pyautogui as gui
import time
import datetime
# import os
def msg_sender(cntname, message):
    sel_contact(cntname)
    gui.click(767, 816)
    message=  message + '\n Automate BOT by SamX'
    gui.typewrite(message)  # message
    gui.click(1466, 815)

def datetimechck(gdatetime):
    _time = False
    while _time != True:
        currentTime = datetime.datetime.now()
        currentTime = currentTime.strftime("%d/%m %I:%M %p")
        if currentTime == gdatetime:
            _time = True
            return _time
        elif gdatetime < currentTime  :
            gui.alert(text='you enter wrong date and time', title='Wrong date and time', button='OK')
            return _time
        else:
            time.sleep(30)

def file_sender(cntname,file,file_path):
    sel_contact(cntname)
    #click on attach
    gui.click(604,813)
    gui.sleep(1)
    #click on Doc
    gui.click(590,596)
    gui.sleep(1.5)
    #click on file_path
    gui.click(629,165)
    gui.hotkey('ctrl','a')
    gui.sleep(.2)
    gui.typewrite(file_path)
    gui.hotkey('enter')
    time.sleep(.2)
    #click on file_name
    gui.click(724,580)    
    gui.typewrite(file)
    gui.click(1104, 665)
    #click on send
    time.sleep(.75)
    gui.click(1421,713)

def sel_contact(cntname):
    web.open("https://web.whatsapp.com/")
    time.sleep(10) #temp change bcz slow network
    # # for searching contact
    gui.click(253, 239)
    # # type contact name
    gui.typewrite(cntname)
    # click on contact
    gui.hotkey('enter')
    gui.sleep(1.5)
    
def main():
    cntname = gui.prompt('Enter contact name or number')  # or number
    selection=gui.confirm(text='', title='What Do you want?', buttons=['Sent Text', 'Send File'])
    if selection=='Sent Text':
        message = gui.prompt('Enter the massage')  # Enter Message
        gdatetime = gui.prompt('Enter the date and time in d/m H:M p')
        if datetimechck(gdatetime): # checking Date and time
            msg_sender(cntname, message)
    elif selection == 'Send File':
            file = gui.prompt('Enter the file name')
            file_path = gui.prompt('Enter the file path')
            file_sender(cntname,file,file_path)

if __name__ == "__main__":
    main()
    # time.sleep(5)
    # os.system("pkill -KILL -u samx") # for logut samx user