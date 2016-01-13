#Fern Creek High School Teacher Login Program
#Iosef Casas
codes = {
        '118':['Josh Abbel', 0],
        '311':['Akaydin', 0],
        '134a':['Andy Ames', 0],
        '310':['David Anderson', 0],
        'G5':['Roger Angel', 0],
        '138a':['Beau Baker', 0],
        '139':['Balbach', 0],
        '146':['Paul Barnwell', 0],
        '223':['Sam Barrett', 0],
        '321':['Barte', 0],
        '302':['Basemore', 0],
        '307':['Batovsky', 0],
        '201':['Megan Bishop', 0],
        '332':['Marcus Blakney', 0],
        '304':['Steve Boros', 0],
        '103':['Justin Brown', 0],
        'G3':['Greg Bruce', 0],
        '203':['Liz Canale', 0],
        '327':['Cannon', 0],
        '137':['Chris Caragianis', 0],
        '202':['Susan Cramer', 0],
        '110':['Joe Franzen', 0],
        '329':['Jennifer Gohs', 0],
        '226':['Lauren Gordon', 0],
        '106':['Arik Hanks', 0],
        'G6':['Frank Herbert', 0],
        '140':['Scott Horan', 0],
        '133':['Hottman', 0],
        '216':['Frank Houston', 0],
        '333':['Mariam Hubbard', 0],
        '306':['Joe Hutchins', 0],
        '326':['Erin Kenney', 0],
        'G1':['Carl Kling', 0],
        '334':['Lauren Kovacs', 0],
        '218':['Kelsey Kruger', 0],
        '222':['Brook LaRosa', 0],
        '123':['Josh Lowry', 0],
        '205':['Isabelle Maramont', 0],
        '324':['Dan Mattews', 0],
        'G2':['Aaron May', 0],
        '234':['Erin McAndrew', 0],
        '303':['Holly McArthur', 0],
        '235':['Tony McBee', 0],
        '101a':['McPhail', 0],
        '229':['Brad Mefford', 0],
        '210a':['Dana Morris', 0],
        '330':['K. Morris', 0],
        '220':['Mozzingo', 0],
        '134b':['David Meyers', 0],
        '336':['Jacky Nelson', 0],
        '318':['Lauralee Nuetz', 0],
        '236':['Joe Nichols', 0],
        '104':['Mary Nieber', 0],
        '221':['Niemann', 0],
        '200':['Katie Nuss', 0],
        '119':['Patt Padron', 0],
        '214b':['Pedro', 0],
        '209':['Brent Peters', 0],
        '102':['Dyann Pauly', 0],
        '309':['Robert Redies', 0],
        '314':['Isreal Roman', 0],
        '136':['Desiree Sanchez', 0],
        '230':['Doug Snieder', 0],
        '144':['Stephanie Snieder-Smith', 0],
        '233':['Lindsay Scott', 0],
        '319':['Ryan Scott', 0],
        '122':['John Sherman', 0],
        '208':['Garry Shrouds', 0],
        '214a':['Don Smith', 0],
        '142':['Reanne Stengal', 0],
        '143':['Susan Stites', 0],
        '328':['Jared Stout', 0],
        '210b':['Josh Tichenor', 0],
        '120':['Stan Torzewki', 0],
        '331':['Anne Washbish', 0],
        '121':['Stephan Westan', 0],
        '335':['Jennifer Wibbles', 0],
        '114':['Sarah Wilson', 0],
        '212':['Andrea Witton', 0]
    }
'''
-Note: Anything can work as the key, doesn't have to be numbers
-Note: Print access path requires manual change depending on PC
'''
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
                os.startfile("C:/Users/Tiger/Desktop/Login Files/Login.txt", "print")
                codes[user][1] = 1
    var.set("")
def code_list():
    var2=tk.StringVar()
    for each in codes.values():
        import os
        if each[1] == 0:
            my_file = open("Slist.txt", "a")
            my_file.write('\n')
            my_file.write(each[0])
            my_file.close()
            each[1] = 2
            continue
        def code_print():
            admin = var2.get()
            if admin == "-1":
                import os
                os.startfile("C:/Users/Tiger/Desktop/Login Files/Slist.txt", "print")
        class PrintSC:
            LARGE_FONT=("Verdana", 39)
            label6 = tk.Label(text="    ", font=LARGE_FONT)
            label6.pack()
            label5 = tk.Label(text="Enter Admin Code to print", font=LARGE_FONT)
            label5.pack(pady=10,padx=10)
            entry2 = tk.Entry(textvariable=var2, width = 35, font=LARGE_FONT)
            entry2.pack()
            button3 = tk.Button(text="Enter", command=code_print, width = 10, font=LARGE_FONT)
            button3.pack()
            button4 = tk.Button(text="Exit", command=code_end, width = 10, font=LARGE_FONT)
            button4.pack()
        tk.mainloop()
def code_end():
    my_file = open("Slist.txt", "w")
    my_file.write = ("")
    my_file.close
    quit()
class FCHSapp:
    LARGE_FONT=("Verdana", 39)
    labelc = tk.Label(text="    ", font=LARGE_FONT)
    labelc.pack()
    label = tk.Label(text="FCHS Teacher Sign In", font=LARGE_FONT)
    label.pack(pady=10,padx=10)
    entry1 = tk.Entry(textvariable=var, width = 35, font=LARGE_FONT)
    entry1.focus()
    entry1.pack()
    labelb = tk.Label(text="    ", font=LARGE_FONT)
    labelb.pack()
    button1 = tk.Button(text="Sign In", command=code_run, width = 30, font=LARGE_FONT)
    button1.pack()
    button2 = tk.Button(text="Print Absent/Tardy Teachers", command=code_list, width = 30, font=LARGE_FONT)
    button2.pack()
    root.minsize(900, 650)
    root.title("FCHS SIGN IN")
    root.wm_iconbitmap("ICON.ico")    
tk.mainloop()   
