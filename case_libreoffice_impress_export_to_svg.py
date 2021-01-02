import pyautogui
import tkinter
import threading
import re
import time

# Q: Does PyAutoGUI work on multi-monitor setups.
# A: No, right now PyAutoGUI only handles the primary monitor.

def update_status_in_infromer(new_status):
    global global_vars
    if re.sub("\n$","",global_vars['infromer_status_text'].get("1.0", tkinter.END)) != new_status:
        global_vars['infromer_status_text'].delete("1.0", tkinter.END)
        global_vars['infromer_status_text'].insert(tkinter.INSERT, new_status)
        global_vars['infromer_status_text'].pack()

def get_current_screenshot(filename=None):
    myScreenshot = pyautogui.screenshot()
    if filename != None:
        myScreenshot.save('data/screenshots/' + filename) #current.png
    return(myScreenshot)

def check_state(state):
    global global_vars
    if state in global_vars['states']:
        return(global_vars['states'][state])
    else:
        return False

def set_state(state,value):
    global global_vars
    global_vars['states'][state] = value

def get_status_searched_and_clicked(filename):
    result = {}
    if not check_state('Found and clicked on ' + filename):
        result = {"status": "Searching and clicking on " + filename,
                  "action": "Search and click on " + filename}
        status = False
    else:
        status = True
    return status, result

def get_status_searched(filename):
    result = {}
    if not check_state('Found ' + filename):
        result = {"status": "Searching for " + filename,
                  "action": "Search for " + filename}
        status = False
    else:
        status = True
    return status, result

def get_custom_operation(custom_operation):
    result = {}
    if not check_state('Done ' + custom_operation):
        result = {"status": "Doing " + custom_operation,
                  "action": "Do " + custom_operation}
        status = False
    else:
        status = True
    return status, result

def choose_svg_type():
    pyautogui.press('down', presses=8)
    pyautogui.press('enter')

def set_svg_filename():
    global global_vars
    pyautogui.press('delete')
    pyautogui.write(str(global_vars['variables']['slide_number']) + '.svg')
    pyautogui.press('enter')

def clear_states_and_increment_slide_number():
    global global_vars
    global_vars['states'] = dict()
    global_vars['variables']['slide_number'] += 1

def get_status_and_action():
    filename = "impress_icon.png"
    operation_status, result = get_status_searched(filename)
    if operation_status:
        filename = "menu_file_icon.png"
        operation_status, result = get_status_searched_and_clicked(filename)
        if operation_status:
            filename = "menu_export_icon.png"
            operation_status, result = get_status_searched_and_clicked(filename)
            if operation_status:
                filename = "menu_export_choose_options.png"
                operation_status, result = get_status_searched_and_clicked(filename)
                if operation_status:
                    custom_operation = "choose_svg_type"
                    operation_status, result = get_custom_operation(custom_operation)
                    if operation_status:
                        filename = "menu_export_choose_filename.png"
                        operation_status, result = get_status_searched_and_clicked(filename)
                        if operation_status:
                            custom_operation = "set_svg_filename"
                            operation_status, result = get_custom_operation(custom_operation)
                            if operation_status:
                                filename = "menu_slide_icon.png"
                                operation_status, result = get_status_searched_and_clicked(filename)
                                if operation_status:
                                    filename = "menu_slide_navigate.png"
                                    operation_status, result = get_status_searched_and_clicked(filename)
                                    if operation_status:
                                        filename = "menu_slide_navigate_next_slide.png"
                                        operation_status, result = get_status_searched_and_clicked(filename)
                                        if operation_status:
                                            custom_operation = "clear_statuses_and_increment_slide_number"
                                            operation_status, result = get_custom_operation(custom_operation)
    if result == {}:
        result["status"] = "empty"
        result["action"] = "empty"
    return(result)

# menu_export_choose_options_svg


def make_action(action_name):
    if re.findall("Search for [^ ]*.png",action_name):
        file_name = re.findall("Search for ([^ ]*\.png)",action_name)[0]
        if file_name == "impress_icon.png":
            coordinates = pyautogui.locateOnScreen('data/fragments/' + file_name, region=(0, 0, 100, 100))
        else:
            coordinates = pyautogui.locateOnScreen('data/fragments/' + file_name)
        if coordinates != None:
            set_state('Found ' + file_name,True)
        else:
            set_state('Found ' + file_name,False)
    elif re.findall("Search and click on [^ ]*.png",action_name):
        file_name = re.findall("Search and click on ([^ ]*\.png)",action_name)[0]
        ## Optimizations
        # print(file_name)
        # location = None
        # while (location == None):
        #     location = pyautogui.locateOnScreen('data/fragments/' + file_name)
        # print(location)

        if file_name == "menu_file_icon.png":
            coordinates = pyautogui.locateCenterOnScreen('data/fragments/' + file_name, region=(2, 23, 32, 26))
        elif file_name == "menu_file_icon.png":
            coordinates = pyautogui.locateCenterOnScreen('data/fragments/' + file_name, region=(2, 23, 32, 26))
        elif file_name == "menu_export_icon.png":
            coordinates = pyautogui.locateCenterOnScreen('data/fragments/' + file_name, region=(9, 393, 82, 29))
        elif file_name == "menu_export_choose_options.png":
            coordinates = pyautogui.locateCenterOnScreen('data/fragments/' + file_name, region=(521, 491, 122, 30))
        elif file_name == "menu_export_choose_filename.png":
            coordinates = pyautogui.locateCenterOnScreen('data/fragments/' + file_name, region=(248, 459, 154, 46))
        elif file_name == "menu_slide_icon.png":
            coordinates = pyautogui.locateCenterOnScreen('data/fragments/' + file_name, region=(213, 26, 34, 19))
        elif file_name == "menu_slide_navigate.png":
            coordinates = pyautogui.locateCenterOnScreen('data/fragments/' + file_name, region=(244, 532, 73, 22))
        elif file_name == "menu_slide_navigate_next_slide.png":
            coordinates = pyautogui.locateCenterOnScreen('data/fragments/' + file_name, region=(499, 577, 192, 27))
        else:
            coordinates = pyautogui.locateCenterOnScreen('data/fragments/' + file_name)
        if coordinates != None:
            pyautogui.click(x=coordinates[0], y=coordinates[1])
            set_state('Found and clicked on ' + file_name,True)
        else:
            set_state('Found and clicked on ' + file_name,False)
    elif re.findall("Do [^ ]*",action_name):
        custom_operation = re.findall("Do ([^ ]*)",action_name)[0]
        if custom_operation == "choose_svg_type":
            choose_svg_type()
            set_state('Done ' + custom_operation, True)
        if custom_operation == "set_svg_filename":
            set_svg_filename()
            set_state('Done ' + custom_operation, True)
        if custom_operation == "clear_statuses_and_increment_slide_number":
            clear_states_and_increment_slide_number()
            # Don't return status for this custom operation

def operation_thread_function():
    while True:
        status_and_action = get_status_and_action()
        update_status_in_infromer(status_and_action["status"])
        make_action(status_and_action["action"])

root = tkinter.Tk()
root.title("PyTouchOK")
root.geometry('300x100')
root.configure(background='white')
root.attributes('-topmost', True)

text = tkinter.Text(root)
global_vars = dict()
global_vars['infromer_status_text'] = text
global_vars['states'] = dict()
global_vars['variables'] = dict()
global_vars['variables']['slide_number'] = 1

operation_tread = threading.Thread(target=operation_thread_function, daemon = True)
operation_tread.start()


tkinter.mainloop()



