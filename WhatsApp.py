import webbrowser as web
import pyautogui as gui
import time
import datetime
# import os
def msg_sender(cntname, message):
    sel_contact(cntname)
    gui.click(767, 816) #(X,Y)
    message=  message + '\n Automate BOT by MuhammadUsamaMX'
    gui.typewrite(message)  # message
    gui.click(1466, 815) #(X,Y)

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
    gui.click(604,813)#(X,Y)
    gui.sleep(1)
    #click on Doc
    gui.click(590,596)#(X,Y)
    gui.sleep(1.5)
    #click on file_path
    gui.click(629,165)#(X,Y)
    gui.hotkey('ctrl','a')
    gui.sleep(.2)
    gui.typewrite(file_path)
    gui.hotkey('enter')
    time.sleep(.2)
    #click on file_name
    gui.click(724,580)    #(X,Y)
    gui.typewrite(file)
    gui.click(1104, 665)#(X,Y)
    #click on send
    time.sleep(.75)
    gui.click(1421,713)#(X,Y)

def sel_contact(cntname):
    web.open("https://web.whatsapp.com/")
    time.sleep(10) #depend on network speed
    # # for searching contact
    gui.click(253, 239)#(X,Y)
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
