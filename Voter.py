from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import pandas as pd
import datetime
import time
from twilio.rest import Client
import random

try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
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
        for F in (VoterClass, PageNine):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("VoterClass")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Pages:
    p = ''
    q = ''
    r = ''

class VoterClass(tk.Frame, Pages):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")



        GLabel_711 = tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times', size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0, y=0, width=600, height=40)



        GLabel_711 = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#1F323F"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "Please Cast Your Vote"
        GLabel_711.place(x=0, y=60, width=600, height=40)



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711.place(x=0,y=450,width=600,height=20)



        GLabel_827 = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"
        GLabel_827["anchor"] = "w"
        GLabel_827["text"] = "Name"
        GLabel_827.place(x=30, y=150, width=150, height=25)



        GLineEdit_361 = tk.Entry(self)
        GLineEdit_361["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GLineEdit_361["font"] = ft
        GLineEdit_361["fg"] = "#333333"
        GLineEdit_361["justify"] = "center"
        GLineEdit_361["text"] = ""
        GLineEdit_361["relief"] = "solid"
        GLineEdit_361.place(x=180, y=150, width=350, height=25)



        GLabel_705 = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"
        GLabel_705["text"] = "CNIC"
        GLabel_705["anchor"] = "w"
        GLabel_705.place(x=30, y=200, width=150, height=25)



        GLineEdit_191 = tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.place(x=180, y=200, width=350, height=25)



        GLabel_827 = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"
        GLabel_827["anchor"] = "w"
        GLabel_827["text"] = "Phone #"
        GLabel_827.place(x=30, y=250, width=150, height=25)



        GLineEdit_360 = tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"
        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"
        GLineEdit_360.place(x=180, y=250, width=350, height=25)



        GLabel_705 = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"
        GLabel_705["anchor"] = "w"
        GLabel_705["text"] = "Constituency"
        GLabel_705.place(x=30, y=300, width=150, height=25)



        GLineEdit_192 = tk.Entry(self)
        GLineEdit_192["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GLineEdit_192["font"] = ft
        GLineEdit_192["fg"] = "#333333"
        GLineEdit_192["justify"] = "center"
        GLineEdit_192["text"] = ""
        GLineEdit_192["relief"] = "solid"
        GLineEdit_192.place(x=180, y=300, width=350, height=25)



        GLabel_154 = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#333333"
        GLabel_154["bg"] = "#ffffff"
        GLabel_154["anchor"] = "w"
        GLabel_154["text"] = "Password"
        GLabel_154.place(x=30, y=350, width=150, height=25)



        GLineEdit_63 = tk.Entry(self, show="*")
        GLineEdit_63["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GLineEdit_63["font"] = ft
        GLineEdit_63["fg"] = "#333333"
        GLineEdit_63["justify"] = "center"
        GLineEdit_63["text"] = ""
        GLineEdit_63["relief"] = "solid"
        GLineEdit_63.place(x=180, y=350, width=350, height=25)



        fetchImagebtn = tk.Button(self)
        ft = tkfont.Font(family='Times', size=10)
        fetchImagebtn["font"] = ft
        fetchImagebtn["fg"] = "#ffffff"
        fetchImagebtn["bg"] = "#11595F"
        fetchImagebtn["justify"] = "center"
        fetchImagebtn["text"] = "Fetch Details"
        fetchImagebtn["relief"] = "solid"
        fetchImagebtn.place(x=180, y=400, width=80, height=25)
        fetchImagebtn["command"] = self.fetchbtn_command



        GButton_499 = tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times', size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Login"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=460, y=400, width=70, height=25)
        GButton_499["command"] = self.GButton_499_command



        self.labName = GLineEdit_191
        self.labName.config(state='readonly')
        self.labID = GLineEdit_360
        self.labID.config(state='readonly')
        self.voteParty = GLineEdit_63
        self.constituency = GLineEdit_192
        self.name = GLineEdit_361
        self.constituency.config(state='readonly')
        self.name.configure(state='readonly')
        '''
        self.cons = variable
        self.canvas = canvas
        self.candidates = variableCand
        self.candidatedd = candidatedropdown
        '''



    def func(self, value):
        from PIL import ImageTk, Image

        if str(value) == str("Pakistan Tehreek-e-Insaf (PTI)"):
            ab = Image.open("ImageResources/PTI.png")
        elif str(value) == str("Pakistan People's Party (PPP)"):
            ab = Image.open("ImageResources/PPP.png")
        elif str(value) == str("Pakistan Muslim League (Q) (PMLQ)"):
            ab = Image.open("ImageResources/PMLQ.png")
        elif str(value) == str("Pakistan Muslim League (N) (PMLN)"):
            ab = Image.open("ImageResources/PMLN.png")
        elif str(value) == str("Muttahida Qaumi Movement (MQM)"):
            ab = Image.open("ImageResources/MQM.png")
        elif str(value) == str("Jamiat-e-Ulema-e-Islam (JUI)"):
            ab = Image.open("ImageResources/JUI.png")
        elif str(value) == str("Jamaat-e-Islami Pakistan (JI)"):
            ab = Image.open("ImageResources/JI.png")
        elif str(value) == str("Awami National Party (ANP)"):
            ab = Image.open("ImageResources/ANP.png")
        else:
            ab = Image.open("ImageResources/default.png")

        im1 = ab.resize((75, 75))
        img = ImageTk.PhotoImage(im1)

        self.canvas.configure(image=img)
        self.canvas.image = img



    def fetchbtn_command(self):
        self.TrackImages()



    def GButton_499_command(self):
        if len(self.labName.get()) == 0 or len(self.labID.get()) == 0 or len(
                self.voteParty.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            self.SaveVoter()



    def assure_path_exists(self, path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)



    def check_haarcascadefile(self):
        exists = os.path.isfile("HaarFile\haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='Some file missing', message='Please contact us for help')



    def TrackImages(self):
        self.check_haarcascadefile()
        self.assure_path_exists("VotingData/")

        msg = ''
        self.i = 0
        j = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
        if exists3:
            recognizer.read("TrainingImageLabel\Trainner.yml")
        else:
            mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
            return
        harcascadePath = "HaarFile\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
        exists1 = os.path.isfile("VotingData\VoterData.csv")
        if exists1:
            df = pd.read_csv("VotingData\VoterData.csv")
        else:
            mess._show(title='Details Missing', message='Voter details are missing, please check!')
            cam.release()
            cv2.destroyAllWindows()
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                print("Serial Number: " + str(serial) + "\nConfig: " + str(conf))
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['SerialNumber'] == serial]['CNIC'].values

                    ID = df.loc[df['SerialNumber'] == serial]['PhoneNumber'].values
                    constituency2 = df.loc[df['SerialNumber'] == serial]['Constituency'].values

                    name = df.loc[df['SerialNumber'] == serial]['VoterName'].values
                    passWord = df.loc[df['SerialNumber'] == serial]['Password'].values
                    voterName2 = df.loc[df['SerialNumber'] == serial]['VoterName'].values

                    # cons = df.loc[df['SERIAL NO.'] == serial]['CONSTITUENCY'].values
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[1:-1]
                    constituency2 = str(constituency2)
                    name = str(name)
                    constituency2 = constituency2[2:-2]
                    name = name[2:-2]
                    voterName2 = str(voterName2)
                    voterName2 = voterName2[1:-1]
                    passWord = str(passWord)
                    passWord = passWord[1:-1]

                    # cons = str(cons)
                    # cons = cons[2:-2]


                else:
                    Id = 'Unknown'
                    bb = str(Id)
                cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('Face Matching', im)
            if (cv2.waitKey(1) == ord('q')):
                break

        def callback(*args):
            listOfCandidate = []
            with open("VotingData\CandidateData.csv", "r", newline='') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for line_num, content in enumerate(reader):
                    if content[6] == str(self.voteParty.get()) and content[0] == str(self.cons.get()):
                        listOfCandidate.append(content[2])
            f.close()
            prtyName = ""

            self.candidatedd.configure(state='active')
            self.candidatedd['menu'].delete(0, 'end')
            for fi in listOfCandidate:
                self.candidatedd['menu'].add_command(label=fi, command=lambda fi=fi: self.candidates.set(fi))

            cam.release()
            cv2.destroyAllWindows()
            f.close()

        self.labName.config(state='normal')
        self.labID.config(state='normal')
        self.constituency.config(state='normal')
        self.name.config(state='normal')

        self.labName.delete(0, 'end')
        self.labID.delete(0, 'end')
        self.constituency.delete(0, 'end')
        self.name.delete(0, 'end')

        self.labName.insert(0, bb)
        self.labID.insert(0, ID)
        self.labName.config(state='readonly')
        self.labID.config(state='readonly')
        self.constituency.insert(0, constituency2)
        self.name.insert(0, name)
        self.constituency.config(state='readonly')
        self.name.config(state='readonly')

        # self.voteParty.insert(0, cons)
        self.ID = ID
        self.bb = bb
        self.voterName2 = voterName2
        self.passWord = passWord
        self.constituency2 = constituency2
        listOfCandidate = []
        cam.release()
        cv2.destroyAllWindows()



    def SaveVoter(self):
        Password1 = ''
        passwordCorrect = False
        Constituency = ''
        Name = ''
        CNICNo = ''
        phoneNum = ''
        # serial=0
        Name = self.bb
        Password1 = self.passWord
        Constituency = self.constituency2
        CNICNo = self.voterName2
        CNICNo = str(CNICNo)
        CNICNo = CNICNo[1:-1]
        phoneNum = "+" + self.ID
        Pages.p = Constituency
        print(Pages.p)
        Pages.q = Name
        Pages.r = CNICNo

        df = pd.read_csv("VotingData\VoterData.csv")

        print("Cnic" + str(CNICNo))
        print("password" + str(Password1))
        print("Name" + str(Name))
        print("Const" + str(Constituency))

        if Password1 == str(self.voteParty.get()):
            passwordCorrect = True

        print("Name" + Name)
        # print(Constituency)
        Pages.p = Constituency
        print(Pages.p)
        Pages.q = Name
        Pages.r = CNICNo

        if passwordCorrect:
            self.otp = random.randint(1000, 9999)
            print("Your OTP is - ", self.otp)
            # Your Account Sid and Auth Token from twilio.com/console
            # DANGER! This is insecure. See http://twil.io/secure

            account_sid = 'ACb79268c2dda44f60f45b6e07405a978d'
            auth_token = '1f81bad21aa342f625960375efad6e5d'


            #uncoment these lines too

            # client = Client(account_sid, auth_token)
            # message = client.messages.create(
            #     body='Your Secure Device OTP is - ' + str(self.otp) + ' ',
            #     from_='+18329248439',
            #     to=str(phoneNum)
            # )


            password = tsd.askstring('OTP', 'Enter OTP', show='*')
            print(password)
            otp = self.otp
            print(otp)

            self.controller.show_frame("PageNine") #remove this line

            #uncoment these lines

            # if str(password) == str(otp):
            #     self.controller.show_frame("PageNine")
            # elif (password == None):
            #     mess._show(title='Null Error', message='OTP can not be null')
            # else:
            #     mess._show(title='Wrong OTP', message='You have entered wrong OTP')


        else:
            mess.showinfo("Failure", "No Record")
            print(self.labName.get())
            print(self.voteParty.get())



class PageNine(tk.Frame, Pages):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")



        GLabel_711 = tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times', size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0, y=0, width=600, height=40)



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711.place(x=0,y=450,width=600,height=20)



        GLabel_711 = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#1F323F"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "Please Cast Your Vote"
        GLabel_711.place(x=0, y=60, width=600, height=40)



        party = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        party["font"] = ft
        party["fg"] = "#333333"
        party["bg"] = "#ffffff"
        party["anchor"] = "w"
        party["text"] = "Party"
        party.place(x=30, y=150, width=130, height=25)



        from PIL import ImageTk, Image
        ab = Image.open("ImageResources/default.png")
        im1 = ab.resize((75, 75))
        img = ImageTk.PhotoImage(im1)

        canvas = tk.Label(self, bg="#ffffff", image=img)
        canvas.image = img
        canvas.place(x=450, y=150, width=75, height=75)



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
        variable.set("Select Party")
        partydropdown = tk.OptionMenu(self, variable, *OPTIONS, command=self.func)
        partydropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        partydropdown["font"] = ft
        partydropdown["fg"] = "#333333"
        partydropdown["justify"] = "center"
        partydropdown["text"] = "Entry"
        partydropdown["relief"] = "solid"
        partydropdown.place(x=180, y=150, width=250, height=25)



        candidate = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        candidate["font"] = ft
        candidate["fg"] = "#333333"
        candidate["bg"] = "#ffffff"
        candidate["anchor"] = "w"
        candidate["text"] = "Candidate"
        candidate.place(x=30, y=200, width=130, height=25)



        candidates = [
            ""
        ]
        variableCand = tk.StringVar(self)
        variableCand.set("")
        candidatedropdown = tk.OptionMenu(self, variableCand, *candidates)
        candidatedropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        candidatedropdown["font"] = ft
        candidatedropdown["fg"] = "#333333"
        candidatedropdown["justify"] = "center"
        candidatedropdown["text"] = ""
        candidatedropdown["relief"] = "solid"
        candidatedropdown.place(x=180, y=200, width=250, height=25)



        GButton_499 = tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times', size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Cast Vote"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=180, y=390, width=80, height=25)
        GButton_499["command"] = self.GButton_499_command



        returnButton = tk.Button(self)
        returnButton["bg"] = "#DD4F42"
        ft = tkfont.Font(family='Times', size=10)
        returnButton["font"] = ft
        returnButton["fg"] = "#ffffff"
        returnButton["justify"] = "center"
        returnButton["text"] = "Logout"
        returnButton["relief"] = "solid"
        returnButton.place(x=460,y=390,width=70,height=25)
        returnButton["command"] = self.returnButton_command



        self.cons = variable
        self.canvas = canvas
        self.candidates = variableCand
        self.candidatedd = candidatedropdown



    def returnButton_command(self):
        self.cons.set("Select Party")
        self.candidates.set("")
        self.controller.show_frame("VoterClass")



    def GButton_499_command(self):
        if ( self.candidates.get() !="" and self.cons.get()!="" and self.cons.get()!="Select Party"):
            self.SaveVoter()
        else:
            mess.showinfo("Please Fill all details","Some Data Missing")



    def SaveVoter(self):
        attendance = [str(Pages.q), '',Pages.r,'', Pages.p, '', self.cons.get(), '', self.candidates.get()]
        col_names = ['Id', '','Name','', 'Constituency', '', 'Party Voted', '', 'Candidate']

        exists = os.path.isfile("VotingData\ResultData.csv")
        VoterAlreadyExist = False
        if exists:
            with open("VotingData\ResultData.csv", "r", newline='\n') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for line_num, content in enumerate(reader):
                    if content[0] == str(Pages.q):
                        VoterAlreadyExist = True
                        break
            if not VoterAlreadyExist:
                with open("VotingData\ResultData.csv", 'a+', newline='') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(attendance)
                csvFile1.close()
                mess.showinfo("Vote Cast", "Your vote has been cast.")

                #self.candidatedd.delete(0, 'end')
            else:
                mess.showinfo("Failure", "You have already voted.")

        else:

            with open("VotingData\ResultData.csv", 'a+', newline='') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()

        # cam.release()
        cv2.destroyAllWindows()



    def func(self, value):
        from PIL import ImageTk, Image
        labName = Pages.p

        if str(value) == str("Pakistan Tehreek-e-Insaf (PTI)"):
            ab = Image.open("ImageResources/PTI.png")
        elif str(value) == str("Pakistan People's Party (PPP)"):
            ab = Image.open("ImageResources/PPP.png")
        elif str(value) == str("Pakistan Muslim League (Q) (PMLQ)"):
            ab = Image.open("ImageResources/PMLQ.png")
        elif str(value) == str("Pakistan Muslim League (N) (PMLN)"):
            ab = Image.open("ImageResources/PMLN.png")
        elif str(value) == str("Muttahida Qaumi Movement (MQM)"):
            ab = Image.open("ImageResources/MQM.png")
        elif str(value) == str("Jamiat-e-Ulema-e-Islam (JUI)"):
            ab = Image.open("ImageResources/JUI.png")
        elif str(value) == str("Jamaat-e-Islami Pakistan (JI)"):
            ab = Image.open("ImageResources/JI.png")
        elif str(value) == str("Awami National Party (ANP)"):
            ab = Image.open("ImageResources/ANP.png")
        else:
            ab = Image.open("ImageResources/default.png")

        im1 = ab.resize((75, 75))
        img = ImageTk.PhotoImage(im1)
        self.canvas.configure(image=img)
        self.canvas.image = img

        listOfCandidate = []
        with open("VotingData\CandidateData.csv", "r", newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for line_num, content in enumerate(reader):
                if content[6] == str(labName) and content[0] == str(self.cons.get()):
                    listOfCandidate.append(content[2])
        f.close()
        print(listOfCandidate)

        self.candidatedd.configure(state='active')
        self.candidatedd['menu'].delete(0, 'end')
        for fi in listOfCandidate:
            self.candidatedd['menu'].add_command(label=fi, command=lambda fi=fi: self.candidates.set(fi))

        f.close()

        def callback(*args):
            self.candidates.set('')
            listOfCandidate = []
            with open("VotingData\CandidateData.csv", "r", newline='') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for line_num, content in enumerate(reader):
                    if content[6] == str(labName) and content[0] == str(self.cons.get()):
                        listOfCandidate.append(content[2])
            f.close()
            #prtyName = ""
            print(listOfCandidate)

            self.candidatedd.configure(state='active')
            self.candidatedd['menu'].delete(0, 'end')
            for fi in listOfCandidate:
                self.candidatedd['menu'].add_command(label=fi, command=lambda fi=fi: self.candidates.set(fi))

            f.close()

        self.cons.trace("w", callback)



if __name__ == "__main__":
    app = SampleApp()
    app.title("Voter")
    app.mainloop()