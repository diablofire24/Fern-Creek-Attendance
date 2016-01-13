codes = {
        '118':['Josh Abbel', 0],
        '201':['Andy Ames', 0],
        '310':['David Anderson', 0],
        '840':['Roger Angel', 0],
        '136':['Beau Baker', 0],
        '133':['Paul Barnwell', 0],
        '227':['Sam Barrett', 0],
        '331':['Megan Bishop', 0],
        '314':['Andrew Black', 0],
        '332':['Marcus Blakney', 0],
        '229':['Amber Bolton', 0],
        '304':['Steve Boros', 0],
        '414':['Joni Britt', 0],
        '220':['Justin Brown', 0],
        '756':['Greg Bruce', 0],
        '218':['Shane Canale', 0],
        '205':['Liz Canale', 0],
        '137':['Chris Caragianis', 0],
        '202':['Susan Cramer', 0],
        '110':['Joe Franzen', 0],
        '329':['Jennifer Gohs', 0],
        '226':['Lauren Gordon', 0],
        '106':['Arik Hanks', 0],
        '844':['Frank Herbert', 0],
        '140':['Scott Horan', 0],
        '216':['Frank Houston', 0],
        '333':['Mariam Hubbard', 0],
        '548':['Joe Hutchins', 0],
        '332':['Erin Kenney', 0],
        '404':['Carl Kling', 0],
        '334':['Lauren Kovacs', 0],
        '223':['Kelsey Kruger', 0],
        '222':['Brook LaRosa', 0],
        '123':['Josh Lowry', 0],
        '203':['Isabelle Maramont', 0],
        '324':['Dan Mattews', 0],
        '405':['Aaron May', 0],
        '234':['Erin McAndrew', 0],
        '303':['Holly McArthur', 0],
        '209':['Tony McBee', 0],
        '311':['Brad Mefford', 0],
        '302':['Brian Miller', 0],
        '410':['Dana Morris', 0],
        '400':['David Meyers', 0],
        '336':['Jacky Nelson', 0],
        '318':['Lauralee Nuetz', 0],
        '236':['Joe Nichols', 0],
        '104':['Mary Niebre', 0],
        '200':['Katie Nuss', 0],
        '320':['Christora Osters', 0],
        '119':['Patt Padron', 0],
        '209':['Brent Peters', 0],
        '102':['Dyann Pauly', 0],
        '221':['Peggy Preston', 0],
        '309':['Robert Redies', 0],
        '321':['Isreal Roman', 0],
        '323':['Desiree Sanchez', 0],
        '230':['Doug Snieder', 0],
        '142':['Stephanie Snieder-Smith', 0],
        '307':['Lindsay Scott', 0],
        '319':['Ryan Scott', 0],
        '122':['John Sherman', 0],
        '208':['Garry Shrouds', 0],
        '415':['Don Smith', 0],
        '322':['Reanne Stengal', 0],
        '143':['Susan Stytes', 0],
        '328':['Jared Stout', 0],
        '513':['Mike Stergeon', 0],
        '410':['Josh Tichenor', 0],
        '120':['Stan Torzewki', 0],
        '330':['Anne Washbish', 0],
        '121':['Stephan Westan', 0],
        '335':['Jennifer Wibbles', 0],
        '114':['Sarah Wilson', 0],
        '139':['Andrea Witton', 0]
    }
#Administrator names
#rework data for recent school year
import tkinter as tk
root = tk.Tk()
var = tk.StringVar()
def code_run():
    user = var.get()
    for i in codes.keys():
        if user == i:
            if codes[user][1] == 0:
                import os
                from time import gmtime, strftime
                time = strftime("%H:%M:%S", gmtime())
                print(time)
                my_file = open("Login.txt", "w")
                name = codes[user][0]
                my_file.write(name)
                my_file.write(" ")
                my_file.write(time)
                my_file.close()
                import tempfile
                import win32api
                import win32print
                file = tempfile.mktemp (".txt")
                win32api.ShellExecute (
                0,
                "printto",
                'Login.txt',
                '"%s"' % win32print.GetDefaultPrinter (),
                ".",
                0
                )
                codes[user][1] = 1
                #win32api does not work/cannot be found
                #might only work on seperate PC without any server interferance
def code_list():
    for each in codes.values():
        import os
        if each[1] == 0:
            my_file = open("Slist.txt", "a")
            my_file.write('\n')
            my_file.write(each[0])
            my_file.close()
            each[1] = 2
            class PrintSC:
                LARGE_FONT=("Verdana", 16)
                label5 = tk.Label(text="The List will now print.", font=LARGE_FONT)
                label5.pack(pady=10,padx=10)
                button3 = tk.Button(text="OK", command=code_print, width = 10, font=LARGE_FONT)
                button3.pack()
                button4 = tk.Button(text="Close", command=code_end, width = 10, font=LARGE_FONT)
                button4.pack()
            tk.mainloop()
            #How to open as a seperate window instead as an addition to the current
def code_end():
    quit()
    #Quit checkbox must appear over main window
def code_print():
    my_file = open("Slist.txt", "r")
    import tempfile
    import win32api
    import win32print
    file = tempfile.mktemp (".txt")
    win32api.ShellExecute (
    0,
    "printto",
    'Slist.txt',
    '"%s"' % win32print.GetDefaultPrinter (),
    ".",
    0
    )
    my_file.close()
    #Must clear entry after clicking login
    #Must Resize and Reorganize Main Window
class FCHSapp:
    LARGE_FONT=("Verdana", 16)
    label = tk.Label(text="FCTHS Teacher Login", font=LARGE_FONT)
    label.pack(pady=10,padx=10)
    entry1 = tk.Entry(textvariable=var, width = 35, font=LARGE_FONT)
    entry1.pack()
    button1 = tk.Button(text="Login", command=code_run, width = 30, font=LARGE_FONT)
    button1.pack()
    button2 = tk.Button(text="Print Absent/Tardy Teachers", command=code_list, width = 30, font=LARGE_FONT)
    button2.pack()
    root.minsize(920, 680)
    root.title("FCHS LOGIN")
    root.wm_iconbitmap("ICON.ico")
tk.mainloop()              
