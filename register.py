
import ast
import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import serial
import serial.tools.list_ports
import struct
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from IPython.display import HTML


serial_port = "COM10" # COM PORT CHANGE

# Welcome Screen
def main_screen():
    global welcome_screen
    welcome_screen = Tk()
    welcome_screen.geometry("400x300+500+250")
    welcome_screen.title("Pacemaker DCM")

    global counter
    global egram_req 
    egram_req = 0
    counter = 0

    Label(text = "Welcome", bg="grey", width="300", height = "2", font = ("Calibri", 13)).pack()

    Label(text = "").pack()

    Button(text = "Login", width="30", height = "2", command = login).pack()

    Label(text = "").pack()

    Button(text = "Register", width="30", height = "2", command = register).pack()

    welcome_screen.mainloop()

# Registration
def register():
    global register_screen
    register_screen = Toplevel(welcome_screen)
    register_screen.title("Register")
    register_screen.geometry("400x300+500+250")

    global input_username
    global input_password
    global username_entry_register
    global password_entry_register

    input_username = StringVar()
    input_password = StringVar()

    Label(register_screen, text = "Please enter details below to register", font = ("Calibri", 13)).pack()

    Label(register_screen, text = "").pack()

    Label(register_screen, text = "Username").pack()
    username_entry_register = Entry(register_screen, textvariable = input_username)
    username_entry_register.pack()

    Label(register_screen,text = "Password").pack()
    password_entry_register = Entry(register_screen, textvariable = input_password)
    password_entry_register.pack()

    Label(register_screen, text = "").pack()

    Button(register_screen, text = "Register", width = 10, height = 1, command = register_user).pack()

def register_user():
    global username_info

    username_info = input_username.get()
    password_info  = input_password.get()

    username_length = len(username_info)
    password_length = len(password_info)

    special_characters = "!@#$%^&*()-+?_=,<>/ "

    try:
        file = open('database.txt', 'r+')
        d = file.read()
        r = ast.literal_eval(d)
        dict = {username_info: password_info}
        if username_info in r.keys():
            messagebox.showerror('Error', 'Username Already Exists!')
        elif (username_info == "" or password_info == ""):
            messagebox.showerror('Error', 'Username or Password cant be empty!')
        elif (username_length > 20 or password_length > 20):
            messagebox.showerror('Error', '20 Characters Limit Exceeded!')
        elif any(c in special_characters for c in username_info):
            messagebox.showerror('Error', 'Special Characters Cant Be Used!')
        else: 
            if len(r) <= 10:
                r.update(dict)
                file.truncate(0)
                file.close()
                file = open('database.txt', 'w')
                w = file.write(str(r))
                messagebox.showinfo('Success', 'The Account has been Registered Successfully!')
                f = open("data.json", "r+")
                data = json.load(f)
                newUserData = {"username": f"{username_info}",
                                "VOO": {
                                    "LRL": "",
                                    "URL": "",
                                    "VA": "",
                                    "VPW": ""
                                },
                                "AOO": {
                                    "LRL": "",
                                    "URL": "",
                                    "AA": "",
                                    "APW": ""
                                },
                                "VVI": {
                                    "LRL": "",
                                    "URL": "",
                                    "VA": "",
                                    "VPW": "",
                                    "VRP": "",
                                    "VS": "",
                                    "H": "",
                                    "S": ""
                                },
                                "AAI": {
                                    "LRL": "",
                                    "URL": "",
                                    "AA": "",
                                    "APW": "",
                                    "ARP": "",
                                    "AS": "",
                                    "PVARP": "",
                                    "H": "",
                                    "S": ""
                                },
                                "VOOR": {
                                    "LRL": "",
                                    "URL": "",
                                    "VA": "",
                                    "VPW": "",
                                    "MSR": "",
                                    "AT": "",
                                    "REACTION TIME": "",
                                    "RESPONSE FACTOR": "",
                                    "RECOVERY TIME": ""
                                },
                                "AOOR": {
                                    "LRL": "",
                                    "URL": "",
                                    "AA": "",
                                    "APW": "",
                                    "MSR": "",
                                    "AT": "",
                                    "REACTION TIME": "",
                                    "RESPONSE FACTOR": "",
                                    "RECOVERY TIME": ""
                                },
                                "VVIR": {
                                    "LRL": "",
                                    "URL": "",
                                    "VA": "",
                                    "VPW": "",
                                    "VRP": "",
                                    "VS": "",
                                    "H": "",
                                    "S": "",
                                    "MSR": "",
                                    "AT": "",
                                    "REACTION TIME": "",
                                    "RESPONSE FACTOR": "",
                                    "RECOVERY TIME": ""
                                },
                                "AAIR": {
                                    "LRL": "",
                                    "URL": "",
                                    "AA": "",
                                    "APW": "",
                                    "ARP": "",
                                    "AS": "",
                                    "PVARP": "",
                                    "H": "",
                                    "S": "",
                                    "MSR": "",
                                    "AT": "",
                                    "REACTION TIME": "",
                                    "RESPONSE FACTOR": "",
                                    "RECOVERY TIME": ""
                                }}
                data.append(newUserData)
                f.seek(0)
                json.dump(data, f, indent=4)
                f.close()
            else:
                messagebox.showerror('Error', 'User Capacity Reached!')
    except:
        file = open('database.txt', 'w')
        pp = str({'Username': 'password'})
        file.write(pp)
        file.close()
        pp1=[{"username": " ",
                            "VOO": {
                                "LRL": "",
                                "URL": "",
                                "VA": "",
                                "VPW": ""
                            },
                            "AOO": {
                                "LRL": "",
                                "URL": "",
                                "AA": "",
                                "APW": ""
                            },
                            "VVI": {
                                "LRL": "",
                                "URL": "",
                                "VA": "",
                                "VPW": "",
                                "VRP": "",
                                "VS": "",
                                "H": "",
                                "S": ""
                            },
                            "AAI": {
                                "LRL": "",
                                "URL": "",
                                "AA": "",
                                "APW": "",
                                "ARP": "",
                                "AS": "",
                                "PVARP": "",
                                "H": "",
                                "S": ""
                            },
                            "VOOR": {
                                "LRL": "",
                                "URL": "",
                                "VA": "",
                                "VPW": "",
                                "MSR": "",
                                "AT": "",
                                "REACTION TIME": "",
                                "RESPONSE FACTOR": "",
                                "RECOVERY TIME": ""
                            },
                            "AOOR": {
                                "LRL": "",
                                "URL": "",
                                "AA": "",
                                "APW": "",
                                "MSR": "",
                                "AT": "",
                                "REACTION TIME": "",
                                "RESPONSE FACTOR": "",
                                "RECOVERY TIME": ""
                            },
                            "VVIR": {
                                "LRL": "",
                                "URL": "",
                                "VA": "",
                                "VPW": "",
                                "VRP": "",
                                "VS": "",
                                "H": "",
                                "S": "",
                                "MSR": "",
                                "AT": "",
                                "REACTION TIME": "",
                                "RESPONSE FACTOR": "",
                                "RECOVERY TIME": ""
                            },
                            "AAIR": {
                                "LRL": "",
                                "URL": "",
                                "AA": "",
                                "APW": "",
                                "ARP": "",
                                "AS": "",
                                "PVARP": "",
                                "H": "",
                                "S": "",
                                "MSR": "",
                                "AT": "",
                                "REACTION TIME": "",
                                "RESPONSE FACTOR": "",
                                "RECOVERY TIME": ""
                            }}]
        with open('data.json','w') as f:
            json.dump(pp1,f,indent=4)
        f.close()
        messagebox.showerror('Error', 'The database was just created. Please Register again.')

    username_entry_register.delete(0, END)
    password_entry_register.delete(0, END)

    register_screen.destroy()

# Login
def login():
    global login_screen
    login_screen = Toplevel(welcome_screen)
    login_screen.title("Login")
    login_screen.geometry("400x300+500+250")

    global counter
    if(counter >= 1):
        messagebox.showerror('Error', 'Please Stop the program and run it again!')
        login_screen.destroy()

    Label(login_screen, text = "Please enter details below to login", font = ("Calibri", 13)).pack()
    Label(login_screen, text = "").pack()

    global username_entry_login
    global password_entry_login
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text = "Username").pack()
    username_entry_login = Entry(login_screen, textvariable = username_verify)
    username_entry_login.pack()

    Label(login_screen, text = "").pack()

    Label(login_screen, text = "Password").pack()
    password_entry_login = Entry(login_screen, textvariable = password_verify)
    password_entry_login.pack()

    Label(login_screen, text = "").pack()

    Button(login_screen, text = "Login", width = 10, height = 1, command = login_verify).pack()

def login_verify():
    global username_info_login

    username_info_login = username_verify.get()
    password_info_login = password_verify.get()

    username_entry_login.delete(0, END)
    password_entry_login.delete(0, END)

    file = open('database.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username_info_login in r.keys() and password_info_login==r[username_info_login]:
        login_screen.destroy()
        connect() #Leads to another screen
    else:
        messagebox.showerror('Error', 'Login Unsuccessful')

def connect():
    global connect_screen
    connect_screen = Toplevel(welcome_screen)
    connect_screen.geometry("400x300+500+250")
    connect_screen.title("Modes")

    Label(connect_screen, text = "Please click the button to connect", bg="grey", width="300", height = "2", font = ("Calibri", 13)).pack()

    Label(connect_screen, text = "").pack()

    Button(connect_screen, text = "Connect", width="30", height = "2", command = connect_destroy).pack()

def connect_destroy():
    try:
        ser = serial.Serial(serial_port, 115200)  # COM PORT CHANGE
        messagebox.showinfo('Success', 'You have been successfully connected!')
        connect_screen.destroy()
        modes()
    except:
        messagebox.showerror('Error', 'Make sure to connect the pacemaker!')
        connect_screen.destroy()

# Modes
def modes():
    global modes_screen
    modes_screen = Toplevel(welcome_screen)
    modes_screen.geometry("490x330+500+250")
    modes_screen.title("Modes")
    
    global counter
    counter += 1

    Label(modes_screen, text = "Please choose one of the following modes", bg="grey", width="300", height = "2", font = ("Calibri", 13)).pack()

    Label(modes_screen, text = "").pack()

    Button(modes_screen, text = "VOO", width="30", height = "2", command = voo).place(x=10, y=60)

    Button(modes_screen, text = "AOO", width="30", height = "2", command = aoo).place(x=10, y=120)

    Button(modes_screen, text = "VVI", width="30", height = "2", command = vvi).place(x=10, y=180)

    Button(modes_screen, text = "AAI", width="30", height = "2", command = aai).place(x=10, y=240)

    Button(modes_screen, text = "VOOR", width="30", height = "2", command = voor).place(x=260, y=60)

    Button(modes_screen, text = "AOOR", width="30", height = "2", command = aoor).place(x=260, y=120)

    Button(modes_screen, text = "VVIR", width="30", height = "2", command = vvir).place(x=260, y=180)
    
    Button(modes_screen, text = "AAIR", width="30", height = "2", command = aair).place(x=260, y=240)

    Label(modes_screen, text = "Current User Logged In: %s" % (username_info_login)).place(x=10, y=300)
    
    Button(modes_screen, text = "Logout", width="5", height = "2", command = logout).place(x=420, y=5)

    


def logout():
    modes_screen.destroy()

##############################################################################################################################################################################################
def voo():
    modes_screen.destroy()

    global voo_screen
    voo_screen = Toplevel(welcome_screen)
    voo_screen.geometry("400x500+500+100")
    voo_screen.title("VOO")

    global url_voo
    
    global modeSet
    modeSet = 'VOO'

    Label(voo_screen, text = "Set the details below", font = ("Calibri", 13)).pack()
    Label(voo_screen, text = "").pack()

    Label(voo_screen, text = "Lower Rate Limit (ppm)").pack()
    options = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
    ]
    choice = DoubleVar()
    choice.set(options[0])
    list = ttk.Combobox(voo_screen, value= options)
    list.current(14)
    list.bind("<<ComboboxSelected>>")
    list.pack() 
    Label(voo_screen, text = "").pack()

    Label(voo_screen, text = "Upper Rate Limit (ppm)").pack()
    url_voo = Scale(voo_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_voo.set(120)
    url_voo.pack()
    Label(voo_screen, text = "").pack()

    Label(voo_screen, text = "Ventricular Amplitude (V)").pack()
    options2 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice1 = DoubleVar()
    choice1.set(options2[0])
    list1 = ttk.Combobox(voo_screen, value= options2)
    list1.current(29)
    list1.bind("<<ComboboxSelected>>")
    list1.pack()
    Label(voo_screen, text = "").pack()

    Label(voo_screen, text = "Ventricular Pulse Width (ms)").pack()
    options3 = [
        "1","2","3","4","5","6","7","8","9","10", "11","12","13","14","15","16","17","18","19","20", "21","22","23","24","25","26","27","28","29","30"
    ]
    choice2 = DoubleVar()
    choice2.set(options3[0])
    list2 = ttk.Combobox(voo_screen, value= options3)
    list2.current(4)
    list2.bind("<<ComboboxSelected>>")
    list2.pack()
    Label(voo_screen, text = "").pack()

    def show():

        global lrl_voo
        global va_voo
        global vpw_voo
        
        lrl_voo = list.get()
        va_voo = list1.get()
        vpw_voo = list2.get()
        if (int(lrl_voo) > url_voo.get()):
            messagebox.showerror('Error', 'LRL is higher than URL')
        else:    
            set_values()
            print("The values for VOO")
            print("LOWER RATE LIMIT:", lrl_voo)
            print("UPPER RATE LIMIT:", url_voo.get())
            print("VENTRICULAR AMPLITUDE:", va_voo)
            print("VENTRICULAR PULSE WIDTH:", vpw_voo)
            print("-------------------------------------------------------------------")

            # serial_port = "COM10"

            Start = b'\x16'
            Fn_set = b'\x55'
            #test
            vpw =struct.pack("H", int(vpw_voo))
            mode = struct.pack("B", 1)
            lrl = struct.pack("H", int(lrl_voo))
            url = struct.pack("B", url_voo.get())
            vamp = struct.pack("f", float(va_voo))
            aamp = struct.pack("f", 0)
            apw = struct.pack("H", 0)
            vrp = struct.pack("H", 0)
            arp = struct.pack("H", 0)
            atr_sens = struct.pack("f", 0)
            vent_sens = struct.pack("f", 0)
            pvarp = struct.pack("H", 0)
            rs = struct.pack("B", 0)
            hs = struct.pack("B", 0)
            Signal_set = (Start + Fn_set + vpw + lrl + mode + url + vamp + aamp + apw + vrp + arp + atr_sens + vent_sens + pvarp + rs + hs)

            with serial.Serial(serial_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)
                time.sleep(0.5)
    
    def echo_signal():
        # serial_port = "COM10"

        Start = b'\x16'
        SYNC = b'\x22'
        vpw =struct.pack("H", int(vpw_voo))
        mode = struct.pack("B", 1)
        lrl = struct.pack("H", int(lrl_voo))
        url = struct.pack("B", url_voo.get())
        vamp = struct.pack("f", float(va_voo))
        aamp = struct.pack("f", 0)
        apw = struct.pack("H", 0)
        vrp = struct.pack("H", 0)
        arp = struct.pack("H", 0)
        atr_sens = struct.pack("f", 0)
        vent_sens = struct.pack("f", 0)
        pvarp = struct.pack("H", 0)
        rs = struct.pack("B", 0)
        hs = struct.pack("B", 0)

        Signal_echo = Start + SYNC + vpw + lrl + mode + url + vamp + aamp + apw + vrp + arp + atr_sens + vent_sens + pvarp + rs + hs

        with serial.Serial(serial_port, 115200) as pacemaker:
            pacemaker.write(Signal_echo)
            data = pacemaker.read(32)
            time.sleep(0.5)
            vpw_rev =  struct.unpack("H", data[0:2])[0]
            lrl_rev = struct.unpack("H", data[2:4])[0]
            mode_rev = data[4]
            url_rev = data[5]
            vamp_rev = struct.unpack("f", data[6:10])[0]
            aamp_rev = struct.unpack("f", data[10:14])[0]
            apw_rev = struct.unpack("H", data[14:16])[0]
            vrp_rev =  struct.unpack("H", data[16:18])[0]
            arp_rev =  struct.unpack("H", data[18:20])[0]
            atrsens_rev =  struct.unpack("f", data[20:24])[0]
            ventsens_rev =  struct.unpack("f", data[24:28])[0]
            PVARP_rev =  struct.unpack("H", data[28:30])[0]
            rs_rev =  data[30]
            hs_rev =  data[31]

            time.sleep(0.5)
            print("From the board (VOO):")
            print("MODE = ", mode_rev)
            print("LOWER RATE LIMIT = ", lrl_rev)
            print("UPPER RATE LIMIT = ",  url_rev)
            print("VENTRICULAR PULSE WIDTH = ", vpw_rev)
            print("VENTRICULAR AMPLITUDE = ", vamp_rev)

            serial.time.sleep(0.5)

    Button(voo_screen, text = "SEND", width="5", height = "1", command = show).place(x=70, y=400)
    Label(voo_screen, text = "").pack()
    Button(voo_screen, text = "LOAD", width="5", height = "1", command = access_val).place(x=175, y=400)
    Label(voo_screen, text = "").pack()
    Button(voo_screen, text = "BACK", width="5", height = "1", command = destroy_voo).place(x=280, y=400)
    Label(voo_screen, text = "").pack()
    Button(voo_screen, text = "Echo", width="5", height = "1", command = echo_signal).place(x=70, y=440)
    Label(voo_screen, text = "").pack()
    Button(voo_screen, text = "EGRAM", width="5", height = "1", command = egram_plot).place(x=175, y=440)
    Label(voo_screen, text = "").pack()
    Button(voo_screen, text = "STOP", width="5", height = "1", command = egram_stop).place(x=280, y=440)
    Label(voo_screen, text = "").pack()
    Label(voo_screen, text = "Current User Logged In: %s" % (username_info_login)).place(x=12, y=470)
##############################################################################################################################################################################################
def aoo():
    modes_screen.destroy()

    global aoo_screen
    aoo_screen = Toplevel(welcome_screen)
    aoo_screen.geometry("400x500+500+100")
    aoo_screen.title("AOO")

    global url_aoo

    global modeSet
    modeSet = 'AOO'

    Label(aoo_screen, text = "Set the details below", font = ("Calibri", 13)).pack()
    Label(aoo_screen, text = "").pack()

    Label(aoo_screen, text = "Lower Rate Limit (ppm)").pack()
    options = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
    ]
    choice = DoubleVar()
    choice.set(options[0])
    list = ttk.Combobox(aoo_screen, value= options)
    list.current(14)
    list.bind("<<ComboboxSelected>>")
    list.pack() 
    Label(aoo_screen, text = "").pack()

    Label(aoo_screen, text = "Upper Rate Limit (ppm)").pack()
    url_aoo = Scale(aoo_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_aoo.set(120)
    url_aoo.pack()
    Label(aoo_screen, text = "").pack()

    Label(aoo_screen, text = "Atrial Amplitude (V)").pack()
    options1 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice1 = DoubleVar()
    choice1.set(options1[0])
    list1 = ttk.Combobox(aoo_screen, value= options1)
    list1.current(29)
    list1.bind("<<ComboboxSelected>>")
    list1.pack()
    Label(aoo_screen, text = "").pack()

    Label(aoo_screen, text = "Atrial Pulse Width (ms)").pack()
    options2 = [
         "1","2","3","4","5","6","7","8","9","10", "11","12","13","14","15","16","17","18","19","20", "21","22","23","24","25","26","27","28","29","30"
    ]
    choice2 = DoubleVar()
    choice2.set(options2[0])
    list2 = ttk.Combobox(aoo_screen, value= options2)
    list2.current(4)
    list2.bind("<<ComboboxSelected>>")
    list2.pack()
    Label(aoo_screen, text = "").pack()

    def show():

        global lrl_aoo
        global aa_aoo
        global apw_aoo

        lrl_aoo = list.get()
        aa_aoo = list1.get()
        apw_aoo = list2.get()
        if (int(lrl_aoo) > url_aoo.get()):
            messagebox.showerror('Error', 'LRL is higher than URL')
        else: 
            set_values()
            print("The values for AOO")
            print("LOWER RATE LIMIT:", lrl_aoo)
            print("UPPER RATE LIMIT:", url_aoo.get())
            print("ATRIAL AMPLITUDE:", aa_aoo)
            print("ATRIAL PULSE WIDTH:", apw_aoo)
            print("-------------------------------------------------------------------")

            # serial_port = "COM10"

            Start = b'\x16'
            Fn_set = b'\x55'
            #test
            vpw =struct.pack("H", 0)
            mode = struct.pack("B", 2)
            lrl = struct.pack("H", int(lrl_aoo))
            url = struct.pack("B", url_aoo.get())
            vamp = struct.pack("f", 0)
            aamp = struct.pack("f", float(aa_aoo))
            apw = struct.pack("H", int(apw_aoo))
            vrp = struct.pack("H", 0)
            arp = struct.pack("H", 0)
            atr_sens = struct.pack("f", 0)
            vent_sens = struct.pack("f", 0)
            pvarp = struct.pack("H", 0)
            rs = struct.pack("B", 0)
            hs = struct.pack("B", 0)
            Signal_set = (Start + Fn_set + vpw + lrl + mode + url + vamp + aamp + apw + vrp + arp + atr_sens + vent_sens + pvarp + rs + hs)

            with serial.Serial(serial_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)
                time.sleep(0.5)
    def echo_signal():
        # serial_port = "COM10"

        Start = b'\x16'
        SYNC = b'\x22'
        vpw =struct.pack("H", 0)
        mode = struct.pack("B", 2)
        lrl = struct.pack("H", int(lrl_aoo))
        url = struct.pack("B", url_aoo.get())
        vamp = struct.pack("f", 0)
        aamp = struct.pack("f", float(aa_aoo))
        apw = struct.pack("H", int(apw_aoo))
        vrp = struct.pack("H", 0)
        arp = struct.pack("H", 0)
        atr_sens = struct.pack("f", 0)
        vent_sens = struct.pack("f", 0)
        pvarp = struct.pack("H", 0)
        rs = struct.pack("B", 0)
        hs = struct.pack("B", 0)

        Signal_echo = Start + SYNC + vpw + lrl + mode + url + vamp + aamp + apw + vrp + arp + atr_sens + vent_sens + pvarp + rs + hs

        with serial.Serial(serial_port, 115200) as pacemaker:
            pacemaker.write(Signal_echo)
            data = pacemaker.read(32)
            time.sleep(0.5)
            vpw_rev =  struct.unpack("H", data[0:2])[0]
            lrl_rev = struct.unpack("H", data[2:4])[0]
            mode_rev = data[4]
            url_rev = data[5]
            vamp_rev = struct.unpack("f", data[6:10])[0]
            aamp_rev = struct.unpack("f", data[10:14])[0]
            apw_rev = struct.unpack("H", data[14:16])[0]
            vrp_rev =  struct.unpack("H", data[16:18])[0]
            arp_rev =  struct.unpack("H", data[18:20])[0]
            atrsens_rev =  struct.unpack("f", data[20:24])[0]
            ventsens_rev =  struct.unpack("f", data[24:28])[0]
            PVARP_rev =  struct.unpack("H", data[28:30])[0]
            rs_rev =  data[30]
            hs_rev =  data[31]

            time.sleep(0.5)
            print("From the board (AOO):")
            print("MODE = ", mode_rev)
            print("LOWER RATE LIMIT = ", lrl_rev)
            print("UPPER RATE LIMIT = ",  url_rev)
            print("ATRIAL PULSE WIDTH = ", apw_rev)
            print("ATRIAL AMPLITUDE = ", aamp_rev)

            serial.time.sleep(0.5)

    Button(aoo_screen, text = "SEND", width="5", height = "1", command = show).place(x=70, y=400)
    Label(aoo_screen, text = "").pack()
    Button(aoo_screen, text = "LOAD", width="5", height = "1", command = access_val).place(x=175, y=400)
    Label(aoo_screen, text = "").pack()
    Button(aoo_screen, text = "BACK", width="5", height = "1", command = destroy_aoo).place(x=280, y=400)
    Label(aoo_screen, text = "").pack()
    Button(aoo_screen, text = "ECHO", width="5", height = "1", command= echo_signal).place(x=70, y=440)
    Label(aoo_screen, text = "").pack()
    Button(aoo_screen, text = "EGRAM", width="5", height = "1", command = egram_plot).place(x=175, y=440)
    Label(aoo_screen, text = "").pack()
    Button(aoo_screen, text = "STOP", width="5", height = "1", command = egram_stop).place(x=280, y=440)
    Label(aoo_screen, text = "").pack()
    Label(aoo_screen, text = "Current User Logged In: %s" % (username_info_login)).place(x=12, y=470)
##############################################################################################################################################################################################
def vvi():
    modes_screen.destroy()

    global vvi_screen
    vvi_screen = Toplevel(welcome_screen)
    vvi_screen.geometry("400x500+500+50")
    vvi_screen.title("VVI")

    global url_vvi
    global vrp_vvi
    global rs_vvi

    global modeSet
    modeSet = 'VVI'

    Label(vvi_screen, text = "Set the details below", font = ("Calibri", 13)).pack()
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Lower Rate Limit (ppm)").place(x=15, y=60)
    options = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
    ]
    choice = DoubleVar()
    choice.set(options[0])
    list = ttk.Combobox(vvi_screen, value= options)
    list.current(14)
    list.bind("<<ComboboxSelected>>")
    list.place(x=10, y=90)

    Label(vvi_screen, text = "Upper Rate Limit (ppm)").place(x=15, y=135)
    url_vvi = Scale(vvi_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_vvi.set(120)
    url_vvi.place(x=15, y=155)

    Label(vvi_screen, text = "Ventricular Amplitude (V)").place(x=12, y=220)
    options1 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice1 = DoubleVar()
    choice1.set(options1[0])
    list1 = ttk.Combobox(vvi_screen, value= options1)
    list1.current(29)
    list1.bind("<<ComboboxSelected>>")
    list1.place(x=10, y=250)

    Label(vvi_screen, text = "Ventricular Pulse Width (ms)").place(x=12, y=295)
    options2 = [
        "1","2","3","4","5","6","7","8","9","10", "11","12","13","14","15","16","17","18","19","20", "21","22","23","24","25","26","27","28","29","30"
    ]
    choice2 = DoubleVar()
    choice2.set(options2[0])
    list2 = ttk.Combobox(vvi_screen, value= options2)
    list2.current(4)
    list2.bind("<<ComboboxSelected")
    list2.place(x=12, y=325)

    Label(vvi_screen, text = "Ventricular sensitivity (V)").place(x=220, y=60)
    options3 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice3 = DoubleVar()
    choice3.set(options3[0])
    list3 = ttk.Combobox(vvi_screen, value= options3)
    list3.current(6)
    list3.bind("<<ComboboxSelected>>")
    list3.place(x=220, y=90)

    Label(vvi_screen, text = "Ventricular Refractory Period (ms)").place(x=220, y=135)
    vrp_vvi = Scale(vvi_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    vrp_vvi.set(320)
    vrp_vvi.place(x=220, y=155)

    Label(vvi_screen, text = "Hysteresis ").place(x=220, y=220)
    options4 = [
        "OFF","same as LRL",
    ]
    choice4 = StringVar()
    choice4.set(options4[0])
    list4 = ttk.Combobox(vvi_screen, value= options4)
    list4.current(0)
    list4.bind("<<ComboboxSelected>>")
    list4.place(x=220, y=250)

    Label(vvi_screen, text = "Rate smoothing").place(x=220, y=295)
    rs_vvi = Scale(vvi_screen, from_=0, to =25, resolution=3.07, orient=HORIZONTAL)
    rs_vvi.place(x=220, y=315)

    def show():

        global lrl_vvi
        global va_vvi
        global vpw_vvi
        global vs_vvi
        global hysteresis_vvi

        lrl_vvi = list.get()
        va_vvi = list1.get()
        vpw_vvi = list2.get()
        vs_vvi = list3.get()
        if (list4.get() == "OFF"):
            hysteresis_vvi = 0
        else:
            hysteresis_vvi = list.get()

        if (int(lrl_vvi) > url_vvi.get()):
            messagebox.showerror('Error', 'LRL is higher than URL')
        elif ((float(60000/int(lrl_vvi)) - float(vpw_vvi)) < float(vrp_vvi.get())):
            messagebox.showerror('Error', 'VRP cant be greater than 60000/LRL - PW!')
        else: 
            set_values()
            print("The values for VVI")
            print("LOWER RATE LIMIT:", lrl_vvi) 
            print("UPPER RATE LIMIT:", url_vvi.get()) 
            print("VENTRICULAR AMPLITUDE:", va_vvi) 
            print("VENTRICULAR PULSE WIDTH:", vpw_vvi) 
            print("VENTRICULAR SENSITIVITY:", vs_vvi) 
            print("VENTRICULAR REFRACTORY PERIOD:", vrp_vvi.get()) 
            print("HYSTERESIS:", hysteresis_vvi) 
            print("RATE SMOOTHING:", rs_vvi.get()) 
            print("-------------------------------------------------------------------")

            # serial_port = "COM10"

            Start = b'\x16'
            Fn_set = b'\x55'
            #test
            vpw =struct.pack("H", int(vpw_vvi))
            mode = struct.pack("B", 3)
            lrl = struct.pack("H", int(lrl_vvi))
            url = struct.pack("B", url_vvi.get())
            vamp = struct.pack("f", float(va_vvi))
            aamp = struct.pack("f", 0)
            apw = struct.pack("H", 0)
            vrp = struct.pack("H", vrp_vvi.get())
            arp = struct.pack("H", 0)
            atr_sens = struct.pack("f", 0)
            vent_sens = struct.pack("f", float(vs_vvi))
            pvarp = struct.pack("H", 0)
            rs = struct.pack("B", rs_vvi.get())
            hs = struct.pack("B", int(hysteresis_vvi)) 
            Signal_set = (Start + Fn_set + vpw + lrl + mode + url + vamp + aamp + apw + vrp + arp + atr_sens + vent_sens + pvarp + rs + hs)

            with serial.Serial(serial_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)
                time.sleep(0.5)

    def echo_signal():
        # serial_port = "COM10"

        Start = b'\x16'
        SYNC = b'\x22'
        vpw =struct.pack("H", int(vpw_vvi))
        mode = struct.pack("B", 3)
        lrl = struct.pack("H", int(lrl_vvi))
        url = struct.pack("B", url_vvi.get())
        vamp = struct.pack("f", float(va_vvi))
        aamp = struct.pack("f", 0)
        apw = struct.pack("H", 0)
        vrp = struct.pack("H", vrp_vvi.get())
        arp = struct.pack("H", 0)
        atr_sens = struct.pack("f", 0)
        vent_sens = struct.pack("f", float(vs_vvi))
        pvarp = struct.pack("H", 0)
        rs = struct.pack("B", rs_vvi.get())
        hs = struct.pack("B", int(hysteresis_vvi))

        Signal_echo = Start + SYNC + vpw + lrl + mode + url + vamp + aamp + apw + vrp + arp + atr_sens + vent_sens + pvarp + rs + hs

        with serial.Serial(serial_port, 115200) as pacemaker:
            pacemaker.write(Signal_echo)
            data = pacemaker.read(32)
            time.sleep(0.5)
            vpw_rev =  struct.unpack("H", data[0:2])[0]
            lrl_rev = struct.unpack("H", data[2:4])[0]
            mode_rev = data[4]
            url_rev = data[5]
            vamp_rev = struct.unpack("f", data[6:10])[0]
            aamp_rev = struct.unpack("f", data[10:14])[0]
            apw_rev = struct.unpack("H", data[14:16])[0]
            vrp_rev =  struct.unpack("H", data[16:18])[0]
            arp_rev =  struct.unpack("H", data[18:20])[0]
            atrsens_rev =  struct.unpack("f", data[20:24])[0]
            ventsens_rev =  struct.unpack("f", data[24:28])[0]
            PVARP_rev =  struct.unpack("H", data[28:30])[0]
            rs_rev =  data[30]
            hs_rev =  data[31]

            time.sleep(0.5)
            print("From the board (VVI):")
            print("MODE = ", mode_rev)
            print("LOWER RATE LIMIT = ", lrl_rev)
            print("UPPER RATE LIMIT = ",  url_rev)
            print("VENTRICULAR PULSE WIDTH = ", vpw_rev)
            print("VENTRICULAR AMPLITUDE = ", vamp_rev)
            print("VENTRICULAR SENSITIVITY:", ventsens_rev) 
            print("VENTRICULAR REFRACTORY PERIOD:", vrp_rev) 
            print("HYSTERESIS:", hs_rev) 
            print("RATE SMOOTHING:", rs_rev)
            serial.time.sleep(0.5)



    Button(vvi_screen, text = "Save", width="5", height = "1", command = show).place(x=70, y=400)
    Label(vvi_screen, text = "").pack()
    Button(vvi_screen, text = "Load", width="5", height = "1", command = access_val).place(x=175, y=400)
    Label(vvi_screen, text = "").pack()
    Button(vvi_screen, text = "Back", width="5", height = "1", command = destroy_vvi).place(x=280, y=400)
    Label(vvi_screen, text = "").pack()
    Button(vvi_screen, text = "Echo", width="5", height = "1", command = echo_signal).place(x=70, y=440)
    Label(vvi_screen, text = "").pack()
    Button(vvi_screen, text = "EGRAM", width="5", height = "1", command = egram_plot).place(x=175, y=440)
    Label(vvi_screen, text = "").pack()
    Button(vvi_screen, text = "STOP", width="5", height = "1", command = egram_stop).place(x=280, y=440)
    Label(vvi_screen, text = "").pack()
    Label(vvi_screen, text = "Current User Logged In: %s" % (username_info_login)).place(x=12, y=470)
##############################################################################################################################################################################################
def aai():
    modes_screen.destroy()

    global aai_screen
    aai_screen = Toplevel(welcome_screen)
    aai_screen.geometry("400x500+500+50")
    aai_screen.title("AAI")

    global lrl_aai
    global url_aai
    global aa_aai
    global apw_aai
    global as_aai
    global arp_aai
    global pvarp_aai
    global hysteresis_aai
    global rs_aai

    global modeSet
    modeSet = 'AAI'

    Label(aai_screen, text = "Set the details below", font = ("Calibri", 13)).pack()

    Label(aai_screen, text = "Lower Rate Limit (ppm)").place(x=15, y=60)
    options = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
    ]
    choice = DoubleVar()
    choice.set(options[0])
    list = ttk.Combobox(aai_screen, value= options)
    list.current(14)
    list.bind("<<ComboboxSelected>>")
    list.place(x=10, y=90)

    Label(aai_screen, text = "Upper Rate Limit (ppm)").place(x=15, y=135)
    url_aai = Scale(aai_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_aai.set(120)
    url_aai.place(x=15, y=155)

    Label(aai_screen, text = "Atrial Amplitude (V)").place(x=12, y=220)
    options1 = [
        "0","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9","2.0",
        "2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.5","4.0","4.5","5.0","5.5",
        "6.0","6.5","7.0","7.5",
    ]
    choice1 = DoubleVar()
    choice1.set(options1[0])
    list1 = ttk.Combobox(aai_screen, value= options1)
    list1.current(29)
    list1.bind("<<ComboboxSelected>>")
    list1.place(x=10, y=250)

    Label(aai_screen, text = "Atrial Pulse Width (ms)").place(x=12, y=295)
    options2 = [
        "1","2","3","4","5","6","7","8","9","10", "11","12","13","14","15","16","17","18","19","20", "21","22","23","24","25","26","27","28","29","30"
    ]
    choice2 = DoubleVar()
    choice2.set(options2[0])
    list2 = ttk.Combobox(aai_screen, value= options2)
    list2.current(4)
    list2.bind("<<ComboboxSelected")
    list2.place(x=12, y=325)

    Label(aai_screen, text = "Atrial sensitivity (mV)").place(x=12, y=370)
    options3 = [
        "0.25","0.5","0.75","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5","6.0","6.5","7.0","7.5","8.0","8.5","9.0","9.5","10.0",
    ]
    choice3 = DoubleVar()
    choice3.set(options3[0])
    list3 = ttk.Combobox(aai_screen, value= options3)
    list3.current(2)
    list3.bind("<<ComboboxSelected>>")
    list3.place(x=12, y=400)

    Label(aai_screen, text = "Atrial Refractory Period (ms)").place(x=220, y=60)
    arp_aai = Scale(aai_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    arp_aai.set(250)
    arp_aai.place(x=220, y=80)

    Label(aai_screen, text = "Post Ventricular Atrial Refractory Period (ms)").place(x=220, y=145)
    pvarp_aai = Scale(aai_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    pvarp_aai.set(250)
    pvarp_aai.place(x=220, y=165)

    Label(aai_screen, text = "Hysteresis ").place(x=220, y=230)
    options4 = [
        "OFF","same as LRL",
    ]
    choice4 = StringVar()
    choice4.set(options4[0])
    list4 = ttk.Combobox(aai_screen, value= options4)
    list4.current(0)
    list4.bind("<<ComboboxSelected>>")
    list4.place(x=220, y=250)

    Label(aai_screen, text = "Rate smoothing").place(x=220, y=295)
    rs_aai = Scale(aai_screen, from_=0, to =25, resolution=3.07, orient=HORIZONTAL)
    rs_aai.place(x=220, y=315)

    def show():

        global lrl_aai
        global aa_aai
        global apw_aai
        global as_aai
        global hysteresis_aai

        lrl_aai = list.get()
        aa_aai = list1.get()
        apw_aai = list2.get()
        as_aai = list3.get()
        if (list4.get() == "OFF"):
            hysteresis_aai = 0
        else:
            hysteresis_aai = list.get()
        if (int(lrl_aai) > url_aai.get()):
            messagebox.showerror('Error', 'LRL is higher than URL')
        elif ((float(60000/int(lrl_aai)) - float(apw_aai)) < float(arp_aai.get())):
            messagebox.showerror('Error', 'ARP cant be greater than 60000/LRL - PW!')
        else: 
            set_values()
            print("The values for AAI")
            print("LOWER RATE LIMIT:", lrl_aai) 
            print("UPPER RATE LIMIT:", url_aai.get()) 
            print("ATRIAL AMPLITUDE:", aa_aai) 
            print("ATRIAL PULSE WIDTH:", apw_aai) 
            print("ATRIAL SENSITIVITY:", as_aai) 
            print("ATRIAL REFRACTORY PERIOD:", arp_aai.get()) 
            print("POST VENTRICULAR ATRIAL REFRACTORY PERIOD:", pvarp_aai.get()) 
            print("HYSTERESIS:", hysteresis_aai)
            print("RATE SMOOTHING:", rs_aai.get())
            print("-------------------------------------------------------------------")
        
            # serial_port = "COM10"

            Start = b'\x16'
            Fn_set = b'\x55'
            #test
            vpw =struct.pack("H", 0)
            mode = struct.pack("B", 4)
            lrl = struct.pack("H", int(lrl_aai))
            url = struct.pack("B", url_aai.get())
            vamp = struct.pack("f", 0)
            aamp = struct.pack("f", float(aa_aai))
            apw = struct.pack("H", int(apw_aai))
            vrp = struct.pack("H", 0)
            arp = struct.pack("H", arp_aai.get())
            atr_sens = struct.pack("f", float(as_aai))
            vent_sens = struct.pack("f", 0)
            pvarp = struct.pack("H", pvarp_aai.get())
            rs = struct.pack("B", rs_aai.get())
            hs = struct.pack("B", int(hysteresis_aai)) 
            Signal_set = (Start + Fn_set + vpw + lrl + mode + url + vamp + aamp + apw + vrp + arp + atr_sens + vent_sens + pvarp + rs + hs)

            with serial.Serial(serial_port, 115200) as pacemaker:
                pacemaker.write(Signal_set)
                time.sleep(0.5)
    
    def echo_signal():
        # serial_port = "COM10"

        Start = b'\x16'
        SYNC = b'\x22'
        vpw =struct.pack("H", 0)
        mode = struct.pack("B", 3)
        lrl = struct.pack("H", int(lrl_aai))
        url = struct.pack("B", url_aai.get())
        vamp = struct.pack("f", 0)
        aamp = struct.pack("f", float(aa_aai))
        apw = struct.pack("H", int(apw_aai))
        vrp = struct.pack("H", 0)
        arp = struct.pack("H", arp_aai.get())
        atr_sens = struct.pack("f", float(as_aai))
        vent_sens = struct.pack("f", 0)
        pvarp = struct.pack("H", pvarp_aai.get())
        rs = struct.pack("B", rs_aai.get())
        hs = struct.pack("B", int(hysteresis_aai)) 

        Signal_echo = Start + SYNC + vpw + lrl + mode + url + vamp + aamp + apw + vrp + arp + atr_sens + vent_sens + pvarp + rs + hs

        with serial.Serial(serial_port, 115200) as pacemaker:
            pacemaker.write(Signal_echo)
            data = pacemaker.read(32)
            time.sleep(0.5)
            vpw_rev =  struct.unpack("H", data[0:2])[0]
            lrl_rev = struct.unpack("H", data[2:4])[0]
            mode_rev = data[4]
            url_rev = data[5]
            vamp_rev = struct.unpack("f", data[6:10])[0]
            aamp_rev = struct.unpack("f", data[10:14])[0]
            apw_rev = struct.unpack("H", data[14:16])[0]
            vrp_rev =  struct.unpack("H", data[16:18])[0]
            arp_rev =  struct.unpack("H", data[18:20])[0]
            atrsens_rev =  struct.unpack("f", data[20:24])[0]
            ventsens_rev =  struct.unpack("f", data[24:28])[0]
            PVARP_rev =  struct.unpack("H", data[28:30])[0]
            rs_rev =  data[30]
            hs_rev =  data[31]

            time.sleep(0.5)
            print("From the board (AAI):")
            print("MODE = ", mode_rev)
            print("LOWER RATE LIMIT = ", lrl_rev)
            print("UPPER RATE LIMIT = ",  url_rev)
            print("ATRIAL PULSE WIDTH = ", apw_rev)
            print("ATRIAL AMPLITUDE = ", aamp_rev)
            print("ATRIAL SENSITIVITY:", atrsens_rev) 
            print("ATRIAL REFRACTORY PERIOD:", arp_rev) 
            print("POST VENTRICULAR ATRIAL REFRACTORY PERIOD:", PVARP_rev) 
            print("HYSTERESIS:", hs_rev)
            print("RATE SMOOTHING:", rs_rev)
            serial.time.sleep(0.5)

    Button(aai_screen, text = "Save", width="5", height = "1", command = show).place(x=190, y=385)
    Label(aai_screen, text = "").pack()
    Button(aai_screen, text = "Load", width="5", height = "1", command = access_val).place(x=250, y=385)
    Label(aai_screen, text = "").pack()
    Button(aai_screen, text = "Back", width="5", height = "1", command = destroy_aai).place(x=310, y=385)
    Label(aai_screen, text = "").pack()
    Button(aai_screen, text = "Echo", width="5", height = "1", command = echo_signal).place(x=190, y=440)
    Label(aai_screen, text = "").pack()
    Button(aai_screen, text = "EGRAM", width="5", height = "1", command = egram_plot).place(x=250, y=440)
    Label(aai_screen, text = "").pack()
    Button(aai_screen, text = "STOP", width="5", height = "1", command = egram_stop).place(x=310, y=440)
    Label(aai_screen, text = "").pack()
    Label(aai_screen, text = "Current User Logged In: %s" % (username_info_login)).place(x=12, y=470)
##############################################################################################################################################################################################
##############################################################################################################################################################################################
def voor():
    modes_screen.destroy()

    global voor_screen
    voor_screen = Toplevel(welcome_screen)
    voor_screen.geometry("400x470+500+100")
    voor_screen.title("VOOR")

    global url_voor
    global msr_voor
    global reactiont_voor
    global responsef_voor
    global recoveryt_voor
    
    global modeSet
    modeSet = 'VOOR'

    Label(voor_screen, text = "Set the details below", font = ("Calibri", 13)).pack()
    Label(voor_screen, text = "").pack()

    Label(voor_screen, text = "Lower Rate Limit (ppm)").place(x=15, y=60)
    options = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
    ]
    choice = DoubleVar()
    choice.set(options[0])
    list = ttk.Combobox(voor_screen, value= options)
    list.current(14)
    list.bind("<<ComboboxSelected>>")
    list.place(x=10, y=90)

    Label(voor_screen, text = "Upper Rate Limit (ppm)").place(x=15, y=135)
    url_voor = Scale(voor_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_voor.set(120)
    url_voor.place(x=15, y=155)

    Label(voor_screen, text = "Ventricular Amplitude (V)").place(x=12, y=220)
    options2 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice1 = DoubleVar()
    choice1.set(options2[0])
    list1 = ttk.Combobox(voor_screen, value= options2)
    list1.current(50)
    list1.bind("<<ComboboxSelected>>")
    list1.place(x=10, y=250)

    Label(voor_screen, text = "Ventricular Pulse Width (ms)").place(x=12, y=295)
    options3 = [
        "1","2","3","4","5","6","7","8","9","10", "11","12","13","14","15","16","17","18","19","20", "21","22","23","24","25","26","27","28","29","30"
    ]
    choice2 = DoubleVar()
    choice2.set(options3[0])
    list2 = ttk.Combobox(voor_screen, value= options3)
    list2.current(0)
    list2.bind("<<ComboboxSelected>>")
    list2.place(x=12, y=325)

    Label(voor_screen, text = "Maximum Sensor Rate (ppm)").place(x=12, y=370)
    msr_voor = Scale(voor_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    msr_voor.set(120)
    msr_voor.place(x=12, y=390)

    Label(voor_screen, text = "Activity Threshold").place(x=220, y=60)
    options4 = ["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]
    choice3 = DoubleVar()
    choice3.set(options4[0])
    list3 = ttk.Combobox(voor_screen, value= options4)
    list3.current(3)
    list3.bind("<<ComboboxSelected>>")
    list3.place(x=220, y=90)

    Label(voor_screen, text = "Reaction Time (sec)").place(x=220, y=135)
    reactiont_voor = Scale(voor_screen, from_=10, to =50, resolution=10, orient=HORIZONTAL)
    reactiont_voor.set(30)
    reactiont_voor.place(x=220, y=155)

    Label(voor_screen, text = "Response Factor").place(x=220, y=220)
    responsef_voor = Scale(voor_screen, from_=1, to =16, resolution=1, orient=HORIZONTAL)
    responsef_voor.set(8)
    responsef_voor.place(x=220, y=240)

    Label(voor_screen, text = "Recovery Time (min)").place(x=220, y=305)
    recoveryt_voor = Scale(voor_screen, from_=2, to =16, resolution=1, orient=HORIZONTAL)
    recoveryt_voor.set(5)
    recoveryt_voor.place(x=220, y=325)

    def show():
        global lrl_voor
        global va_voor
        global vpw_voor
        global at_voor
        
        lrl_voor = list.get()
        va_voor = list1.get()
        vpw_voor = list2.get()
        at_voor = list3.get()

        if (int(lrl_voor) > url_voor.get()):
            messagebox.showerror('Error', 'LRL is higher than URL')
        else:    
            set_values()
            print("The values for VOOR")
            print("LOWER RATE LIMIT:", lrl_voor)
            print("UPPER RATE LIMIT:", url_voor.get())
            print("VENTRICULAR AMPLITUDE:", va_voor)
            print("VENTRICULAR PULSE WIDTH:", vpw_voor)
            print("MAXIMUM SENSOR RATE:", msr_voor.get())
            print("ACTIVITY THRESHOLD:", at_voor)
            print("REACTION TIME:", reactiont_voor.get())
            print("RESPONSE FACTOR:", responsef_voor.get())
            print("RECOVERY TIME:", recoveryt_voor.get())
            print("-------------------------------------------------------------------")

    Button(voor_screen, text = "Save", width="5", height = "1", command = show).place(x=190, y=395)
    Label(voor_screen, text = "").pack()
    Button(voor_screen, text = "Load", width="5", height = "1", command = access_val).place(x=250, y=395)
    Label(voor_screen, text = "").pack()
    Button(voor_screen, text = "Back", width="5", height = "1", command = destroy_voor).place(x=310, y=395)
    Label(voor_screen, text = "Current User Logged In: %s" % (username_info_login)).place(x=12, y=440)

##############################################################################################################################################################################################    
def aoor():
    modes_screen.destroy()

    global aoor_screen
    aoor_screen = Toplevel(welcome_screen)
    aoor_screen.geometry("400x470+500+100")
    aoor_screen.title("AOOR")

    global url_aoor
    global msr_aoor
    global reactiont_aoor
    global responsef_aoor
    global recoveryt_aoor
    
    global modeSet
    modeSet = 'AOOR'

    Label(aoor_screen, text = "Set the details below", font = ("Calibri", 13)).pack()
    Label(aoor_screen, text = "").pack()

    Label(aoor_screen, text = "Lower Rate Limit (ppm)").place(x=15, y=60)
    options = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
    ]
    choice = DoubleVar()
    choice.set(options[0])
    list = ttk.Combobox(aoor_screen, value= options)
    list.current(14)
    list.bind("<<ComboboxSelected>>")
    list.place(x=10, y=90)

    Label(aoor_screen, text = "Upper Rate Limit (ppm)").place(x=15, y=135)
    url_aoor = Scale(aoor_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_aoor.set(120)
    url_aoor.place(x=15, y=155)

    Label(aoor_screen, text = "Atrial Amplitude (V)").place(x=12, y=220)
    options2 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice1 = DoubleVar()
    choice1.set(options2[0])
    list1 = ttk.Combobox(aoor_screen, value= options2)
    list1.current(50)
    list1.bind("<<ComboboxSelected>>")
    list1.place(x=10, y=250)

    Label(aoor_screen, text = "Atrial Pulse Width (ms)").place(x=12, y=295)
    options3 = [
        "1","2","3","4","5","6","7","8","9","10", "11","12","13","14","15","16","17","18","19","20", "21","22","23","24","25","26","27","28","29","30"
    ]
    choice2 = DoubleVar()
    choice2.set(options3[0])
    list2 = ttk.Combobox(aoor_screen, value= options3)
    list2.current(0)
    list2.bind("<<ComboboxSelected>>")
    list2.place(x=12, y=325)

    Label(aoor_screen, text = "Maximum Sensor Rate (ppm)").place(x=12, y=370)
    msr_aoor = Scale(aoor_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    msr_aoor.set(120)
    msr_aoor.place(x=12, y=390)

    Label(aoor_screen, text = "Activity Threshold").place(x=220, y=60)
    options4 = ["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]
    choice3 = DoubleVar()
    choice3.set(options4[0])
    list3 = ttk.Combobox(aoor_screen, value= options4)
    list3.current(3)
    list3.bind("<<ComboboxSelected>>")
    list3.place(x=220, y=90)

    Label(aoor_screen, text = "Reaction Time (sec)").place(x=220, y=135)
    reactiont_aoor = Scale(aoor_screen, from_=10, to =50, resolution=10, orient=HORIZONTAL)
    reactiont_aoor.set(30)
    reactiont_aoor.place(x=220, y=155)

    Label(aoor_screen, text = "Response Factor").place(x=220, y=220)
    responsef_aoor = Scale(aoor_screen, from_=1, to =16, resolution=1, orient=HORIZONTAL)
    responsef_aoor.set(8)
    responsef_aoor.place(x=220, y=240)

    Label(aoor_screen, text = "Recovery Time (min)").place(x=220, y=305)
    recoveryt_aoor = Scale(aoor_screen, from_=2, to =16, resolution=1, orient=HORIZONTAL)
    recoveryt_aoor.set(5)
    recoveryt_aoor.place(x=220, y=325)

    def show():
        global lrl_aoor
        global aa_aoor
        global apw_aoor
        global at_aoor
        
        lrl_aoor = list.get()
        aa_aoor = list1.get()
        apw_aoor = list2.get()
        at_aoor = list3.get()

        if (int(lrl_aoor) > url_aoor.get()):
            messagebox.showerror('Error', 'LRL is higher than URL')
        else:    
            set_values()
            print("The values for AOOR")
            print("LOWER RATE LIMIT:", lrl_aoor)
            print("UPPER RATE LIMIT:", url_aoor.get())
            print("ATRIAL AMPLITUDE:", aa_aoor)
            print("ATRIAL PULSE WIDTH:", apw_aoor)
            print("MAXIMUM SENSOR RATE:", msr_aoor.get())
            print("ACTIVITY THRESHOLD:", at_aoor)
            print("REACTION TIME:", reactiont_aoor.get())
            print("RESPONSE FACTOR:", responsef_aoor.get())
            print("RECOVERY TIME:", recoveryt_aoor.get())
            print("-------------------------------------------------------------------")

    Button(aoor_screen, text = "Save", width="5", height = "1", command = show).place(x=190, y=395)
    Label(aoor_screen, text = "").pack()
    Button(aoor_screen, text = "Load", width="5", height = "1", command = access_val).place(x=250, y=395)
    Label(aoor_screen, text = "").pack()
    Button(aoor_screen, text = "Back", width="5", height = "1", command = destroy_aoor).place(x=310, y=395)
    Label(aoor_screen, text = "Current User Logged In: %s" % (username_info_login)).place(x=12, y=440)
##############################################################################################################################################################################################
def vvir():
    modes_screen.destroy()

    global vvir_screen
    vvir_screen = Toplevel(welcome_screen)
    vvir_screen.geometry("400x630+500+5")
    vvir_screen.title("VVIR")

    global url_vvir
    global vrp_vvir
    global rs_vvir
    global msr_vvir
    global reactiont_vvir
    global responsef_vvir
    global recoveryt_vvir

    global modeSet
    modeSet = 'VVIR'

    Label(vvir_screen, text = "Set the details below", font = ("Calibri", 13)).pack()
    Label(vvir_screen, text = "").pack()

    Label(vvir_screen, text = "Lower Rate Limit (ppm)").place(x=15, y=60)
    options = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
    ]
    choice = DoubleVar()
    choice.set(options[0])
    list = ttk.Combobox(vvir_screen, value= options)
    list.current(14)
    list.bind("<<ComboboxSelected>>")
    list.place(x=10, y=90)

    Label(vvir_screen, text = "Upper Rate Limit (ppm)").place(x=15, y=135)
    url_vvir = Scale(vvir_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_vvir.set(120)
    url_vvir.place(x=15, y=155)

    Label(vvir_screen, text = "Ventricular Amplitude (V)").place(x=12, y=220)
    options1 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice1 = DoubleVar()
    choice1.set(options1[0])
    list1 = ttk.Combobox(vvir_screen, value= options1)
    list1.current(50)
    list1.bind("<<ComboboxSelected>>")
    list1.place(x=10, y=250)

    Label(vvir_screen, text = "Ventricular Pulse Width (ms)").place(x=12, y=295)
    options2 = [
        "1","2","3","4","5","6","7","8","9","10", "11","12","13","14","15","16","17","18","19","20", "21","22","23","24","25","26","27","28","29","30"
    ]
    choice2 = DoubleVar()
    choice2.set(options2[0])
    list2 = ttk.Combobox(vvir_screen, value= options2)
    list2.current(0)
    list2.bind("<<ComboboxSelected")
    list2.place(x=12, y=325)

    Label(vvir_screen, text = "Ventricular sensitivity (V)").place(x=12, y=370)
    options3 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice3 = DoubleVar()
    choice3.set(options3[0])
    list3 = ttk.Combobox(vvir_screen, value= options3)
    list3.current()
    list3.bind("<<ComboboxSelected>>")
    list3.place(x=12, y=400)

    Label(vvir_screen, text = "Ventricular Refractory Period (ms)").place(x=12, y=445)
    vrp_vvir = Scale(vvir_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    vrp_vvir.set(320)
    vrp_vvir.place(x=12, y=475)

    Label(vvir_screen, text = "Hysteresis ").place(x=12, y=540)
    options4 = [
        "OFF","same as LRL",
    ]
    choice4 = StringVar()
    choice4.set(options4[0])
    list4 = ttk.Combobox(vvir_screen, value= options4)
    list4.current(0)
    list4.bind("<<ComboboxSelected>>")
    list4.place(x=12, y=560)

    Label(vvir_screen, text = "Rate smoothing").place(x=220, y=60)
    rs_vvir = Scale(vvir_screen, from_=0, to =25, resolution=3.07, orient=HORIZONTAL)
    rs_vvir.place(x=220, y=80)

    Label(vvir_screen, text = "Maximum Sensor Rate (ppm)").place(x=220, y=145)
    msr_vvir = Scale(vvir_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    msr_vvir.set(120)
    msr_vvir.place(x=220, y=165)

    Label(vvir_screen, text = "Activity Threshold").place(x=220, y=230)
    options5 = ["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]
    choice5 = DoubleVar()
    choice5.set(options5[0])
    list5 = ttk.Combobox(vvir_screen, value= options5)
    list5.current(3)
    list5.bind("<<ComboboxSelected>>")
    list5.place(x=220, y=250)

    Label(vvir_screen, text = "Reaction Time (sec)").place(x=220, y=295)
    reactiont_vvir = Scale(vvir_screen, from_=10, to =50, resolution=10, orient=HORIZONTAL)
    reactiont_vvir.set(30)
    reactiont_vvir.place(x=220, y=315)

    Label(vvir_screen, text = "Response Factor").place(x=220, y=380)
    responsef_vvir = Scale(vvir_screen, from_=1, to =16, resolution=1, orient=HORIZONTAL)
    responsef_vvir.set(8)
    responsef_vvir.place(x=220, y=400)

    Label(vvir_screen, text = "Recovery Time (min)").place(x=220, y=465)
    recoveryt_vvir = Scale(vvir_screen, from_=2, to =16, resolution=1, orient=HORIZONTAL)
    recoveryt_vvir.set(5)
    recoveryt_vvir.place(x=220, y=485)

    def show():

        global lrl_vvir
        global va_vvir
        global vpw_vvir
        global vs_vvir
        global hysteresis_vvir
        global at_vvir

        lrl_vvir = list.get()
        va_vvir = list1.get()
        vpw_vvir = list2.get()
        vs_vvir = list3.get()
        hysteresis_vvir = list4.get()
        at_vvir = list5.get()
        if (int(lrl_vvir) > url_vvir.get()):
            messagebox.showerror('Error', 'LRL is higher than URL')
        elif ((float(60000/int(lrl_vvir)) - float(vpw_vvir)) < float(vrp_vvir.get())):
            messagebox.showerror('Error', 'VRP cant be greater than 60000/LRL - PW!')
        else: 
            set_values()
            print("The values for VVIR")
            print("LOWER RATE LIMIT:", lrl_vvir)
            print("UPPER RATE LIMIT:", url_vvir.get())
            print("VENTRICULAR AMPLITUDE:", va_vvir)
            print("VENTRICULAR PULSE WIDTH:", vpw_vvir)
            print("VENTRICULAR SENSITIVITY:", vs_vvir)
            print("VENTRICULAR REFRACTORY PERIOD:", vrp_vvir.get())
            print("HYSTERESIS:", hysteresis_vvir)
            print("RATE SMOOTHING:", rs_vvir.get())
            print("MAXIMUM SENSOR RATE:", msr_vvir.get())
            print("ACTIVITY THRESHOLD:", at_vvir)
            print("REACTION TIME:", reactiont_vvir.get())
            print("RESPONSE FACTOR:", responsef_vvir.get())
            print("RECOVERY TIME:", recoveryt_vvir.get())
            print("-------------------------------------------------------------------")

    Button(vvir_screen, text = "Save", width="5", height = "1", command = show).place(x=190, y=555)
    Label(vvir_screen, text = "").pack()
    Button(vvir_screen, text = "Load", width="5", height = "1", command = access_val).place(x=250, y=555)
    Label(vvir_screen, text = "").pack()
    Button(vvir_screen, text = "Back", width="5", height = "1", command = destroy_vvir).place(x=310, y=555)
    Label(vvir_screen, text = "Current User Logged In: %s" % (username_info_login)).place(x=12, y=600)
##############################################################################################################################################################################################
def aair():  
    modes_screen.destroy()

    global aair_screen
    aair_screen = Toplevel(welcome_screen)
    aair_screen.geometry("400x700+500+5")
    aair_screen.title("AAIR")

    global url_aair
    global arp_aair
    global pvarp_aair
    global rs_aair
    global msr_aair
    global reactiont_aair
    global responsef_aair
    global recoveryt_aair

    global modeSet
    modeSet = 'AAIR'

    Label(aair_screen, text = "Set the details below", font = ("Calibri", 13)).pack()
    Label(aair_screen, text = "").pack()

    Label(aair_screen, text = "Lower Rate Limit (ppm)").place(x=15, y=60)
    options = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
    ]
    choice = DoubleVar()
    choice.set(options[0])
    list = ttk.Combobox(aair_screen, value= options)
    list.current(14)
    list.bind("<<ComboboxSelected>>")
    list.place(x=10, y=90)

    Label(aair_screen, text = "Upper Rate Limit (ppm)").place(x=15, y=135)
    url_aair = Scale(aair_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_aair.set(120)
    url_aair.place(x=15, y=155)

    Label(aair_screen, text = "Atrial Amplitude (V)").place(x=12, y=220)
    options1 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice1 = DoubleVar()
    choice1.set(options1[0])
    list1 = ttk.Combobox(aair_screen, value= options1)
    list1.current(50)
    list1.bind("<<ComboboxSelected>>")
    list1.place(x=10, y=250)

    Label(aair_screen, text = "Atrial Pulse Width (ms)").place(x=12, y=295)
    options2 = [
        "1","2","3","4","5","6","7","8","9","10", "11","12","13","14","15","16","17","18","19","20", "21","22","23","24","25","26","27","28","29","30"
    ]
    choice2 = DoubleVar()
    choice2.set(options2[0])
    list2 = ttk.Combobox(aair_screen, value= options2)
    list2.current(0)
    list2.bind("<<ComboboxSelected")
    list2.place(x=12, y=325)

    Label(aair_screen, text = "Atrial sensitivity (V)").place(x=12, y=370)
    options3 = [
        "0","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6",
        "1.7","1.8","1.9","2.0","2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.3",
        "3.4","3.5","3.6","3.7","3.8","3.9","4.0","4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","5.0"
    ]
    choice3 = DoubleVar()
    choice3.set(options3[0])
    list3 = ttk.Combobox(aair_screen, value= options3)
    list3.current()
    list3.bind("<<ComboboxSelected>>")
    list3.place(x=12, y=400)

    Label(aair_screen, text = "Atrial Refractory Period (ms)").place(x=12, y=445)
    arp_aair = Scale(aair_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    arp_aair.set(250)
    arp_aair.place(x=12, y=475)

    Label(aair_screen, text = "PVARP (ms)").place(x=12, y=540)
    pvarp_aair = Scale(aair_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    pvarp_aair.set(250)
    pvarp_aair.place(x=12, y=560)

    Label(aair_screen, text = "Hysteresis ").place(x=220, y=60)
    options4 = [
        "OFF","same as LRL",
    ]
    choice4 = StringVar()
    choice4.set(options4[0])
    list4 = ttk.Combobox(aair_screen, value= options4)
    list4.current(0)
    list4.bind("<<ComboboxSelected>>")
    list4.place(x=220, y=90)

    Label(aair_screen, text = "Rate smoothing").place(x=220, y=135)
    rs_aair = Scale(aair_screen, from_=0, to =25, resolution=3.07, orient=HORIZONTAL)
    rs_aair.place(x=220, y=155)

    Label(aair_screen, text = "Maximum Sensor Rate (ppm)").place(x=220, y=220)
    msr_aair = Scale(aair_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    msr_aair.set(120)
    msr_aair.place(x=220, y=240)

    Label(aair_screen, text = "Activity Threshold").place(x=220, y=305)
    options5 = ["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]
    choice5 = DoubleVar()
    choice5.set(options5[0])
    list5 = ttk.Combobox(aair_screen, value= options5)
    list5.current(3)
    list5.bind("<<ComboboxSelected>>")
    list5.place(x=220, y=335)

    Label(aair_screen, text = "Reaction Time (sec)").place(x=220, y=380)
    reactiont_aair = Scale(aair_screen, from_=10, to =50, resolution=10, orient=HORIZONTAL)
    reactiont_aair.set(30)
    reactiont_aair.place(x=220, y=400)

    Label(aair_screen, text = "Response Factor").place(x=220, y=465)
    responsef_aair = Scale(aair_screen, from_=1, to =16, resolution=1, orient=HORIZONTAL)
    responsef_aair.set(8)
    responsef_aair.place(x=220, y=485)

    Label(aair_screen, text = "Recovery Time (min)").place(x=220, y=550)
    recoveryt_aair = Scale(aair_screen, from_=2, to =16, resolution=1, orient=HORIZONTAL)
    recoveryt_aair.set(5)
    recoveryt_aair.place(x=220, y=570)

    def show():

        global lrl_aair
        global aa_aair
        global apw_aair
        global as_aair
        global hysteresis_aair
        global at_aair

        lrl_aair = list.get()
        aa_aair = list1.get()
        apw_aair = list2.get()
        as_aair = list3.get()
        hysteresis_aair = list4.get()
        at_aair = list5.get()
        if (int(lrl_aair) > url_aair.get()):
            messagebox.showerror('Error', 'LRL is higher than URL')
        elif ((float(60000/int(lrl_aair)) - float(apw_aair)) < float(arp_aair.get())):
            messagebox.showerror('Error', 'VRP cant be greater than 60000/LRL - PW!')
        else: 
            set_values()
            print("The values for AAIR")
            print("LOWER RATE LIMIT:", lrl_aair)
            print("UPPER RATE LIMIT:", url_aair.get())
            print("ATRIAL AMPLITUDE:", aa_aair)
            print("ATRIAL PULSE WIDTH:", apw_aair)
            print("ATRIAL SENSITIVITY:", as_aair)
            print("ATRIAL REFRACTORY PERIOD:", arp_aair.get())
            print("POST VENTRICULAR ATRIAL REFRACTORY PERIOD:", pvarp_aair.get())
            print("HYSTERESIS:", hysteresis_aair)
            print("RATE SMOOTHING:", rs_aair.get())
            print("MAXIMUM SENSOR RATE:", msr_aair.get())
            print("ACTIVITY THRESHOLD:", at_aair)
            print("REACTION TIME:", reactiont_aair.get())
            print("RESPONSE FACTOR:", responsef_aair.get())
            print("RECOVERY TIME:", recoveryt_aair.get())
            print("-------------------------------------------------------------------")

    Button(aair_screen, text = "Save", width="5", height = "1", command = show).place(x=70, y=640)
    Label(aair_screen, text = "").pack()
    Button(aair_screen, text = "Load", width="5", height = "1", command = access_val).place(x=175, y=640)
    Label(aair_screen, text = "").pack()
    Button(aair_screen, text = "Back", width="5", height = "1", command = destroy_aair).place(x=280, y=640)
    Label(aair_screen, text = "Current User Logged In: %s" % (username_info_login)).place(x=12, y=675)
##############################################################################################################################################################################################
def destroy_voo():
    voo_screen.destroy()
    modes()

def destroy_aoo():
    aoo_screen.destroy()
    modes()

def destroy_vvi():
    vvi_screen.destroy()
    modes()

def destroy_aai():
    aai_screen.destroy()
    modes()

def destroy_voor():
    voor_screen.destroy()
    modes()

def destroy_aoor():
    aoor_screen.destroy()
    modes()

def destroy_vvir():
    vvir_screen.destroy()
    modes()

def destroy_aair():
    aair_screen.destroy()
    modes()
##############################################################################################################################################################################################
def set_values():
    if modeSet=='VOO':
        VOO_LRL=lrl_voo
        VOO_URL=str(url_voo.get())
        VOO_VA=va_voo
        VOO_VPW=vpw_voo
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                i["VOO"]["LRL"] = VOO_LRL
                i["VOO"]["URL"] = VOO_URL
                i["VOO"]["VA"] = VOO_VA
                i["VOO"]["VPW"] = VOO_VPW
        open("data.json", "w").write(
            json.dumps(data, indent=4, separators=(',', ': '))
        )
    elif modeSet=='AOO':
        AOO_LRL= lrl_aoo
        AOO_URL= str(url_aoo.get())
        AOO_AA= aa_aoo
        AOO_APW= apw_aoo
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                i["AOO"]["LRL"] = AOO_LRL
                i["AOO"]["URL"] = AOO_URL
                i["AOO"]["AA"] = AOO_AA
                i["AOO"]["APW"] = AOO_APW
        open("data.json", "w").write(
            json.dumps(data, indent=4, separators=(',', ': '))
        )
    elif modeSet=='VVI':
        VVI_LRL=lrl_vvi
        VVI_URL=str(url_vvi.get())
        VVI_VA=va_vvi
        VVI_VPW=vpw_vvi
        VVI_VRP=str(vrp_vvi.get())
        VVI_VS=vs_vvi
        VVI_H=hysteresis_vvi
        VVI_S=str(rs_vvi.get())

        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                i["VVI"]["LRL"] = VVI_LRL
                i["VVI"]["URL"] = VVI_URL
                i["VVI"]["VA"] = VVI_VA
                i["VVI"]["VPW"] = VVI_VPW
                i["VVI"]["VRP"] = VVI_VRP
                i["VVI"]["VS"] = VVI_VS
                i["VVI"]["H"] = VVI_H
                i["VVI"]["S"] = VVI_S
        open("data.json", "w").write(
            json.dumps(data, indent=4, separators=(',', ': '))
        )
    elif modeSet=='AAI':
        AAI_LRL=lrl_aai
        AAI_URL=str(url_aai.get())
        AAI_AA=aa_aai
        AAI_APW=apw_aai
        AAI_ARP=str(arp_aai.get())
        AAI_AS=as_aai
        AAI_PVARP=str(pvarp_aai.get())
        AAI_H=hysteresis_aai
        AAI_S=str(rs_aai.get())

        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                i["AAI"]["LRL"] = AAI_LRL
                i["AAI"]["URL"] = AAI_URL
                i["AAI"]["AA"] = AAI_AA
                i["AAI"]["APW"] = AAI_APW
                i["AAI"]["ARP"] = AAI_ARP
                i["AAI"]["AS"] = AAI_AS
                i["AAI"]["PVARP"] = AAI_PVARP
                i["AAI"]["H"] = AAI_H
                i["AAI"]["S"] = AAI_S
        open("data.json", "w").write(
            json.dumps(data, indent=4, separators=(',', ': '))
        )
    elif modeSet=='VOOR':
        VOOR_LRL=lrl_voor
        VOOR_URL=str(url_voor.get())
        VOOR_VA=va_voor
        VOOR_VPW=vpw_voor
        VOOR_MSR=str(msr_voor.get())
        VOOR_AT= at_voor
        VOOR_REACTION=str(reactiont_voor.get())
        VOOR_RF=str(responsef_voor.get())
        VOOR_RECOVERY=str(recoveryt_voor.get())
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                i["VOOR"]["LRL"] = VOOR_LRL
                i["VOOR"]["URL"] = VOOR_URL
                i["VOOR"]["VA"] = VOOR_VA
                i["VOOR"]["VPW"] = VOOR_VPW
                i["VOOR"]["MSR"] = VOOR_MSR
                i["VOOR"]["AT"] = VOOR_AT
                i["VOOR"]["REACTION TIME"] = VOOR_REACTION
                i["VOOR"]["RESPONSE FACTOR"] = VOOR_RF
                i["VOOR"]["RECOVERY TIME"] = VOOR_RECOVERY
        open("data.json", "w").write(
            json.dumps(data, indent=4, separators=(',', ': '))
        )
    elif modeSet=='AOOR':
        AOOR_LRL= lrl_aoor
        AOOR_URL= str(url_aoor.get())
        AOOR_AA= aa_aoor
        AOOR_APW= apw_aoor
        AOOR_MSR=str(msr_aoor.get())
        AOOR_AT= at_aoor
        AOOR_REACTION=str(reactiont_aoor.get())
        AOOR_RF=str(responsef_aoor.get())
        AOOR_RECOVERY=str(recoveryt_aoor.get())
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                i["AOOR"]["LRL"] = AOOR_LRL
                i["AOOR"]["URL"] = AOOR_URL
                i["AOOR"]["AA"] = AOOR_AA
                i["AOOR"]["APW"] = AOOR_APW
                i["AOOR"]["MSR"] = AOOR_MSR
                i["AOOR"]["AT"] = AOOR_AT
                i["AOOR"]["REACTION TIME"] = AOOR_REACTION
                i["AOOR"]["RESPONSE FACTOR"] = AOOR_RF
                i["AOOR"]["RECOVERY TIME"] = AOOR_RECOVERY
        open("data.json", "w").write(
            json.dumps(data, indent=4, separators=(',', ': '))
        )
    elif modeSet=='VVIR':
        VVIR_LRL=lrl_vvir
        VVIR_URL=str(url_vvir.get())
        VVIR_VA=va_vvir
        VVIR_VPW=vpw_vvir
        VVIR_VRP=str(vrp_vvir.get())
        VVIR_VS=vs_vvir
        VVIR_H=hysteresis_vvir
        VVIR_S=str(rs_vvir.get())
        VVIR_MSR=str(msr_vvir.get())
        VVIR_AT= at_vvir
        VVIR_REACTION=str(reactiont_vvir.get())
        VVIR_RF=str(responsef_vvir.get())
        VVIR_RECOVERY=str(recoveryt_vvir.get())
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                i["VVIR"]["LRL"] = VVIR_LRL
                i["VVIR"]["URL"] = VVIR_URL
                i["VVIR"]["VA"] = VVIR_VA
                i["VVIR"]["VPW"] = VVIR_VPW
                i["VVIR"]["VRP"] = VVIR_VRP
                i["VVIR"]["VS"] = VVIR_VS
                i["VVIR"]["H"] = VVIR_H
                i["VVIR"]["S"] = VVIR_S
                i["VVIR"]["MSR"] = VVIR_MSR
                i["VVIR"]["AT"] = VVIR_AT
                i["VVIR"]["REACTION TIME"] = VVIR_REACTION
                i["VVIR"]["RESPONSE FACTOR"] = VVIR_RF
                i["VVIR"]["RECOVERY TIME"] = VVIR_RECOVERY
        open("data.json", "w").write(
            json.dumps(data, indent=4, separators=(',', ': '))
        )
    elif modeSet=='AAIR':
        AAIR_LRL=lrl_aair
        AAIR_URL=str(url_aair.get())
        AAIR_AA=aa_aair
        AAIR_APW=apw_aair
        AAIR_ARP=str(arp_aair.get())
        AAIR_AS=as_aair
        AAIR_PVARP=str(pvarp_aair.get())
        AAIR_H=hysteresis_aair
        AAIR_S=str(rs_aair.get())
        AAIR_MSR=str(msr_aair.get())
        AAIR_AT= at_aair
        AAIR_REACTION=str(reactiont_aair.get())
        AAIR_RF=str(responsef_aair.get())
        AAIR_RECOVERY=str(recoveryt_aair.get())
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                i["AAIR"]["LRL"] = AAIR_LRL
                i["AAIR"]["URL"] = AAIR_URL
                i["AAIR"]["AA"] = AAIR_AA
                i["AAIR"]["APW"] = AAIR_APW
                i["AAIR"]["ARP"] = AAIR_ARP
                i["AAIR"]["AS"] = AAIR_AS
                i["AAIR"]["PVARP"] = AAIR_PVARP
                i["AAIR"]["H"] = AAIR_H
                i["AAIR"]["S"] = AAIR_S
                i["AAIR"]["MSR"] = AAIR_MSR
                i["AAIR"]["AT"] = AAIR_AT
                i["AAIR"]["REACTION TIME"] = AAIR_REACTION
                i["AAIR"]["RESPONSE FACTOR"] = AAIR_RF
                i["AAIR"]["RECOVERY TIME"] = AAIR_RECOVERY
        open("data.json", "w").write(
            json.dumps(data, indent=4, separators=(',', ': '))
        )

def access_val():
    if modeSet=='VOO':
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                if i["VOO"]["LRL"] == "":
                    print("No previous parameters saved")
                    print("USER:", username_info_login)
                else:
                    VOO_LRL = i["VOO"]["LRL"]
                    VOO_URL = i["VOO"]["URL"]
                    VOO_VA = i["VOO"]["VA"]
                    VOO_VPW = i["VOO"]["VPW"]
                    print("The saved values for VOO")
                    print("USER:", username_info_login)
                    print("LOWER RATE LIMIT:", VOO_LRL)
                    print("UPPER RATE LIMIT:", VOO_URL)
                    print("VENTRICULAR AMPLITUDE:", VOO_VA)
                    print("VENTRICULAR PULSE WIDTH:", VOO_VPW)
                    print("-------------------------------------------------------------------")
    elif modeSet=='AOO':
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                if i["AOO"]["LRL"] == "":
                    print("No previous parameters saved")
                    print("USER:", username_info_login)
                else:
                    AOO_LRL = i["AOO"]["LRL"]
                    AOO_URL = i["AOO"]["URL"]
                    AOO_AA = i["AOO"]["AA"]
                    AOO_APW = i["AOO"]["APW"]  
                    print("The saved values for AOO")
                    print("USER:", username_info_login)
                    print("LOWER RATE LIMIT:", AOO_LRL)
                    print("UPPER RATE LIMIT:", AOO_URL)
                    print("ATRIAL AMPLITUDE:", AOO_AA)
                    print("ATRIAL PULSE WIDTH:", AOO_APW) 
                    print("-------------------------------------------------------------------")      
    elif modeSet=='VVI':
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                if i["VVI"]["LRL"] == "":
                    print("No previous parameters saved")
                    print("USER:", username_info_login)
                else:
                    VVI_LRL = i["VVI"]["LRL"]
                    VVI_URL = i["VVI"]["URL"]
                    VVI_VA = i["VVI"]["VA"]
                    VVI_VPW = i["VVI"]["VPW"]
                    VVI_VRP = i["VVI"]["VRP"]
                    VVI_VS = i["VVI"]["VS"]
                    VVI_H = i["VVI"]["H"]
                    VVI_S = i["VVI"]["S"]
                    print("The saved values for VVI")
                    print("USER:", username_info_login)
                    print("LOWER RATE LIMIT:", VVI_LRL)
                    print("UPPER RATE LIMIT:", VVI_URL)
                    print("VENTRICULAR AMPLITUDE:", VVI_VA)
                    print("VENTRICULAR PULSE WIDTH:", VVI_VPW)
                    print("VENTRICULAR SENSITIVITY:", VVI_VS)
                    print("VENTRICULAR REFRACTORY PERIOD:", VVI_VRP)
                    print("HYSTERESIS:", VVI_H)
                    print("RATE SMOOTHING:", VVI_S)
                    print("-------------------------------------------------------------------")
    elif modeSet=='AAI':
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                if i["AAI"]["LRL"] == "":
                    print("No previous parameters saved")
                    print("USER:", username_info_login)
                else:
                    AAI_LRL = i["AAI"]["LRL"]
                    AAI_URL = i["AAI"]["URL"]
                    AAI_AA = i["AAI"]["AA"]
                    AAI_APW = i["AAI"]["APW"]
                    AAI_ARP = i["AAI"]["ARP"]
                    AAI_AS = i["AAI"]["AS"]
                    AAI_PVARP = i["AAI"]["PVARP"]
                    AAI_H = i["AAI"]["H"]
                    AAI_S = i["AAI"]["S"]
                    print("The saved values for AAI")
                    print("USER:", username_info_login)
                    print("LOWER RATE LIMIT:", AAI_LRL)
                    print("UPPER RATE LIMIT:", AAI_URL)
                    print("ATRIAL AMPLITUDE:", AAI_AA)
                    print("ATRIAL PULSE WIDTH:", AAI_APW)
                    print("ATRIAL SENSITIVITY:", AAI_AS)
                    print("ATRIAL REFRACTORY PERIOD:", AAI_ARP)
                    print("POST VENTRICULAR ATRIAL REFRACTORY PERIOD:", AAI_PVARP)
                    print("HYSTERESIS:", AAI_H)
                    print("RATE SMOOTHING:", AAI_S)
                    print("-------------------------------------------------------------------")
    elif modeSet=='VOOR':
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                if i["VOOR"]["LRL"] == "":
                    print("No previous parameters saved")
                    print("USER:", username_info_login)
                else:
                    VOOR_LRL = i["VOOR"]["LRL"]
                    VOOR_URL = i["VOOR"]["URL"]
                    VOOR_VA = i["VOOR"]["VA"]
                    VOOR_VPW = i["VOOR"]["VPW"]
                    VOOR_MSR = i["VOOR"]["MSR"]
                    VOOR_AT = i["VOOR"]["AT"]
                    VOOR_REACTION = i["VOOR"]["REACTION TIME"]
                    VOOR_RF = i["VOOR"]["RESPONSE FACTOR"]
                    VOOR_RECOVERY = i["VOOR"]["RECOVERY TIME"]
                    print("The saved values for VOOR")
                    print("USER:", username_info_login)
                    print("LOWER RATE LIMIT:", VOOR_LRL)
                    print("UPPER RATE LIMIT:", VOOR_URL)
                    print("VENTRICULAR AMPLITUDE:", VOOR_VA)
                    print("VENTRICULAR PULSE WIDTH:", VOOR_VPW)
                    print("MAXIMUM SENSOR RATE:", VOOR_MSR)
                    print("ACTIVITY THRESHOLD:", VOOR_AT)
                    print("REACTION TIME:", VOOR_REACTION)
                    print("RESPONSE FACTOR:", VOOR_RF)
                    print("RECOVERY TIME:", VOOR_RECOVERY)
                    print("-------------------------------------------------------------------")
    elif modeSet=='AOOR':
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                if i["AOOR"]["LRL"] == "":
                    print("No previous parameters saved")
                    print("USER:", username_info_login)
                else:
                    AOOR_LRL = i["AOOR"]["LRL"]
                    AOOR_URL = i["AOOR"]["URL"]
                    AOOR_AA = i["AOOR"]["AA"]
                    AOOR_APW = i["AOOR"]["APW"]
                    AOOR_MSR = i["AOOR"]["MSR"]
                    AOOR_AT = i["AOOR"]["AT"]
                    AOOR_REACTION = i["AOOR"]["REACTION TIME"]
                    AOOR_RF = i["AOOR"]["RESPONSE FACTOR"]
                    AOOR_RECOVERY = i["AOOR"]["RECOVERY TIME"]  
                    print("The saved values for AOOR")
                    print("USER:", username_info_login)
                    print("LOWER RATE LIMIT:", AOOR_LRL)
                    print("UPPER RATE LIMIT:", AOOR_URL)
                    print("ATRIAL AMPLITUDE:", AOOR_AA)
                    print("ATRIAL PULSE WIDTH:", AOOR_APW)
                    print("MAXIMUM SENSOR RATE:", AOOR_MSR)
                    print("ACTIVITY THRESHOLD:", AOOR_AT)
                    print("REACTION TIME:", AOOR_REACTION)
                    print("RESPONSE FACTOR:", AOOR_RF)
                    print("RECOVERY TIME:", AOOR_RECOVERY) 
                    print("-------------------------------------------------------------------")      
    elif modeSet=='VVIR':
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                if i["VVIR"]["LRL"] == "":
                    print("No previous parameters saved")
                    print("USER:", username_info_login)
                else:
                    VVIR_LRL = i["VVIR"]["LRL"]
                    VVIR_URL = i["VVIR"]["URL"]
                    VVIR_VA = i["VVIR"]["VA"]
                    VVIR_VPW = i["VVIR"]["VPW"]
                    VVIR_VRP = i["VVIR"]["VRP"]
                    VVIR_VS = i["VVIR"]["VS"]
                    VVIR_H = i["VVIR"]["H"]
                    VVIR_S = i["VVIR"]["S"]
                    VVIR_MSR = i["VVIR"]["MSR"]
                    VVIR_AT = i["VVIR"]["AT"]
                    VVIR_REACTION = i["VVIR"]["REACTION TIME"]
                    VVIR_RF = i["VVIR"]["RESPONSE FACTOR"]
                    VVIR_RECOVERY = i["VVIR"]["RECOVERY TIME"]
                    print("The saved values for VVIR")
                    print("USER:", username_info_login)
                    print("LOWER RATE LIMIT:", VVIR_LRL)
                    print("UPPER RATE LIMIT:", VVIR_URL)
                    print("VENTRICULAR AMPLITUDE:", VVIR_VA)
                    print("VENTRICULAR PULSE WIDTH:", VVIR_VPW)
                    print("VENTRICULAR SENSITIVITY:", VVIR_VS)
                    print("VENTRICULAR REFRACTORY PERIOD:", VVIR_VRP)
                    print("HYSTERESIS:", VVIR_H)
                    print("RATE SMOOTHING:", VVIR_S)
                    print("MAXIMUM SENSOR RATE:", VVIR_MSR)
                    print("ACTIVITY THRESHOLD:", VVIR_AT)
                    print("REACTION TIME:", VVIR_REACTION)
                    print("RESPONSE FACTOR:", VVIR_RF)
                    print("RECOVERY TIME:", VVIR_RECOVERY)
                    print("-------------------------------------------------------------------")
    elif modeSet=='AAIR':
        f = open("data.json", "r+")
        data = json.load(f)
        for i in data:
            if i["username"] == username_info_login:
                if i["AAIR"]["LRL"] == "":
                    print("No previous parameters saved")
                    print("USER:", username_info_login)
                else:
                    AAIR_LRL = i["AAIR"]["LRL"]
                    AAIR_URL = i["AAIR"]["URL"]
                    AAIR_AA = i["AAIR"]["AA"]
                    AAIR_APW = i["AAIR"]["APW"]
                    AAIR_ARP = i["AAIR"]["ARP"]
                    AAIR_AS = i["AAIR"]["AS"]
                    AAIR_PVARP = i["AAIR"]["PVARP"]
                    AAIR_H = i["AAIR"]["H"]
                    AAIR_S = i["AAIR"]["S"]
                    AAIR_MSR = i["AAIR"]["MSR"]
                    AAIR_AT = i["AAIR"]["AT"]
                    AAIR_REACTION = i["AAIR"]["REACTION TIME"]
                    AAIR_RF = i["AAIR"]["RESPONSE FACTOR"]
                    AAIR_RECOVERY = i["AAIR"]["RECOVERY TIME"]
                    print("The saved values for AAIR")
                    print("USER:", username_info_login)
                    print("LOWER RATE LIMIT:", AAIR_LRL)
                    print("UPPER RATE LIMIT:", AAIR_URL)
                    print("ATRIAL AMPLITUDE:", AAIR_AA)
                    print("ATRIAL PULSE WIDTH:", AAIR_APW)
                    print("ATRIAL SENSITIVITY:", AAIR_AS)
                    print("ATRIAL REFRACTORY PERIOD:", AAIR_ARP)
                    print("POST VENTRICULAR ATRIAL REFRACTORY PERIOD:", AAIR_PVARP)
                    print("HYSTERESIS:", AAIR_H)
                    print("RATE SMOOTHING:", AAIR_S)
                    print("MAXIMUM SENSOR RATE:", AAIR_MSR)
                    print("ACTIVITY THRESHOLD:", AAIR_AT)
                    print("REACTION TIME:", AAIR_REACTION)
                    print("RESPONSE FACTOR:", AAIR_RF)
                    print("RECOVERY TIME:", AAIR_RECOVERY)
                    print("-------------------------------------------------------------------")

    
def egram_plot():
    egram_req = 1
    # serial_port = "COM10"

    Start = b'\x16'
    Fn_set = b'\x47'
    #test
    
    if(modeSet == 'VOO'):
        vpw =struct.pack("H", int(vpw_voo))
        mode = struct.pack("B", 1)
        lrl = struct.pack("H", int(lrl_voo))
        url = struct.pack("B", url_voo.get())
        vamp = struct.pack("f", float(va_voo))
        aamp = struct.pack("f", 0)
        apw = struct.pack("H", 0)
        vrp = struct.pack("H", 0)
        arp = struct.pack("H", 0)
        atr_sens = struct.pack("f", 0)
        vent_sens = struct.pack("f", 0)
        pvarp = struct.pack("H", 0)
        rs = struct.pack("B", 0)
        hs = struct.pack("B", 0)
    elif (modeSet == 'AOO'):
        vpw =struct.pack("H", 0)
        mode = struct.pack("B", 1)
        lrl = struct.pack("H", int(lrl_aoo))
        url = struct.pack("B", url_aoo.get())
        vamp = struct.pack("f", 0)
        aamp = struct.pack("f", float(aa_aoo))
        apw = struct.pack("H", int(apw_aoo))
        vrp = struct.pack("H", 0)
        arp = struct.pack("H", 0)
        atr_sens = struct.pack("f", 0)
        vent_sens = struct.pack("f", 0)
        pvarp = struct.pack("H", 0)
        rs = struct.pack("B", 0)
        hs = struct.pack("B", 0)
    elif (modeSet == 'AAI'):
        vpw =struct.pack("H", 0)
        mode = struct.pack("B", 4)
        lrl = struct.pack("H", int(lrl_aai))
        url = struct.pack("B", url_aai.get())
        vamp = struct.pack("f", 0)
        aamp = struct.pack("f", float(aa_aai))
        apw = struct.pack("H", int(apw_aai))
        vrp = struct.pack("H", 0)
        arp = struct.pack("H", 0)
        atr_sens = struct.pack("f", 0)
        vent_sens = struct.pack("f", 0)
        pvarp = struct.pack("H", 0)
        rs = struct.pack("B", 0)
        hs = struct.pack("B", 0)
    elif(modeSet=='VVI'):
        vpw =struct.pack("H", int(vpw_vvi))
        mode = struct.pack("B", 3)
        lrl = struct.pack("H", int(lrl_vvi))
        url = struct.pack("B", url_vvi.get())
        vamp = struct.pack("f", float(va_vvi))
        aamp = struct.pack("f", 0)
        apw = struct.pack("H", 0)
        vrp = struct.pack("H", vrp_vvi.get())
        arp = struct.pack("H", 0)
        atr_sens = struct.pack("f", 0)
        vent_sens = struct.pack("f", float(vs_vvi))
        pvarp = struct.pack("H", 0)
        rs = struct.pack("B", rs_vvi.get())
        hs = struct.pack("B", int(hysteresis_vvi))
    Signal_set = (Start + Fn_set + vpw + lrl + mode + url + vamp + aamp + apw + vrp + arp + atr_sens + vent_sens + pvarp + rs + hs)
    xs = []
    ys = []
    j=0
    
    with serial.Serial(serial_port, 115200) as pacemaker:
        pacemaker.write(Signal_set)
        time.sleep(0.5)
    print("SENDING REQUEST")
        
    style.use('fivethirtyeight')
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, j, ax1), interval=1000)
    HTML(ani.to_html5_video())
    plt.show()

def egram_stop():
    egram_req = 0
    print("STOPPING EGRAM STREAM")
    plt.close()
    
def animate(i,xs,ys,j, ax1):
    print("ANIMATE")
    serial_port= "COM10"
    with serial.Serial(serial_port,115200) as pacemaker:
        data = pacemaker.read(9)
        egram_data =  struct.unpack("d", data[0:8])[0]
    print("EGRAM_DATA: ", egram_data)
    j=j+1
    xs.append(j)
    ys.append(egram_data)
    xs[-20:]
    ys[-20:]
    ax1.clear()
    ax1.plot(ys,xs)
        
        
        
    
        
main_screen()