#Fern Creek High School Teacher Sign In Program
#Iosef Casas

import tkinter as tk
import os
from time import gmtime, strftime
import csv
'''
-Note: Anything can work as the key, doesn't have to be numbers
-Note: Print access path requires manual change depending on PC
-Note: Make teacher list seperate from code
'''

teacherDataFilename = "attendanceData.csv"

def openCsvReadFile(filename):
    with open(filename, "rb") as csvFile:
        csvReadFile = csv.reader(csvFile)
    return csvReadFile

def openCsvWriteFile(filename):
    with open(filename, "wb") as csvFile:
        csvWriteFile = csv.writer(csvFile)
    return csvWriteFile

def openCsvAppendFile(filename):
    with open(filename, "a") as csvFile:
        csvAppendFile = csv.writer(csvFile)
    return csvAppendFile

def searchTeacherLine(code):
    teacherFile = openCsvReadFile(code)
    lineNum = 0
    for teacher in teacherFile:
        if teacher[0] == code:
            return lineNum 
        lineNum ++
    return -1

def changeAttendanceState(teacher):
    editAttendanceFile = openCsvWriteFile(teacherDataFilename)
    if editAttendanceFile[teacher][2] == 0:
        editAttendanceFile[teacher][2] = 1
    return editAttendanceFile[teacher][2]
    

root = tk.Tk()
var = tk.StringVar()
txt1 = "\nFern Creek High School\nTeacher Sign In\n"

def code_run(event=None):

    def yes():
        for i in codes.keys():
            if user == i:
                if codes[user][1] == 0:
                    codes[user][1] = 1
                    name = codes[user][0]
                    
                    time = strftime("%H:%M:%S", gmtime())
                    my_file = open("Login.txt", "w")
                    name = codes[user][0]
                    my_file.write(name)
                    my_file.write("\n")
                    my_file.write(time)
                    my_file.close()
                    os.startfile("Login.txt", "print")
                window.destroy()
                #end yes
                
    def no():
        var.set("")
        window.destroy()
        #end no
        
    user = var.get()

    for i in codes.keys():
        if user == i:
            if codes[user][1] == 0:
                name = codes[user][0]
                txt2 = "Are you \n%s?" % (name)
                LARGE_FONT=("Verdana", 25)
                window = tk.Toplevel()
                label = tk.Label(window, text=txt2, font=LARGE_FONT)
                label.pack(side="top", fill="both", padx=10, pady=10)
                button8 = tk.Button(window, text="Yes", command=yes, width=8, font=LARGE_FONT, bd = 6)
                button8.pack()
                button9 = tk.Button(window, text="No", command=no, width=8, font=LARGE_FONT, bd = 6)
                button9.pack()
                root.title("FCHS SIGN IN")
                root.wm_iconbitmap(window, "ICON.ico")
                #print request accepted window

            elif codes[user][1] == 1:
                def ok():
                    var.set("")
                    window1.destroy()
                    #end ok
                    
                name = codes[user][0]
                LARGE_FONT=("Verdana", 25)
                window1 = tk.Toplevel()
                label9 = tk.Label(window1, text="You've Already signed\n in %s!" % name, font=LARGE_FONT)
                label9.pack(side="top", fill="both", padx=10, pady=10)
                button10 = tk.Button(window1, text="OK", command=ok, width=5, font=LARGE_FONT, bd = 6)
                button10.pack()
                root.title("FCHS SIGN IN")
                root.wm_iconbitmap(window1, "ICON.ico")
                #print request denied window

        else:
            var.set("")
            
def code_list():
    
    var2=tk.StringVar()

    def code_end():

        admin = var2.get()

        if admin == "-1":
            my_file = open("Slist.txt", "w")
            my_file.write = ("")
            my_file.close
            quit()

        else:
            var2.set("")
        #end code_end
            
    def code_print():

        admin = var2.get()

        if admin == "-1":
            var2.set("")
            for each in codes.values():

                my_file = open("Slist.txt", "a")
                if each[1] == 0:
                    my_file.write('\n')
                    my_file.write(each[0])
                    #writes all names of who are absent to .txt file
            my_file.close()
            os.startfile("C:/Users/tigertech/Desktop/Login Files/Slist.txt", "print")
            my_file = open("Slist.txt", "w")
            my_file.write("")
            my_file.close()
            #end code_print
            
    window2 = tk.Toplevel()
    LARGE_FONT=("Verdana", 25)
    label6 = tk.Label(window2, text="    ", font=LARGE_FONT)
    label6.pack()
    label5 = tk.Label(window2, text="Enter Administrator\n Code to print", font=LARGE_FONT)
    label5.pack()
    entry2 = tk.Entry(window2, textvariable=var2, width = 15, font=LARGE_FONT, bd = 4)
    entry2.pack()
    button3 = tk.Button(window2, text="Enter", command=code_print, width = 10, font=LARGE_FONT, bd = 6)
    button3.pack()
    button4 = tk.Button(window2, text="Exit", command=code_end, width = 10, font=LARGE_FONT, bd = 6)
    button4.pack()
    root.title("FCHS SIGN IN")
    root.wm_iconbitmap(window2, "ICON.ico")
    #teacher list print request window
    
def code_end():

    admin = var2.get()

    if admin == "-1":
        my_file = open("Slist.txt", "w")
        my_file.write = ("")
        my_file.close
        quit()
        #end program
        
class FCHSapp:
    #program start
    #main window
    LARGE_FONT=("Verdana", 47)
    label = tk.Label(text=txt1, font=LARGE_FONT)
    label.pack(pady=10,padx=10)
    entry1 = tk.Entry(textvariable=var, width = 30, font=LARGE_FONT, bd = 4)
    entry1.focus()
    entry1.pack()
    labelb = tk.Label(text="", font=LARGE_FONT)
    labelb.pack()
    button1 = tk.Button(text="Sign In", command=code_run, width = 30, font=LARGE_FONT, bd = 6)
    button1.pack()
    button2 = tk.Button(text="Print Absent/Tardy Teachers", command=code_list, width = 30, font=LARGE_FONT, bd = 6)
    button2.pack()
    root.bind('<Return>', code_run)
    root.title("FCHS SIGN IN")
    root.wm_iconbitmap("ICON.ico")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
tk.mainloop()
