import ast
import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Welcome Screen
def main_screen():
    global welcome_screen
    welcome_screen = Tk()
    welcome_screen.geometry("400x300+500+250")
    welcome_screen.title("Pacemaker DCM")

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
                                "AOO": {
                                    "LRL": "",
                                    "URL": "",
                                    "AA": "",
                                    "APW": ""
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
                                "VOO": {
                                    "LRL": "",
                                    "URL": "",
                                    "VA": "",
                                    "VPW": ""
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
                            "AOO": {
                                "LRL": "",
                                "URL": "",
                                "AA": "",
                                "APW": ""
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
                            "VOO": {
                                "LRL": "",
                                "URL": "",
                                "VA": "",
                                "VPW": ""
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
    messagebox.showinfo('Success', 'You have been successfully connected!')
    connect_screen.destroy()
    modes()


# Modes
def modes():
    global modes_screen
    modes_screen = Toplevel(welcome_screen)
    modes_screen.geometry("400x350+500+250")
    modes_screen.title("Modes")

    

    Label(modes_screen, text = "Please choose one of the following modes", bg="grey", width="300", height = "2", font = ("Calibri", 13)).pack()

    Label(modes_screen, text = "").pack()

    Button(modes_screen, text = "VOO", width="30", height = "2", command = voo).pack()

    Label(modes_screen, text = "").pack()

    Button(modes_screen, text = "AOO", width="30", height = "2", command = aoo).pack()

    Label(modes_screen, text = "").pack()

    Button(modes_screen, text = "VVI", width="30", height = "2", command = vvi).pack()

    Label(modes_screen, text = "").pack()

    Button(modes_screen, text = "AAI", width="30", height = "2", command = aai).pack()

    Label(modes_screen, text = "").pack()

    Label(modes_screen, text = "Current User Logged In: %s" % (username_info_login)).pack(side=LEFT)

##############################################################################################################################################################################################
def voo():
    modes_screen.destroy()

    global voo_screen
    voo_screen = Toplevel(welcome_screen)
    voo_screen.geometry("400x470+500+100")
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
        "0","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9","2.0",
        "2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.5","4.0","4.5","5.0","5.5",
        "6.0","6.5","7.0","7.5",
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
        "0.05","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9",
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

        set_values()
        print("The values for VOO")
        print("LOWER RATE LIMIT:", lrl_voo)
        print("UPPER RATE LIMIT:", url_voo.get())
        print("VENTRICULAR AMPLITUDE:", va_voo)
        print("VENTRICULAR PULSE WIDTH:", vpw_voo)
        print("-------------------------------------------------------------------")

    Button(voo_screen, text = "Save", width="5", height = "1", command = show).pack()
    Label(voo_screen, text = "").pack()
    Button(voo_screen, text = "Load", width="5", height = "1", command = access_val).pack()
    Label(voo_screen, text = "").pack()
    Button(voo_screen, text = "Back", width="5", height = "1", command = destroy_voo).pack()
    Label(voo_screen, text = "Current User Logged In: %s" % (username_info_login)).pack(side=LEFT)
##############################################################################################################################################################################################
def aoo():
    modes_screen.destroy()

    global aoo_screen
    aoo_screen = Toplevel(welcome_screen)
    aoo_screen.geometry("400x470+500+100")
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
        "0","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9","2.0",
        "2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.5","4.0","4.5","5.0","5.5",
        "6.0","6.5","7.0","7.5",
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
        "0.05","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9",
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

        set_values()
        print("The values for AOO")
        print("LOWER RATE LIMIT:", lrl_aoo)
        print("UPPER RATE LIMIT:", url_aoo.get())
        print("ATRIAL AMPLITUDE:", aa_aoo)
        print("ATRIAL PULSE WIDTH:", apw_aoo)
        print("-------------------------------------------------------------------")

    Button(aoo_screen, text = "Save", width="5", height = "1", command = show).pack()
    Label(aoo_screen, text = "").pack()
    Button(aoo_screen, text = "Load", width="5", height = "1", command = access_val).pack()
    Label(aoo_screen, text = "").pack()
    Button(aoo_screen, text = "Back", width="5", height = "1", command = destroy_aoo).pack()
    Label(aoo_screen, text = "Current User Logged In: %s" % (username_info_login)).pack(side=LEFT)
##############################################################################################################################################################################################
def vvi():
    modes_screen.destroy()

    global vvi_screen
    vvi_screen = Toplevel(welcome_screen)
    vvi_screen.geometry("400x752+500+20")
    vvi_screen.title("VVI")

    global url_vvi
    global vrp_vvi
    global rs_vvi

    global modeSet
    modeSet = 'VVI'

    Label(vvi_screen, text = "Set the details below", font = ("Calibri", 13)).pack()
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Lower Rate Limit (ppm)").pack()
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
    list.pack() 
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Upper Rate Limit (ppm)").pack()
    url_vvi = Scale(vvi_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_vvi.set(120)
    url_vvi.pack()
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Ventricular Amplitude (V)").pack()
    options1 = [
        "0","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9","2.0",
        "2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","3.0","3.1","3.2","3.5","4.0","4.5","5.0","5.5",
        "6.0","6.5","7.0","7.5",
    ]
    choice1 = DoubleVar()
    choice1.set(options1[0])
    list1 = ttk.Combobox(vvi_screen, value= options1)
    list1.current(29)
    list1.bind("<<ComboboxSelected>>")
    list1.pack()
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Ventricular Pulse Width (ms)").pack()
    options2 = [
        "0.05","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9",
    ]
    choice2 = DoubleVar()
    choice2.set(options2[0])
    list2 = ttk.Combobox(vvi_screen, value= options2)
    list2.current(4)
    list2.bind("<<ComboboxSelected")
    list2.pack()
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Ventricular sensitivity (mV)").pack()
    options3 = [
        "0.25","0.5","0.75","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5","6.0","6.5","7.0","7.5","8.0","8.5","9.0","9.5","10.0",
    ]
    choice3 = DoubleVar()
    choice3.set(options3[0])
    list3 = ttk.Combobox(vvi_screen, value= options3)
    list3.current(6)
    list3.bind("<<ComboboxSelected>>")
    list3.pack()
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Ventricular Refractory Period (ms)").pack()
    vrp_vvi = Scale(vvi_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    vrp_vvi.set(320)
    vrp_vvi.pack()
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Hysteresis ").pack()
    options4 = [
        "OFF","same as LRL",
    ]
    choice4 = StringVar()
    choice4.set(options4[0])
    list4 = ttk.Combobox(vvi_screen, value= options4)
    list4.current(0)
    list4.bind("<<ComboboxSelected>>")
    list4.pack()
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Rate smoothing").pack()
    rs_vvi = Scale(vvi_screen, from_=0, to =25, resolution=3.07, orient=HORIZONTAL)
    rs_vvi.pack()
    Label(vvi_screen, text = "").pack()

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
        hysteresis_vvi = list4.get()

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

    Button(vvi_screen, text = "Save", width="5", height = "1", command = show).pack()
    Label(vvi_screen, text = "").pack()
    Button(vvi_screen, text = "Load", width="5", height = "1", command = access_val).pack()
    Label(vvi_screen, text = "").pack()
    Button(vvi_screen, text = "Back", width="5", height = "1", command = destroy_vvi).pack()
    Label(vvi_screen, text = "Current User Logged In: %s" % (username_info_login)).pack(side=LEFT)
##############################################################################################################################################################################################
def aai():
    modes_screen.destroy()

    global aai_screen
    aai_screen = Toplevel(welcome_screen)
    aai_screen.geometry("400x764+500+5")
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

    Label(aai_screen, text = "Lower Rate Limit (ppm)").pack()
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
    list.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Upper Rate Limit (ppm)").pack()
    url_aai = Scale(aai_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
    url_aai.set(120)
    url_aai.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Atrial Amplitude (V)").pack()
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
    list1.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Atrial Pulse Width (ms)").pack()
    options2 = [
        "0.05","0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0","1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9",
    ]
    choice2 = DoubleVar()
    choice2.set(options2[0])
    list2 = ttk.Combobox(aai_screen, value= options2)
    list2.current(4)
    list2.bind("<<ComboboxSelected")
    list2.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Atrial sensitivity (mV)").pack()
    options3 = [
        "0.25","0.5","0.75","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5","6.0","6.5","7.0","7.5","8.0","8.5","9.0","9.5","10.0",
    ]
    choice3 = DoubleVar()
    choice3.set(options3[0])
    list3 = ttk.Combobox(aai_screen, value= options3)
    list3.current(2)
    list3.bind("<<ComboboxSelected>>")
    list3.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Atrial Refractory Period (ms)").pack()
    arp_aai = Scale(aai_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    arp_aai.set(250)
    arp_aai.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Post Ventricular Atrial Refractory Period (ms)").pack()
    pvarp_aai = Scale(aai_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    pvarp_aai.set(250)
    pvarp_aai.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Hysteresis ").pack()
    options4 = [
        "OFF","same as LRL",
    ]
    choice4 = StringVar()
    choice4.set(options4[0])
    list4 = ttk.Combobox(aai_screen, value= options4)
    list4.current(0)
    list4.bind("<<ComboboxSelected>>")
    list4.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Rate smoothing").pack()
    rs_aai = Scale(aai_screen, from_=0, to =25, resolution=3.07, orient=HORIZONTAL)
    rs_aai.pack()
    Label(aai_screen, text = "").pack()

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
        hysteresis_aai = list4.get()

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

    Button(aai_screen, text = "Save", width="5", height = "1", command = show).place(x=70, y=700)
    Label(aai_screen, text = "").pack()
    Button(aai_screen, text = "Load", width="5", height = "1", command = access_val).pack()
    Label(aai_screen, text = "").pack()
    Button(aai_screen, text = "Back", width="5", height = "1", command = destroy_aai).place(x=280, y=700)
    Label(aai_screen, text = "Current User Logged In: %s" % (username_info_login)).pack(side=LEFT)

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
                
main_screen()