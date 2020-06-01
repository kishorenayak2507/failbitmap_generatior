# import modules
import bitmapgen
from tkinter import *
import os

# Designing window for generic id search

def gen_id():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Generic ID Search")
    register_screen.geometry("350x300")
    register_screen.configure(bg='#E9B195')
    Label(register_screen, text="Please Enter Generic ID",bg='#FD705E',  width="300", height="2",font=("Calibri", 13, 'bold') ).pack()
    Label(register_screen, text="", bg='#E9B195').pack()

    global genericid
    global softwareversion
    global genericid_entry
    global softwareversion_entry
    genericid = StringVar()
    softwareversion = StringVar()

    username_lable = Label(register_screen, text="Generic ID * ")
    username_lable.pack()
    Label(register_screen, text="", bg='#E9B195').pack()
    genericid_entry = Entry(register_screen, textvariable=genericid)
    genericid_entry.pack()
    Label(register_screen, text="", bg='#E9B195').pack()
    password_lable = Label(register_screen, text="SW Version Used * ")
    password_lable.pack()
    Label(register_screen, text="", bg='#E9B195').pack()
    softwareversion_entry = Entry(register_screen, textvariable=softwareversion)
    softwareversion_entry.pack()
    Label(register_screen, text="", bg='#E9B195').pack()
    Button(register_screen, text="SEARCH", width=10, height=1, bg="blue", command=geneid_search).pack()


# Designing window for failure name search

def fail_name():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Failure Name Search ")
    login_screen.geometry("300x250")
    login_screen.configure(bg='#E9B195')
    Label(login_screen, text="Please Enter Failure Name",bg='#FD705E',  width="300", height="2",font=("Calibri", 13, 'bold') ).pack()
    Label(login_screen, text="", bg='#E9B195').pack()

    global failurename_verify
    global sw_version
    failurename_verify = StringVar()
    sw_version = StringVar()
    global failurename_login_entry
    global sw_version_login_entry
    Label(login_screen, text="Failure Name * ", bg='#E9B195', font=("Calibri", 13, 'bold')).pack()
    failurename_login_entry = Entry(login_screen, textvariable=failurename_verify)
    failurename_login_entry.place(width=100,height=2)
    failurename_login_entry.pack()
    Label(login_screen, text="", bg='#E9B195').pack()
    Label(login_screen, text="SW Version Used * ", bg='#E9B195', font=("Calibri", 13, 'bold')).pack()
    sw_version_login_entry = Entry(login_screen, textvariable=sw_version)
    sw_version_login_entry.place(width=100,height=2)
    sw_version_login_entry.pack()
    Label(login_screen, text="", bg='#E9B195').pack()
    Button(login_screen, text="SEARCH",bg='#508FF6', width=10, height=1, font=("Calibri", 13, 'bold'), command=fail_search).pack()


# Implementing event on generic id button

def geneid_search():
    genericid_info = genericid.get()
    softwareversion_info = softwareversion.get()
    fail_info_id = []
    fail_info_id = bitmapgen.find_failure_byID(genericid_info, softwareversion_info)
    if fail_info_id[0] == 'True':
        gid_search_sucess(fail_info_id)
    else:
        gid_search_sucess(fail_info_id)

# Implementing event on failure name button

def fail_search():
    f_name = failurename_verify.get()
    s_ver = sw_version.get()
    fail_info = []
    fail_info = bitmapgen.find_failure_byname(f_name, s_ver)
    if fail_info[0] == 'True':
        fail_search_sucess(fail_info)
    else:
        fail_search_failed()



# Designing popup for search success

def fail_search_sucess(info):
    global login_success_screen
    f_name = failurename_verify.get()
    f_info = info
    failurename_login_entry.delete(0, END)
    sw_version_login_entry.delete(0, END)
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Failure Found ")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Failure Name :\t"+f_name).pack()
    Label(login_success_screen, text="", bg='#E9B195').pack()
    Label(login_success_screen, text="WORD :\t" + f_info[1]+"\tBIT :\t" + f_info[2]).pack()
    Label(login_success_screen, text="", bg='#E9B195').pack()
    Label(login_success_screen, text="GENERIC ID :\t" + f_info[3]).pack()
    Label(login_success_screen, text="", bg='#E9B195').pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def gid_search_sucess(info):
    global login_success_screen
    gid_name = genericid.get()
    g_info = info
    genericid_entry.delete(0, END)
    softwareversion_entry.delete(0, END)
    login_success_screen = Toplevel(register_screen)
    login_success_screen.title("Failure Found ")
    login_success_screen.geometry("300x250")
    Label(login_success_screen, text="Failure Name :\t" + g_info[1]).pack()
    Label(login_success_screen, text="", bg='#E9B195').pack()
    Label(login_success_screen, text="WORD :\t" + g_info[2]+"\tBIT :\t" + g_info[3]).pack()
    Label(login_success_screen, text="", bg='#E9B195').pack()
    Label(login_success_screen, text="GENERIC ID :\t" + gid_name).pack()
    Label(login_success_screen, text="", bg='#E9B195').pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for failed search

def fail_search_failed():
    global password_not_recog_screen
    failurename_login_entry.delete(0, END)
    sw_version_login_entry.delete(0, END)
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Failure Not Found")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Failure is Not Active or Invalid name ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
def gid_search_failed():
    global password_not_recog_screen
    genericid_entry.delete(0, END)
    softwareversion_entry.delete(0, END)
    password_not_recog_screen = Toplevel(register_screen)
    password_not_recog_screen.title("Generic ID Not Found")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="GenericID is Not Active or Invalid ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()

# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x400")
    main_screen.configure(bg='green')
    main_screen.title("Failure bitmap friend")
    Label(text="Search Failure Name or Generic ID", bg="#06FE33", width="300", height="2", font=("Calibri", 25, 'bold')).pack()
    Label(text="", bg="green").pack()
    Label(text="", bg="green").pack()
    Label(text="", bg="green").pack()
    Button(text="FAILURE NAME", bg="#FFB233", height="2", width="30",font=("Calibri", 20, 'bold'), command=fail_name).pack()
    Label(text="", bg="green").pack()
    Button(text="GENERIC ID", bg="#FFB233", height="2", width="30", font=("Calibri", 20, 'bold'), command=gen_id).pack()

    main_screen.mainloop()

main_account_screen()


