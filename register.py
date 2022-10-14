import ast
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
    username_info = input_username.get()
    password_info  = input_password.get()

    try:
        file = open('database.txt', 'r+')
        d = file.read()
        r = ast.literal_eval(d)
        dict = {username_info: password_info}
        if username_info in r.keys():
            messagebox.showerror('Error', 'Username Already Exists!')
        else: 
            if len(r) <= 10:
                r.update(dict)
                file.truncate(0)
                file.close()
                file = open('database.txt', 'w')
                w = file.write(str(r))
                messagebox.showinfo('Success', 'The Account has been Registered Successfully!')
            else:
                messagebox.showerror('Error', 'User Capacity Reached!')
    except:
        file = open('database.txt', 'w')
        pp = str({'Username': 'password'})
        file.write(pp)
        file.close()
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
        modes() #Leads to another screen
    else:
        messagebox.showerror('Error', 'Login Unsuccessful')

# Modes
def modes():
    global modes_screen
    modes_screen = Toplevel(welcome_screen)
    modes_screen.geometry("400x300+500+250")
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

##############################################################################################################################################################################################
def voo():
    modes_screen.destroy()

    global voo_screen
    voo_screen = Toplevel(welcome_screen)
    voo_screen.geometry("400x600+500+100")
    voo_screen.title("VOO")

    global lrl_voo
    global url_voo
    global va_voo
    global vpw_voo

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
    list.current(0)
    list.bind("<<ComboboxSelected>>")
    list.pack() 
    # drop = OptionMenu(voo_screen, choice, *options)
    # drop.pack()
    Label(voo_screen, text = "").pack()

    Label(voo_screen, text = "Upper Rate Limit (ppm)").pack()
    url_voo = Scale(voo_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
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
    list1.current(0)
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
    list2.current(0)
    list2.bind("<<ComboboxSelected>>")
    list2.pack()
    Label(voo_screen, text = "").pack()

    def show():
        lrl_voo = list.get()
        va_voo = list1.get()
        vpw_voo = list2.get()
        print("The values for VOO",lrl_voo, url_voo.get(), va_voo, vpw_voo)

    Button(voo_screen, text = "Save", width="3", height = "1", command = show).pack()
    Label(voo_screen, text = "").pack()
    Button(voo_screen, text = "Back", width="3", height = "1", command = destroy_voo).pack()
##############################################################################################################################################################################################
def aoo():
    modes_screen.destroy()

    global aoo_screen
    aoo_screen = Toplevel(welcome_screen)
    aoo_screen.geometry("400x600+500+100")
    aoo_screen.title("AOO")

    global lrl_aoo
    global url_aoo
    global aa_aoo
    global apw_aoo

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
    list.current(0)
    list.bind("<<ComboboxSelected>>")
    list.pack() 
    Label(aoo_screen, text = "").pack()

    Label(aoo_screen, text = "Upper Rate Limit (ppm)").pack()
    url_aoo = Scale(aoo_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
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
    list1.current(0)
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
    list2.current(0)
    list2.bind("<<ComboboxSelected>>")
    list2.pack()
    Label(aoo_screen, text = "").pack()

    def show():
        lrl_aoo = list.get()
        va_aoo = list1.get()
        vpw_aoo = list2.get()
        print("The values for AOO", lrl_aoo, url_aoo.get(), va_aoo, vpw_aoo)

    Button(aoo_screen, text = "Save", width="3", height = "1", command = show).pack()
    Label(aoo_screen, text = "").pack()
    Button(aoo_screen, text = "Back", width="3", height = "1", command = destroy_aoo).pack()
##############################################################################################################################################################################################
def vvi():
    modes_screen.destroy()

    global vvi_screen
    vvi_screen = Toplevel(welcome_screen)
    vvi_screen.geometry("400x700+500+20")
    vvi_screen.title("VVI")

    global lrl_vvi
    global url_vvi
    global va_vvi
    global vpw_vvi
    global vs_vvi
    global vrp_vvi
    global hysteresis_vvi
    global rs_vvi

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
    list.current(0)
    list.bind("<<ComboboxSelected>>")
    list.pack() 
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Upper Rate Limit (ppm)").pack()
    url_vvi = Scale(vvi_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
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
    list1.current(0)
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
    list2.current(0)
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
    list3.current(0)
    list3.bind("<<ComboboxSelected>>")
    list3.pack()
    Label(vvi_screen, text = "").pack()

    Label(vvi_screen, text = "Ventricular Refractory Period (ms)").pack()
    vrp_vvi = Scale(vvi_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
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
    options5 = [
        "0","3","6","9","12","15","18","21","25%"
    ]
    choice5 = DoubleVar()
    choice5.set(options5[0])
    list5 = ttk.Combobox(vvi_screen, value= options5)
    list5.current(0)
    list5.bind("<<ComboboxSelected>>")
    list5.pack()
    Label(vvi_screen, text = "").pack()

    def show():
        lrl_vvi = list.get()
        va_vvi = list1.get()
        vpw_vvi = list2.get()
        vs_vvi = list3.get()
        hysteresis_vvi = list4.get()
        rs_vvi = list5.get()
        print("The values for VVI", lrl_vvi, url_vvi.get(), va_vvi, vpw_vvi, vs_vvi, vrp_vvi.get(), hysteresis_vvi, rs_vvi)

    Button(vvi_screen, text = "Save", width="3", height = "1", command = show).pack()
    Label(vvi_screen, text = "").pack()
    Button(vvi_screen, text = "Back", width="3", height = "1", command = destroy_vvi).pack()
##############################################################################################################################################################################################
def aai():
    modes_screen.destroy()

    global aai_screen
    aai_screen = Toplevel(welcome_screen)
    aai_screen.geometry("400x760+500+10")
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

    Label(aai_screen, text = "Set the details below", font = ("Calibri", 13)).pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Lower Rate Limit (ppm)").pack()
    options = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
    ]
    choice = DoubleVar()
    choice.set(options[0])
    list = ttk.Combobox(aai_screen, value= options)
    list.current(0)
    list.bind("<<ComboboxSelected>>")
    list.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Upper Rate Limit (ppm)").pack()
    url_aai = Scale(aai_screen, from_=50, to =175, resolution=5, orient=HORIZONTAL)
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
    list1.current(0)
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
    list2.current(0)
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
    list3.current(0)
    list3.bind("<<ComboboxSelected>>")
    list3.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Atrial Refractory Period (ms)").pack()
    arp_aai = Scale(aai_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
    arp_aai.pack()
    Label(aai_screen, text = "").pack()

    Label(aai_screen, text = "Post Ventricular Atrial Refractory Period (ms)").pack()
    pvarp_aai = Scale(aai_screen, from_=150, to =500, resolution=10, orient=HORIZONTAL)
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
    options5 = [
        "0","3","6","9","12","15","18","21","25%"
    ]
    choice5 = DoubleVar()
    choice5.set(options5[0])
    list5 = ttk.Combobox(aai_screen, value= options5)
    list5.current(0)
    list5.bind("<<ComboboxSelected>>")
    list5.pack()
    Label(aai_screen, text = "").pack()

    def show():
        lrl_aai = list.get()
        aa_aai = list1.get()
        apw_aai = list2.get()
        as_aai = list3.get()
        hysteresis_aai = list4.get()
        rs_aai = list5.get()
        print("The values for AAI", lrl_aai, url_aai.get(), aa_aai, apw_aai, as_aai, arp_aai.get(), pvarp_aai.get(), hysteresis_aai, rs_aai)

    Button(aai_screen, text = "Save", width="3", height = "1", command = show).pack()
    Label(aai_screen, text = "").pack()
    Button(aai_screen, text = "Back", width="3", height = "1", command = destroy_aai).pack()

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

main_screen()