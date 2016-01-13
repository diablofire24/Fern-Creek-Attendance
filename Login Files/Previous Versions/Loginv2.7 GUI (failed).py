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
#Rework data for recent school year
#Note: Anything can work as the key, doesn't have to be numbers
import tkinter as tk
root = tk.Tk()
var = tk.StringVar()
def code_run():
        user = var.get()
        print(user)
        '''
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
                    os.startfile("C:/Users/ILCASA01/Desktop/Login Files/Login.txt", "print")
                    codes[user][1] = 1
                    '''
                    #Notice: Print access path requires manual change depending on PC
def code_list():
        for each in codes.values():
                import os
                if each[1] == 0:
                        my_file = open("Slist.txt", "a")
                        my_file.write('\n')
                        my_file.write(each[0])
                        my_file.close()
                        each[1] = 2
                        continue
def code_end():
        quit()
        #Quit checkbox must appear over main window
def code_print():
        admin = var.get()
        if admin == "-1":
                import os
                os.startfile("C:/Users/ILCASA01/Desktop/Login Files/Slist.txt", "print")
                for each in codes.values():
                        import os
                        if each[1] == 0:
                                my_file = open("Slist.txt", "a")
                                my_file.write('\n')
                                my_file.write(each[0])
                                my_file.close()
                                each[1] = 2
                                continue
        #Notice: Print access path requires manual change depending on PC
class Loginapp(tk.Tk):
        def __init__(self, *args, **kwargs):
                tk.Tk.__init__(self, *args, **kwargs)
                container = tk.Frame(self)
                container.pack(side="top", fill="both", expand = True)
                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)
                self.frames = {}
                for F in(FCHSapp, PrintSC):
                        frame = F(container, self)
                        self.frames[F] = frame
                        frame.grid(row=0, column=0, sticky="nsew")
                        self.show_frame(FCHSapp)
        def show_frame(self, cont):
                frame = self.frames[cont]
                frame.tkraise()
class FCHSapp(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                LARGE_FONT=("Verdana", 30)
                label = tk.Label(self, text="FCHS Teacher Login", font=LARGE_FONT)
                label.pack(pady=10,padx=10)
                entry1 = tk.Entry(self, textvariable=var, width = 35, font=LARGE_FONT)
                entry1.pack()
                labelb = tk.Label(self, text="    ", font=LARGE_FONT)
                labelb.pack()
                button1 = tk.Button(self, text="Login", command=code_run, width = 30, font=LARGE_FONT)
                button1.pack()
                button2 = tk.Button(self, text="Print Absent/Tardy Teachers", command=lambda: controller.show_frame(PrintSC), width = 30, font=LARGE_FONT)
                button2.pack()
        var = tk.StringVar()
        def code_run(self):
                user = var.get()
                print(user)
                '''
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
                            os.startfile("C:/Users/ILCASA01/Desktop/Login Files/Login.txt", "print")
                            codes[user][1] = 1
                            '''
class PrintSC(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                LARGE_FONT=("Verdana", 30)
                label5 = tk.Label(self, text="Enter Admin Code to print", font=LARGE_FONT)
                label5.pack(pady=10,padx=10)
                entry2 = tk.Entry(self, textvariable=var, width = 35, font=LARGE_FONT)
                entry2.pack()
                button3 = tk.Button(self, text="Enter", command=code_print, width = 10, font=LARGE_FONT)
                button3.pack()
                button4 = tk.Button(self, text="Close", command=code_end, width = 10, font=LARGE_FONT)
                button4.pack()   
app = Loginapp()
app.mainloop()
