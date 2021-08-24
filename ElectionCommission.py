from tkinter import ttk
from tkinter import messagebox as mess
import os
import csv
import re
from _csv import writer


try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import simpledialog
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ElectionCommissionClass, AddCandidateClass, AddPresidingOfficerClass, ViewResultClass):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ElectionCommissionClass")



    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class ElectionCommissionClass(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=0,width=600,height=40)



        GLabel_711=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#1F323F"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "Election Commission"
        GLabel_711.place(x=0,y=60,width=600,height=40)



        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"
        GLabel_827["anchor"] = "w"
        GLabel_827["text"] = "Username"
        GLabel_827.place(x=30,y=210,width=130,height=25)



        GLineEdit_360=tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"
        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"
        GLineEdit_360.place(x=180,y=210,width=350,height=25)



        GLabel_154=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#333333"
        GLabel_154["bg"] = "#ffffff"
        GLabel_154["anchor"] = "w"
        GLabel_154["text"] = "Password"
        GLabel_154.place(x=30,y=270,width=130,height=25)



        GLineEdit_63=tk.Entry(self, show="*")
        GLineEdit_63["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_63["font"] = ft
        GLineEdit_63["fg"] = "#333333"
        GLineEdit_63["justify"] = "center"
        GLineEdit_63["text"] = ""
        GLineEdit_63["relief"] = "solid"
        GLineEdit_63.place(x=180,y=270,width=350,height=25)



        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Login"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=460,y=340,width=70,height=25)
        GButton_499["command"] = self.GButton_499_command



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711.place(x=0,y=450,width=600,height=20)



        self.userName=GLineEdit_360
        self.password=GLineEdit_63



    def GButton_499_command(self):
        UserExists=False
        with open("VotingData/ElectionCommisionData.csv", "r", newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for line_num, content in enumerate(reader):
                if content[0] == str(self.userName.get()) and content[2] == str(self.password.get()):
                    UserExists=True
                    break
        #if self.userName.get() == "abc@ec.com" and self.password.get() == "election123":
        if UserExists:
            self.controller.show_frame("AddCandidateClass")
            self.userName.delete(0,'end')
            self.password.delete(0,'end')
        else:
            mess.showinfo("Wrong Credentials","Please Enter Correct Credentials")
            print(self.userName.get())
            print(self.password.get())



class AddCandidateClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=0,width=600,height=40)



        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#000000"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Add Candidate"
        GButton_520.config(relief=tk.FLAT)
        GButton_520.place(x=0,y=40,width=200,height=50)



        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#000000"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Add Presiding Officer"
        GButton_629.config(relief=tk.FLAT)
        GButton_629.place(x=200,y=40,width=200,height=50)
        GButton_629["command"] = self.GButton_629_command



        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#d0cdcd"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "View Results"
        GButton_737.config(relief=tk.FLAT)
        GButton_737.place(x=400,y=40,width=200,height=50)
        GButton_737["command"] = self.GButton_737_command



        GLabel_705=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"
        GLabel_705["anchor"] = "w"
        GLabel_705["text"] = "Name"
        GLabel_705.place(x=30,y=150,width=130,height=25)



        GLineEdit_191=tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.place(x=180,y=150,width=350,height=25)



        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"
        GLabel_827["anchor"] = "w"
        GLabel_827["text"] = "CNIC"
        GLabel_827.place(x=30,y=210,width=130,height=25)



        GLineEdit_360=tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"
        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"
        GLineEdit_360.place(x=180,y=210,width=350,height=25)



        candidate = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        candidate["font"] = ft
        candidate["fg"] = "#333333"
        candidate["bg"] = "#ffffff"
        candidate["anchor"] = "w"
        candidate["text"] = "Constituency"
        candidate.place(x=30,y=270,width=130,height=25)



        OPTIONS2 = [
            "Attock-1(PP-1)",
            "Attock-1(PP-2)",
            "Attock-2(PP-3)",
            "Attock-2(PP-4)",
            "Attock-2(PP-5)"
        ]
        variable2 = tk.StringVar(self)
        variable2.set(OPTIONS2[0])
        cons = tk.OptionMenu(self, variable2, *OPTIONS2)
        cons["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        cons["font"] = ft
        cons["fg"] = "#333333"
        cons["bg"] = "#ffffff"
        cons["justify"] = "center"
        cons["text"] = "Entry"
        cons["relief"] = "solid"
        cons.place(x=180,y=270,width=350,height=25)



        party = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        party["font"] = ft
        party["fg"] = "#333333"
        party["bg"] = "#ffffff"
        party["anchor"] = "w"
        party["text"] = "Party"
        party.place(x=30, y=330, width=130, height=25)



        OPTIONS = [
            "Pakistan Tehreek-e-Insaf (PTI)",
            "Pakistan People's Party (PPP)",
            "Pakistan Muslim League (N) (PMLN)",
            "Pakistan Muslim League (Q) (PMLQ)",
            "Muttahida Qaumi Movement (MQM)",
            "Jamiat-e-Ulema-e-Islam (JUI)",
            "Jamaat-e-Islami Pakistan (JI)",
            "Awami National Party (ANP)"
        ]
        variable = tk.StringVar(self)
        variable.set(OPTIONS[0])
        partydropdown = tk.OptionMenu(self, variable, *OPTIONS)
        partydropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        partydropdown["font"] = ft
        partydropdown["fg"] = "#333333"
        partydropdown["bg"] = "#ffffff"
        partydropdown["justify"] = "center"
        partydropdown["text"] = "Entry"
        partydropdown["relief"] = "solid"
        partydropdown.place(x=180, y=330, width=350, height=25)



        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Save"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=180, y=390, width=80, height=25)
        GButton_499["command"] = self.GButton_499_command



        GButton_edit=tk.Button(self)
        GButton_edit["bg"] = "#9ECED8"
        ft = tkfont.Font(family='Times',size=10)
        GButton_edit["font"] = ft
        GButton_edit["fg"] = "#000"
        GButton_edit["justify"] = "center"
        GButton_edit["text"] = "Edit"
        GButton_edit["relief"] = "solid"
        GButton_edit.place(x=273, y=390, width=80, height=25)
        GButton_edit["command"] = self.enterCnicDialog



        GButton_update=tk.Button(self)
        GButton_update["bg"] = "#9ECED8"
        ft = tkfont.Font(family='Times',size=10)
        GButton_update["font"] = ft
        GButton_update["fg"] = "#000"
        GButton_update["justify"] = "center"
        GButton_update["text"] = "Update"
        GButton_update["relief"] = "solid"
        GButton_update["command"] = self.updateCandidate
        GButton_update.place_forget()



        GButton_delete=tk.Button(self)
        GButton_delete["bg"] = "#E2DF47"
        ft = tkfont.Font(family='Times',size=10)
        GButton_delete["font"] = ft
        GButton_delete["fg"] = "#000"
        GButton_delete["justify"] = "center"
        GButton_delete["text"] = "Delete"
        GButton_delete["relief"] = "solid"
        GButton_delete.place(x=368, y=390, width=80, height=25)
        GButton_delete["command"] = self.deleteCandidate



        returnButton = tk.Button(self)
        returnButton["bg"] = "#DC4D41"
        ft = tkfont.Font(family='Times', size=10)
        returnButton["font"] = ft
        returnButton["fg"] = "#ffffff"
        returnButton["justify"] = "center"
        returnButton["text"] = "Logout"
        returnButton["relief"] = "solid"
        returnButton.place(x=460,y=390,width=70,height=25)
        returnButton["command"] = self.returnButton_command



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711.place(x=0,y=450,width=600,height=20)



        self.candName = GLineEdit_191
        self.cnic = GLineEdit_360
        self.cons = variable2
        self.party = variable

        self.consDropDown = cons
        self.partyDropDown = partydropdown
        self.editButton = GButton_edit
        self.updateButton = GButton_update
        self.deleteButton = GButton_delete



    def returnButton_command(self):
        self.candName.delete(0, 'end')
        self.cnic.configure(state='normal')
        self.cnic.delete(0, 'end')
        self.consDropDown.configure(state='normal')
        self.partyDropDown.configure(state='normal')
        self.editButton.place(x=273, y=390, width=80, height=25)
        self.updateButton.place_forget()
        self.controller.show_frame("ElectionCommissionClass")



    def GButton_629_command(self):
        self.candName.delete(0, 'end')
        self.cnic.configure(state='normal')
        self.cnic.delete(0, 'end')
        self.consDropDown.configure(state='normal')
        self.partyDropDown.configure(state='normal')
        self.editButton.place(x=273, y=390, width=80, height=25)
        self.updateButton.place_forget()
        self.controller.show_frame("AddPresidingOfficerClass")



    def GButton_737_command(self):
        self.candName.delete(0, 'end')
        self.cnic.configure(state='normal')
        self.cnic.delete(0, 'end')
        self.consDropDown.configure(state='normal')
        self.partyDropDown.configure(state='normal')
        self.editButton.place(x=273, y=390, width=80, height=25)
        self.updateButton.place_forget()
        self.controller.show_frame("ViewResultClass")



    def GButton_499_command(self):
        if len(self.cnic.get()) == 0 or len(self.candName.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            if len(self.cnic.get()) != 13:
                mess.showwarning("CNIC Warning", "Please enter a 13 digit CNIC without dashes\nYou entered "
                                 + str(len(self.cnic.get())) + " digit CNIC")
            else:
                exists = os.path.isfile("VotingData\CandidateData.csv")
                agentDetails = [str(self.party.get()), '', str(self.candName.get()), '', str(self.cnic.get()), '',
                                str(self.cons.get())]
                col_names = ['Party Name', '', 'Candidate Name', '', 'CNIC', '', 'Constituency']
                PollingAgentAlreadyExist = False

                if exists:
                    with open("VotingData\CandidateData.csv", "r", newline='') as f:
                        reader = csv.reader(f, delimiter=',', quotechar='"')
                        for line_num, content in enumerate(reader):
                            if (content[4] == str(self.cnic.get()) and self.party.get() != content[0]) or (
                                    self.cons.get() == content[6] and self.party.get() == content[0]):
                                PollingAgentAlreadyExist = True
                                break
                    if not PollingAgentAlreadyExist:
                        with open("VotingData\CandidateData.csv", 'a+', newline='') as csvFile1:
                            writer = csv.writer(csvFile1)
                            writer.writerow(agentDetails)
                        csvFile1.close()
                        mess.showinfo("Success", "Candidate Added Successfully")
                        self.cnic.delete(0, 'end')
                        self.candName.delete(0, 'end')

                    else:
                        mess.showinfo("Failed", "Data Already Exists")
                        print("Candidate's CNIC Already Exists")
                else:

                    with open("VotingData\CandidateData.csv", 'a+', newline='') as csvFile1:
                        writer = csv.writer(csvFile1)
                        writer.writerow(col_names)
                        writer.writerow(agentDetails)
                    csvFile1.close()
                    mess.showinfo("Success", "Candidate Added Successfully")
                    self.cnic.delete(0, 'end')
                    self.candName.delete(0, 'end')



    def enterCnicDialog(self):
        cnic = simpledialog.askstring("Candidate's CNIC", "Please enter your CNIC as a Candidate.")

        if (len(cnic) == 13):
            _count = 0
            from collections import Counter
            from operator import itemgetter

            exists = os.path.isfile("VotingData\CandidateData.csv")

            i = 0

            if exists:
                with open("VotingData\CandidateData.csv", 'r', newline='') as csvFile1:
                    reader1 = csv.reader(csvFile1, delimiter=',', quotechar='"')

                    id_counts = Counter(map(itemgetter(0, 2, 4, 6), reader1))
                    id_counts = dict(id_counts)

                    for key in id_counts:
                        i = i + 1
                        if (i > 1):
                            if str(cnic) in str(key):
                                _count += 1
                                print(str(key))
                                string_array = str(key).replace('"', '').split(",")

                                _party = string_array[0].replace("'", "")
                                _party = _party[1:]

                                _name = string_array[1].replace("'", "")

                                _cnic = string_array[2].replace("'", "")

                                _cons = string_array[3].replace("'", "")
                                _cons = _cons[:-1]


                                print("Name: " + _name + "\nCNIC: " + _cnic)

                                self.candName.delete(0, 'end')
                                self.cnic.delete(0, 'end')

                                self.candName.insert(0, _name.lstrip())
                                self.cnic.insert(0, _cnic.strip())
                                self.cnic.configure(state='disabled')
                                self.party.set(_party)
                                self.cons.set(_cons.strip())
                                self.consDropDown.configure(state='disabled')
                                self.partyDropDown.configure(state='disabled')

                                print("Done")
                                self.editButton.place_forget()
                                self.updateButton.place(x=273, y=390, width=80, height=25)


                csvFile1.close()

                if (_count < 1):
                    mess._show(title='No Record',
                               message='No record found with this CNIC')
                    return ()


        elif (len(cnic) != 13):
            mess._show(title='Length Error', message='Please enter a 13 digit CNIC without dashes\nYou entered '
                                                     + str(len(cnic)) + ' digit CNIC')



    def updateCandidate(self):

        cnic = self.cnic.get()
        party = self.party.get()
        cons = self.cons.get()

        cnicLength = len(cnic)
        partyLength = len(party)
        consLength = len(cons)

        # mess._show(title = 'CNIC', message = 'CNIC: ' + cnic + '\nPart: ' + party + '\nConst: ' + cons +
        #                                      '\nCNIC Length: ' + str(cnicLength) + '\nParty Length: ' + str(partyLength) +
        #                                      '\nConst Length: ' + str(consLength))


        _count = 0
        if cnicLength == 0 or consLength == 0 or partyLength == 0:
            mess.showwarning("Incomplete Data", "CNIC, Party and Constituency is must.")
        else:
            if cnicLength == 13:
                allRows = []
                exists = os.path.isfile("VotingData/CandidateData.csv")
                if exists:
                    with open("VotingData/CandidateData.csv") as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                        for row in csv_reader:
                            if row[0] == party and row[4] == cnic and row[6] == cons:
                                _count += 1
                            else:
                                allRows.append(row)
                    csv_file.close()
                if (_count > 0):
                    updateFile("VotingData/CandidateData.csv", allRows)
                    self.GButton_499_command()

                    # setting the frame back to normal
                    self.candName.delete(0, 'end')
                    self.cnic.configure(state='normal')
                    self.cnic.delete(0, 'end')
                    self.consDropDown.configure(state='normal')
                    self.partyDropDown.configure(state='normal')
                    self.editButton.place(x=273, y=390, width=80, height=25)
                    self.updateButton.place_forget()

                else:
                    mess._show(title='No Record', message='There is no user existed with this Party Name, Constituency and CNIC.')
            elif (cnicLength != 13):
                mess._show(title='Length Error', message='Please enter a 13 digit CNIC without dashes\nYou entered '
                                                         + str(cnicLength) + ' digit CNIC')



    def deleteCandidate(self):

        cnic = self.cnic.get()
        party = self.party.get()
        cons = self.cons.get()

        cnicLength = len(cnic)
        partyLength = len(party)
        consLength = len(cons)

        # mess._show(title = 'CNIC', message = 'CNIC: ' + cnic + '\nPart: ' + party + '\nConst: ' + cons +
        #                                      '\nCNIC Length: ' + str(cnicLength) + '\nParty Length: ' + str(partyLength) +
        #                                      '\nConst Length: ' + str(consLength))

        _count = 0
        if cnicLength == 0 or consLength == 0 or partyLength == 0:
            mess.showwarning("Incomplete Data", "CNIC, Party and Constituency is must.")
        else:
            if cnicLength == 13:
                allRows = []
                exists = os.path.isfile("VotingData/CandidateData.csv")
                if exists:
                    with open("VotingData/CandidateData.csv") as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                        for row in csv_reader:
                            if row[0] == party and row[4] == cnic and row[6] == cons:
                                _count += 1
                            else:
                                allRows.append(row)
                    csv_file.close()
                if (_count > 0):
                    mess._show(title='User Deleted', message='User has been deleted successfully.')
                    updateFile("VotingData/CandidateData.csv", allRows)

                    # setting the frame back to normal
                    self.candName.delete(0, 'end')
                    self.cnic.configure(state='normal')
                    self.cnic.delete(0, 'end')
                    self.consDropDown.configure(state='normal')
                    self.partyDropDown.configure(state='normal')
                    self.editButton.place(x=273, y=390, width=80, height=25)
                    self.updateButton.place_forget()
                else:
                    mess._show(title='No Record', message='There is no user existed with this Party Name, Constituency and CNIC.')
            elif (cnicLength != 13):
                mess._show(title='Length Error', message='Please enter a 13 digit CNIC without dashes\nYou entered '
                                                         + str(cnicLength) + ' digit CNIC')



def updateFile(fileNmae, allRows):
    with open(fileNmae, 'w', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerows(allRows)



class AddPresidingOfficerClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=0,width=600,height=40)



        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#000000"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Add Candidate"
        GButton_520.config(relief=tk.FLAT)
        GButton_520.place(x=0,y=40,width=200,height=50)
        GButton_520["command"] = self.GButton_520_command



        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#000000"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Add Presiding Officer"
        GButton_629.config(relief=tk.FLAT)
        GButton_629.place(x=200,y=40,width=200,height=50)



        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#d0cdcd"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "View Results"
        GButton_737.config(relief=tk.FLAT)
        GButton_737.place(x=400,y=40,width=200,height=50)
        GButton_737["command"] = self.GButton_737_command



        GLabel_705=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"
        GLabel_705["anchor"] = "w"
        GLabel_705["text"] = "Name"
        GLabel_705.place(x=30,y=150,width=130,height=25)



        GLineEdit_191=tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.place(x=180,y=150,width=350,height=25)



        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"
        GLabel_827["anchor"] = "w"
        GLabel_827["text"] = "CNIC"
        GLabel_827.place(x=30,y=200,width=130,height=25)



        GLineEdit_360=tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"
        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"
        GLineEdit_360.place(x=180,y=200,width=350,height=25)



        GLabel_154=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#333333"
        GLabel_154["bg"] = "#ffffff"
        GLabel_154["anchor"] = "w"
        GLabel_154["text"] = "Password"
        GLabel_154.place(x=30,y=250,width=130,height=25)



        GLineEdit_63=tk.Entry(self)
        GLineEdit_63["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_63["font"] = ft
        GLineEdit_63["fg"] = "#333333"
        GLineEdit_63["justify"] = "center"
        GLineEdit_63["text"] = ""
        GLineEdit_63["relief"] = "solid"
        GLineEdit_63.place(x=180,y=250,width=350,height=25)



        party = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        party["font"] = ft
        party["fg"] = "#333333"
        party["bg"] = "#ffffff"
        party["anchor"] = "w"
        party["text"] = "Phone #"
        party.place(x=30, y=300, width=130, height=25)



        partydropdown = tk.Entry(self)
        partydropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        partydropdown["font"] = ft
        partydropdown["fg"] = "#333333"
        partydropdown["justify"] = "center"
        partydropdown["text"] = ""
        partydropdown["relief"] = "solid"
        partydropdown.insert(0, "+92")
        partydropdown.place(x=180, y=300, width=350, height=25)



        candidate = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        candidate["font"] = ft
        candidate["fg"] = "#333333"
        candidate["bg"] = "#ffffff"
        candidate["anchor"] = "w"
        candidate["text"] = "Constituency"
        candidate.place(x=30, y=350, width=130, height=25)



        OPTIONS = [
            "Attock-1(PP-1)",
            "Attock-1(PP-2)",
            "Attock-2(PP-3)",
            "Attock-2(PP-4)",
            "Attock-2(PP-5)"
        ]
        variable = tk.StringVar(self)
        variable.set(OPTIONS[0])
        GListBox_541 = tk.OptionMenu(self, variable, *OPTIONS)
        GListBox_541["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GListBox_541["font"] = ft
        GListBox_541["bg"] = "#ffffff"
        GListBox_541["fg"] = "#333333"
        GListBox_541["justify"] = "center"
        GListBox_541["text"] = "Entry"
        GListBox_541["relief"] = "solid"
        GListBox_541.place(x=180, y=350, width=350, height=25)



        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Save"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=180, y=390, width=80, height=25)
        GButton_499["command"] = self.GButton_499_command



        GButton_edit=tk.Button(self)
        GButton_edit["bg"] = "#9ECED8"
        ft = tkfont.Font(family='Times',size=10)
        GButton_edit["font"] = ft
        GButton_edit["fg"] = "#000"
        GButton_edit["justify"] = "center"
        GButton_edit["text"] = "Edit"
        GButton_edit["relief"] = "solid"
        GButton_edit.place(x=273, y=390, width=80, height=25)
        GButton_edit["command"] = self.enterCnicDialog



        GButton_update=tk.Button(self)
        GButton_update["bg"] = "#9ECED8"
        ft = tkfont.Font(family='Times',size=10)
        GButton_update["font"] = ft
        GButton_update["fg"] = "#000"
        GButton_update["justify"] = "center"
        GButton_update["text"] = "Update"
        GButton_update["relief"] = "solid"
        GButton_update["command"] = self.updateOfficer
        GButton_update.place_forget()



        GButton_delete=tk.Button(self)
        GButton_delete["bg"] = "#E2DF47"
        ft = tkfont.Font(family='Times',size=10)
        GButton_delete["font"] = ft
        GButton_delete["fg"] = "#000"
        GButton_delete["justify"] = "center"
        GButton_delete["text"] = "Delete"
        GButton_delete["relief"] = "solid"
        GButton_delete.place(x=368, y=390, width=80, height=25)
        GButton_delete["command"] = self.deleteOfficer



        returnButton = tk.Button(self)
        returnButton["bg"] = "#DC4D41"
        ft = tkfont.Font(family='Times', size=10)
        returnButton["font"] = ft
        returnButton["fg"] = "#ffffff"
        returnButton["justify"] = "center"
        returnButton["text"] = "Logout"
        returnButton["relief"] = "solid"
        returnButton.place(x=460,y=390,width=70,height=25)
        returnButton["command"] = self.returnButton_command



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711.place(x=0,y=450,width=600,height=20)



        self.GLineEdit_27 = GLineEdit_191
        self.GLineEdit_676 = GLineEdit_360
        self.GLineEdit_232 = GLineEdit_63
        self.GLineEdit_777 =partydropdown
        self.variable = variable
        self.dropDown = GListBox_541;

        self.editButton = GButton_edit
        self.updateButton = GButton_update
        self.deleteButton = GButton_delete



    def returnButton_command(self):
        self.GLineEdit_27.delete(0, 'end')
        self.GLineEdit_676.configure(state='normal')
        self.GLineEdit_676.delete(0, 'end')
        self.GLineEdit_232.delete(0, 'end')
        self.GLineEdit_777.delete(0, 'end')
        self.dropDown.configure(state='normal')
        self.editButton.place(x=273, y=390, width=80, height=25)
        self.updateButton.place_forget()
        self.controller.show_frame("ElectionCommissionClass")



    def GButton_520_command(self):
        self.GLineEdit_27.delete(0, 'end')
        self.GLineEdit_676.configure(state='normal')
        self.GLineEdit_676.delete(0, 'end')
        self.GLineEdit_232.delete(0, 'end')
        self.GLineEdit_777.delete(0, 'end')
        self.dropDown.configure(state='normal')
        self.editButton.place(x=273, y=390, width=80, height=25)
        self.updateButton.place_forget()
        self.controller.show_frame("AddCandidateClass")



    def GButton_737_command(self):
        self.GLineEdit_27.delete(0, 'end')
        self.GLineEdit_676.configure(state='normal')
        self.GLineEdit_676.delete(0, 'end')
        self.GLineEdit_232.delete(0, 'end')
        self.GLineEdit_777.delete(0, 'end')
        self.dropDown.configure(state='normal')
        self.editButton.place(x=273, y=390, width=80, height=25)
        self.updateButton.place_forget()
        self.controller.show_frame("ViewResultClass")



    def GButton_499_command(self):
        regex = "(\+\w{5})\w{7}"
        if len(self.GLineEdit_27.get()) == 0 or len(self.GLineEdit_676.get()) == 0 or len(
                self.GLineEdit_777.get()) == 0 or len(self.GLineEdit_232.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            if not re.search(regex, str(self.GLineEdit_777.get())) or len(self.GLineEdit_777.get()) != 13:
                mess.showwarning("Wrong Phone Number", "Please enter a valid phone number.\n\nFor Example: +923001234567")
            else:
                if len(self.GLineEdit_676.get()) != 13:
                    mess.showwarning("CNIC Warning", "Please enter a 13 digit CNIC without dashes\nYou entered "
                                     + str(len(self.GLineEdit_676.get())) + " digit CNIC")
                else:
                    name1 = self.GLineEdit_27.get()
                    constituency = self.variable.get()
                    cnic = self.GLineEdit_676.get()
                    password1 = self.GLineEdit_232.get()
                    phone1 = self.GLineEdit_777.get()
                    exists = os.path.isfile("VotingData\PresidingOfficerData.csv")
                    agentDetails = [str(name1), '', cnic, '', password1, '', phone1, '', constituency]
                    col_names = ['Name', '', 'CNIC', '', 'Password', '', 'Phone', '', 'Constituency']
                    PollingAgentAlreadyExist = False

                    if exists:
                        with open("VotingData\PresidingOfficerData.csv", "r", newline='') as f:
                            reader = csv.reader(f, delimiter=',', quotechar='"')
                            for line_num, content in enumerate(reader):
                                if content[2] == str(cnic):
                                    PollingAgentAlreadyExist = True
                                    break
                        if not PollingAgentAlreadyExist:
                            with open("VotingData\PresidingOfficerData.csv", 'a+', newline='') as csvFile1:
                                writer = csv.writer(csvFile1)
                                writer.writerow(agentDetails)
                            csvFile1.close()
                            self.GLineEdit_27.delete(0, 'end')
                            self.GLineEdit_232.delete(0, 'end')
                            self.GLineEdit_676.delete(0, 'end')
                            self.GLineEdit_777.delete(0, 'end')

                            mess.showinfo("Success", "Presiding Officer Added Successfully")
                        else:
                            mess.showinfo("Failed", "Presiding Officer's CNIC  Already Exists")
                            print("Presiding Officer's CNIC Already Exists")


                    else:

                        with open("VotingData\PresidingOfficerData.csv", 'a+', newline='') as csvFile1:
                            writer = csv.writer(csvFile1)
                            writer.writerow(col_names)
                            writer.writerow(agentDetails)
                        csvFile1.close()



    def enterCnicDialog(self):
        cnic = simpledialog.askstring("Presiding Officer's CNIC", "Please enter your CNIC as a Presiding Officer.")

        if (len(cnic) == 13):
            _count = 0
            from collections import Counter
            from operator import itemgetter

            exists = os.path.isfile("VotingData\PresidingOfficerData.csv")

            i = 0

            if exists:
                with open("VotingData\PresidingOfficerData.csv", 'r', newline='') as csvFile1:
                    reader1 = csv.reader(csvFile1, delimiter=',', quotechar='"')

                    id_counts = Counter(map(itemgetter(0, 2, 4, 6, 8), reader1))
                    id_counts = dict(id_counts)

                    for key in id_counts:
                        i = i + 1
                        if (i > 1):
                            # print(str(key))
                            if str(cnic) in str(key):
                                _count += 1
                                print(str(key))
                                string_array = str(key).replace('"', '').split(",")

                                _name = string_array[0].replace("'", "")
                                _name = _name[1:]

                                _cnic = string_array[1].replace("'", "")

                                _password = string_array[2].replace("'", "")

                                _phone = string_array[3].replace("'", "")

                                _cons = string_array[4].replace("'", "")
                                _cons = _cons[:-1]


                                # print("Name: " + _name + "\nCNIC: " + _cnic +"\nPassword: " + _password + "\nPhone: " + _phone)

                                self.GLineEdit_27.delete(0, 'end')
                                self.GLineEdit_676.delete(0, 'end')
                                self.GLineEdit_232.delete(0, 'end')
                                self.GLineEdit_777.delete(0, 'end')

                                self.GLineEdit_27.insert(0, _name.lstrip())
                                self.GLineEdit_676.insert(0, _cnic.strip())
                                self.GLineEdit_676.configure(state='disabled')
                                self.variable.set(_cons.strip())
                                self.dropDown.configure(state='disabled')
                                self.GLineEdit_232.insert(0, _password.strip())
                                self.GLineEdit_777.insert(0, _phone.strip())

                                print("Done")
                                self.editButton.place_forget()
                                self.updateButton.place(x=273, y=390, width=80, height=25)

                csvFile1.close()

                if (_count < 1):
                    mess._show(title='No Record',
                               message='No record found with this CNIC')
                    return ()


        elif (len(cnic) != 13):
            mess._show(title='Length Error', message='Please enter a 13 digit CNIC without dashes\nYou entered '
                                                     + str(len(cnic)) + ' digit CNIC')



    def updateOfficer(self):

        cnic = self.GLineEdit_676.get()
        cons = self.variable.get()

        cnicLength = len(cnic)
        consLength = len(cons)

        # mess._show(title = 'CNIC', message = 'CNIC: ' + cnic + '\nConst: ' + cons +
        #                                      '\nCNIC Length: ' + str(cnicLength) + '\nConst Length: ' + str(consLength))

        _count = 0
        if cnicLength == 0:
            mess.showwarning("Incomplete Data", "CNIC and Constituency is must.")
        else:
            if cnicLength == 13:
                allRows = []
                exists = os.path.isfile("VotingData/PresidingOfficerData.csv")
                if exists:
                    with open("VotingData/PresidingOfficerData.csv") as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                        for row in csv_reader:
                            if row[2] == cnic and row[8] == cons:
                                _count += 1
                            else:
                                allRows.append(row)
                    csv_file.close()
                if (_count > 0):
                    updateFile("VotingData/PresidingOfficerData.csv", allRows)
                    self.GButton_499_command()

                    # setting frame back to normal
                    self.GLineEdit_27.delete(0, 'end')
                    self.GLineEdit_676.configure(state='normal')
                    self.GLineEdit_676.delete(0, 'end')
                    self.GLineEdit_232.delete(0, 'end')
                    self.GLineEdit_777.delete(0, 'end')
                    self.dropDown.configure(state='normal')
                    self.editButton.place(x=273, y=390, width=80, height=25)
                    self.updateButton.place_forget()
                else:
                    mess._show(title='No Record', message='There is no user existed with this Constituency and CNIC.')
            elif (cnicLength != 13):
                mess._show(title='Length Error', message='Please enter a 13 digit CNIC without dashes\nYou entered '
                                                         + str(cnicLength) + ' digit CNIC')




    def deleteOfficer(self):
        _count = 0
        if len(self.GLineEdit_676.get()) == 0:
            mess.showwarning("Incomplete Data", "CNIC and Constituency is must.")
        else:
            if len(self.GLineEdit_676.get()) == 13:
                allRows = []
                exists = os.path.isfile("VotingData/PresidingOfficerData.csv")
                if exists:
                    with open("VotingData/PresidingOfficerData.csv") as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                        for row in csv_reader:
                            if row[2] == self.GLineEdit_676.get() and row[8] == self.variable.get():
                                _count += 1
                            else:
                                allRows.append(row)
                    csv_file.close()
                if (_count > 0):
                    mess._show(title='User Deleted', message='User has been deleted successfully.')
                    updateFile("VotingData/PresidingOfficerData.csv", allRows)

                    # setting frame back to normal
                    self.GLineEdit_27.delete(0, 'end')
                    self.GLineEdit_676.configure(state='normal')
                    self.GLineEdit_676.delete(0, 'end')
                    self.GLineEdit_232.delete(0, 'end')
                    self.GLineEdit_777.delete(0, 'end')
                    self.dropDown.configure(state='normal')
                    self.editButton.place(x=273, y=390, width=80, height=25)
                    self.updateButton.place_forget()
                else:
                    mess._show(title='No Record', message='There is no user existed with this Constituency and CNIC.')
            elif (len(self.GLineEdit_676.get()) != 13):
                mess._show(title='Length Error', message='Please enter a 13 digit CNIC without dashes\nYou entered '
                                                         + str(len(self.GLineEdit_676.get())) + ' digit CNIC')



def updateFile(fileNmae, allRows):
    with open(fileNmae, 'w', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerows(allRows)


class ViewResultClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=0,width=600,height=40)



        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#000000"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Add Candidate"
        GButton_520.config(relief=tk.FLAT)
        GButton_520.place(x=0,y=40,width=200,height=50)
        GButton_520["command"] = self.GButton_520_command



        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#000000"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Add Presiding Officer"
        GButton_629.config(relief=tk.FLAT)
        GButton_629.place(x=200,y=40,width=200,height=50)
        GButton_629["command"] = self.GButton_629_command



        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "View Results"
        GButton_737.config(relief=tk.FLAT)
        GButton_737.place(x=400,y=40,width=200,height=50)



        tv = ttk.Treeview(self, height=15, columns=('Constituency', 'Party', 'Candidate', 'Votes'))
        tv.column('Constituency', width=100)
        tv.column('Party', width=250)
        tv.column('Candidate', width=150)
        tv.column('Votes', width=50)
        tv.heading('Constituency', text='Constituency', anchor=tk.W)
        tv.heading('Party', text='Party', anchor=tk.W)
        tv.heading('Candidate', text='Candidate', anchor=tk.W)
        tv.heading('Votes', text='Votes', anchor=tk.W)
        tv['show'] = 'headings'
        scroll = ttk.Scrollbar(self, orient='vertical', command=tv.yview)
        tv.configure(yscrollcommand=scroll.set)
        tv.place(x=20, y=120, height=230)



        from collections import Counter
        from operator import itemgetter

        exists = os.path.isfile("VotingData\ResultData.csv")
        i = 0

        if exists:
            with open("VotingData\ResultData.csv", 'r', newline='') as csvFile1:
                reader1 = csv.reader(csvFile1, delimiter=',', quotechar='"')

                id_counts = Counter(map(itemgetter(4, 6, 8), reader1))
                id_counts = dict(id_counts)

                for key in id_counts:
                    i = i + 1
                    if (i > 1):
                        print(str(key))
                        if "Attock-1(PP-1)" in str(key):

                            string_array = str(key).replace('"', '').split(",")

                            _constituency = string_array[0].replace("'", "")
                            _constituency = _constituency[1:]

                            _party = string_array[1].replace("'", "")

                            _candidate = string_array[2].replace("'", "")
                            _candidate = _candidate[:-1]

                            tv.insert('', 0, values=(_constituency, _party, _candidate, str(id_counts[key]), str()))

            csvFile1.close()
            self.tv = tv



        viewResults = tk.Button(self)
        viewResults["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times', size=10)
        viewResults["font"] = ft
        viewResults["fg"] = "#ffffff"
        viewResults["justify"] = "center"
        viewResults["text"] = "View Results"
        viewResults["relief"] = "solid"
        viewResults.place(x=80, y=390, width=80, height=25)
        viewResults["command"] = self.viewResults_command



        OPTIONS = [
            "Attock-1(PP-1)",
            "Attock-1(PP-2)",
            "Attock-2(PP-3)",
            "Attock-2(PP-4)",
            "Attock-2(PP-5)"
        ]
        variable = tk.StringVar(self)
        variable.set(OPTIONS[0])
        GListBox_541 = tk.OptionMenu(self, variable, *OPTIONS)
        GListBox_541["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GListBox_541["font"] = ft
        GListBox_541["bg"] = "#ffffff"
        GListBox_541["fg"] = "#333333"
        GListBox_541["justify"] = "center"
        GListBox_541["text"] = "Entry"
        GListBox_541["relief"] = "solid"
        GListBox_541.place(x=180, y=390, width=250, height=25)



        returnButton = tk.Button(self)
        returnButton["bg"] = "#DC4D41"
        ft = tkfont.Font(family='Times', size=10)
        returnButton["font"] = ft
        returnButton["fg"] = "#ffffff"
        returnButton["justify"] = "center"
        returnButton["text"] = "Logout"
        returnButton["relief"] = "solid"
        returnButton.place(x=460,y=390,width=70,height=25)
        returnButton["command"] = self.returnButton_command



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711.place(x=0,y=450,width=600,height=20)

        self.constituency = variable



    def viewResults_command(self):
        self.tv.delete(*self.tv.get_children())

        from collections import Counter
        from operator import itemgetter

        exists = os.path.isfile("VotingData\ResultData.csv")

        i = 0

        if exists:
            with open("VotingData\ResultData.csv", 'r', newline='') as csvFile1:
                reader1 = csv.reader(csvFile1, delimiter=',', quotechar='"')

                id_counts = Counter(map(itemgetter(4, 6, 8), reader1))
                id_counts = dict(id_counts)

                for key in id_counts:
                    i = i + 1
                    if (i > 1):
                        # print(str(key))
                        if str(self.constituency.get()) in str(key):

                            string_array = str(key).replace('"', '').split(",")

                            _constituency = string_array[0].replace("'", "")
                            _constituency = _constituency[1:]

                            _party = string_array[1].replace("'", "")

                            _candidate = string_array[2].replace("'", "")
                            _candidate = _candidate[:-1]

                            self.tv.insert('', 0, values=(_constituency, _party, _candidate, str(id_counts[key]), str()))

            csvFile1.close()



    def returnButton_command(self):
        self.controller.show_frame("ElectionCommissionClass")



    def GButton_520_command(self):
        self.controller.show_frame("AddCandidateClass")



    def GButton_629_command(self):
        self.controller.show_frame("AddPresidingOfficerClass")



if __name__ == "__main__":
    app = SampleApp()
    app.title("Election Commissioner")
    app.mainloop()