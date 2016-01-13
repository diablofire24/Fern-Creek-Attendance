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
x = 1
while x == 1:
    print('\n=================================TEACHER LOGIN==================================\n')
    print('\n                             FERN CREEK HIGH SCHOOL                             \n')
    print('Good Morning, Please put in your 3-digit teacher passcode.')
    my_code = input('\nPasscode: ')
    for i in codes.keys():
        if my_code == i:
            print('\nAre you %s?' % (codes[my_code][0]))
            my_an = input('(y/n) ')
            if my_an.upper() == 'Y':
                if codes[my_code][1] == 0:
                    from time import gmtime, strftime
                    time = strftime("%H:%M:%S", gmtime())
                    print(time)
                    import os
                    name = codes[my_code][0]
                    my_file = open("Login.txt", "w")
                    
                    my_file.write(name)
                    my_file.write(" ")
                    my_file.write(time)
                    my_file.close()
                    os.startfile("C:/Users/Tiger/Desktop/Login Files/Login.txt", "print")
                    codes[my_code][1] = 1                 
                    break
                elif codes[my_code][1] == 1:
                    print("You've already signed in %s." % (codes[my_code][0]))
            else:
                print('Okay!')
                break
        elif my_code == '-1':
            for each in codes.values():
                import os
                if each[1] == 0:
                    print("-", each[0], "has not shown up today.")
                    my_file = open("Slist.txt", "a")
                    my_file.write('\n')
                    my_file.write(each[0])
                    my_file.close()
                    each[1] = 2
                    continue
            print('\nPrint List?')
            my_an = input('(y/n) ')
            if my_an == 'y':
                import os
                os.startfile("C:/Users/Tiger/Desktop/Login Files/Slist.txt", "print")
                print('Program will now end')
                an3 = input('(y/n) ')
                if an3 == 'y':
                    my_file = open("Slist.txt", "w")
                    my_file.write('')
                    my_file.close()
                    quit()
                else:
                    continue
            else:
                continue
