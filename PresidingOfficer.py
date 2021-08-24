from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
from twilio.rest import Client
import random
import re
from _csv import writer
from tkinter import simpledialog
import pandas as pd
import operator

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
        for F in (PollingAgentClass, AddVoter):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PollingAgentClass")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class PollingAgentClass(tk.Frame):
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
        GLabel_711["text"] = "Presiding Officer"
        GLabel_711.place(x=0,y=60,width=600,height=40)



        GLabel_705=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"
        GLabel_705["anchor"] = "w"
        GLabel_705["text"] = "CNIC"
        GLabel_705.place(x=30,y=200,width=130,height=25)



        GLineEdit_191=tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.place(x=180,y=200,width=350,height=25)



        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"
        GLabel_827["anchor"] = "w"
        GLabel_827["text"] = "Password"
        GLabel_827.place(x=30,y=240,width=130,height=25)



        GLineEdit_360=tk.Entry(self,show="*")
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"
        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"
        GLineEdit_360.place(x=180,y=240,width=350,height=25)



        GLabel_154=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#333333"
        GLabel_154["bg"] = "#ffffff"
        GLabel_154["anchor"] = "w"
        GLabel_154["text"] = "Constituency"
        GLabel_154.place(x=30,y=280,width=130,height=25)



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
        GListBox_541["fg"] = "#000000"
        GListBox_541["justify"] = "center"
        GListBox_541["text"] = "Entry"
        GListBox_541["relief"] = "solid"
        GListBox_541.place(x=180,y=280,width=350,height=25)



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



        self.password = GLineEdit_360
        self.cnicNo = GLineEdit_191
        self.constituency = variable



    def GButton_629_command(self):
        print("command")


    def GButton_499_command(self):
        if len(self.password.get()) == 0 or len(self.cnicNo.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            PollingAgentAlreadyExist = False

            exists = os.path.isfile("VotingData\PresidingOfficerData.csv")

            if exists:
                with open("VotingData\PresidingOfficerData.csv", "r", newline='') as f:
                    reader = csv.reader(f, delimiter=',', quotechar='"')
                    for line_num, content in enumerate(reader):
                        if content[2] == str(self.cnicNo.get()) and content[4] == str(self.password.get()) and content[
                            8] == str(self.constituency.get()):
                            PollingAgentAlreadyExist = True
                            self.controller.show_frame("AddVoter")

                            # display msg to take photos first then save profile
                            mess.showinfo("Important",
                                          "1). If user is being registered on run time then you have to take photos first before saving the profile.\n\n2). If user images are already saved in training dataset then simply click on save profile button.")

                            self.cnicNo.delete(0, 'end')
                            self.password.delete(0, 'end')
                            break
                    if not PollingAgentAlreadyExist:
                        mess.showwarning("No Record", "Presiding Officer Does not Exist")

                    print("command")
                f.close()


class AddVoter(tk.Frame):
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
        GLabel_711["text"] = "Register New Voter"
        GLabel_711.place(x=0,y=60,width=600,height=40)



        nameLabel = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        nameLabel["font"] = ft
        nameLabel["fg"] = "#333333"
        nameLabel["bg"] = "#ffffff"
        nameLabel["anchor"] = "w"
        nameLabel["text"] = "Name"
        nameLabel.place(x=30, y=150, width=130, height=25)



        nameEntry = tk.Entry(self)
        nameEntry["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        nameEntry["font"] = ft
        nameEntry["fg"] = "#333333"
        nameEntry["justify"] = "center"
        nameEntry["text"] = ""
        nameEntry["relief"] = "solid"
        nameEntry.place(x=180, y=150, width=350, height=25)



        GLabel_705=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"
        GLabel_705["anchor"] = "w"
        GLabel_705["text"] = "Phone #"
        GLabel_705.place(x=30,y=190,width=130,height=25)



        GLineEdit_191=tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.insert(0, "+92")
        GLineEdit_191.place(x=180, y=190, width=350, height=25)



        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"
        GLabel_827["anchor"] = "w"
        GLabel_827["text"] = "CNIC"
        GLabel_827.place(x=30,y=230,width=130,height=25)



        GLineEdit_360=tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"
        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"
        GLineEdit_360.place(x=180,y=230,width=350,height=25)



        candidate = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        candidate["font"] = ft
        candidate["fg"] = "#333333"
        candidate["bg"] = "#ffffff"
        candidate["anchor"] = "w"
        candidate["text"] = "Constituency"
        candidate.place(x=30,y=270,width=130,height=25)



        OPTIONS = [
            "Attock-1(PP-1)",
            "Attock-1(PP-2)",
            "Attock-2(PP-3)",
            "Attock-2(PP-4)",
            "Attock-2(PP-5)"
        ]
        variable = tk.StringVar(self)
        variable.set(OPTIONS[0])
        candidatedropdown = tk.OptionMenu(self, variable, *OPTIONS)
        candidatedropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        candidatedropdown["font"] = ft
        candidatedropdown["fg"] = "#333333"
        candidatedropdown["bg"] = "#ffffff"
        candidatedropdown["justify"] = "center"
        candidatedropdown["text"] = ""
        candidatedropdown["relief"] = "solid"
        candidatedropdown.place(x=180,y=270,width=350,height=25)



        passWord = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        passWord["font"] = ft
        passWord["fg"] = "#333333"
        passWord["bg"] = "#ffffff"
        passWord["anchor"] = "w"
        passWord["text"] = "Password"
        passWord.place(x=30,y=310,width=130,height=25)



        passEntry = tk.Entry(self)
        passEntry["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        passEntry["font"] = ft
        passEntry["fg"] = "#333333"
        passEntry["justify"] = "center"
        passEntry["text"] = ""
        passEntry["relief"] = "solid"
        passEntry.place(x=180,y=310,width=350,height=25)



        takeImage = tk.Button(self)
        takeImage["bg"] = "#22B0BD"
        ft = tkfont.Font(family='Times', size=10)
        takeImage["font"] = ft
        takeImage["fg"] = "#ffffff"
        takeImage["justify"] = "center"
        takeImage["text"] = "Take Pictures"
        takeImage["relief"] = "solid"
        takeImage.place(x=40, y=370, width=90, height=25)
        takeImage["command"] = self.takeImage_command



        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Save Profile"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=140,y=370,width=90,height=25)
        GButton_499["command"] = self.GButton_499_command



        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#9ECED8"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#000"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Edit Voter"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=240,y=370,width=90,height=25)
        GButton_499["command"] = self.enterCnicDialog



        GButton_update=tk.Button(self)
        GButton_update["bg"] = "#9ECED8"
        ft = tkfont.Font(family='Times',size=10)
        GButton_update["font"] = ft
        GButton_update["fg"] = "#000"
        GButton_update["justify"] = "center"
        GButton_update["text"] = "Update"
        GButton_update["relief"] = "solid"
        GButton_update["command"] = self.updateVoter
        GButton_update.place_forget()



        GButton_49999=tk.Button(self)
        GButton_49999["bg"] = "#E2DF47"
        ft = tkfont.Font(family='Times',size=10)
        GButton_49999["font"] = ft
        GButton_49999["fg"] = "#000"
        GButton_49999["justify"] = "center"
        GButton_49999["text"] = "Delete Voter"
        GButton_49999["relief"] = "solid"
        GButton_49999.place(x=340,y=370,width=90,height=25)
        GButton_49999["command"] = self.deleteVoter



        returnButton = tk.Button(self)
        returnButton["bg"] = "#DD4F42"
        ft = tkfont.Font(family='Times', size=10)
        returnButton["font"] = ft
        returnButton["fg"] = "#ffffff"
        returnButton["justify"] = "center"
        returnButton["text"] = "Logout"
        returnButton["relief"] = "solid"
        returnButton.place(x=440, y=370, width=90, height=25)
        returnButton["command"] = self.returnButton_command



        profileStatus = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        profileStatus["font"] = ft
        profileStatus["fg"] = "#333333"
        profileStatus["bg"] = "#ffffff"
        profileStatus["justify"] = "center"
        # profileStatus["text"] = "1) Take Photo>>> 2) Save Profile"
        profileStatus["text"] = ""
        profileStatus.place(x=130, y=340, width=440, height=20)



        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711.place(x=0,y=450,width=600,height=20)



        self.name = nameEntry
        self.txt = GLineEdit_191
        self.txt2 = GLineEdit_360
        self.constituency = variable
        self.passWord = passEntry
        self.message1 = profileStatus



        self.editButton = GButton_499
        self.updateButton = GButton_update
        self.deleteButton = GButton_49999



    def returnButton_command(self):
        self.controller.show_frame("PollingAgentClass")



    def getImagesAndLabels(self,path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # create empth face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(ID)
        return faces, Ids



    def TrainImages(self):

        _serialNo = 0

        with open("VotingData/VoterData.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            for row in csv_reader:
                    print(row)

            try:
                string_array = str(row).replace('"', '').split(",")
                _serialNo = string_array[0].replace("'", "")
                _serialNo = str(int(_serialNo[1:]) + 1)
            except:
                _serialNo = 0

            print(_serialNo)
        csv_file.close()


        self.check_haarcascadefile()
        self.assure_path_exists("TrainingImageLabel/")
        columns = ['SerialNumber', '', 'PhoneNumber', '', 'CNIC', '', 'Constituency', '', 'VoterName', '', 'Password']
        self.assure_path_exists("VotingData/")
        self.assure_path_exists("TrainingImage/")
        exists = os.path.isfile("VotingData\VoterData.csv")

        # serial = -1
        # if exists:
        #     with open("VotingData\VoterData.csv", 'r', newline='') as csvFile1:
        #         reader1 = csv.reader(csvFile1)
        #         for l in reader1:
        #             serial = serial + 1
        #     # serial = (serial // 2)
        #     csvFile1.close()
        # else:
        #     with open("VotingData\VoterData.csv", 'a+', newline='') as csvFile1:
        #         writer = csv.writer(csvFile1)
        #         writer.writerow(columns)
        #     csvFile1.close()

        _phone = (self.txt.get())
        _cnic = (self.txt2.get())
        _cons = self.constituency.get()
        _name = self.name.get()
        _password = self.passWord.get()

        if (_cnic.isnumeric()):

            harcascadePath = "HaarFile\haarcascade_frontalface_default.xml"

            row = [str(_serialNo), '', _phone, '', _cnic, '', _cons, '', _name, '', _password]
            with open('VotingData\VoterData.csv', 'a+', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            self.txt.delete(0,'end')
            self.txt.insert(0, '+92')
            self.txt2.delete(0,'end')
            self.passWord.delete(0,'end')
            self.name.delete(0,'end')
        else:
            if (_cnic.isnumeric() == False):
                mess.showwarning("Enter Correct CNIC")
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "HaarFile\haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, ID = self.getImagesAndLabels("TrainingImage")
        try:
            recognizer.train(faces, np.array(ID))
        except:
            mess._show(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.save("TrainingImageLabel\Trainner.yml")
        # res = "Profile Saved Successfully"
        res = ""
        mess._show(title='Successful', message='Voter is successfully added.')

        self.message1.configure(text=res)
        #self.message.configure(text='Total Registrations till now  : ' + str(ID[0]))



    def assure_path_exists(self,path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)



    def check_haarcascadefile(self):
        exists = os.path.isfile("HaarFile\haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='Some file missing', message='Please contact us for help')
            # window.destroy()



    def TakeImages(self):

        _serialNo = 0

        with open("VotingData/VoterData.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            for row in csv_reader:
                    print(row)

            try:
                string_array = str(row).replace('"', '').split(",")
                _serialNo = string_array[0].replace("'", "")
                _serialNo = str(int(_serialNo[1:]) + 1)
            except:
                _serialNo = 0

            print(_serialNo)
        csv_file.close()

        self.check_haarcascadefile()
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME', '', 'CONSTITUENCY','','VOTERNAME','','PASSWORD']
        self.assure_path_exists("VotingData/")
        self.assure_path_exists("TrainingImage/")
        # serial = -1
        #
        # exists = os.path.isfile("VotingData\VoterData.csv")
        # if exists:
        #     with open("VotingData\VoterData.csv", 'r', newline='') as csvFile1:
        #         reader1 = csv.reader(csvFile1)
        #         for l in reader1:
        #             serial = serial + 1
        #     # serial = (serial // 2)
        #     csvFile1.close()
        # else:
        #     with open("VotingData\VoterData.csv", 'a+', newline='') as csvFile1:
        #         writer = csv.writer(csvFile1)
        #         writer.writerow(columns)
        #         # serial = 1
        #     csvFile1.close()
        name = (self.txt2.get())
        con = self.constituency.get()
        voterName = self.name.get()
        passWord = self.passWord.get()

        name = (self.txt2.get())
        Id = (self.txt.get())

        # print("Serial Number For Images: " + str(serial))

        if ((name.isnumeric()) ):
            cam = cv2.VideoCapture(0)
            harcascadePath = "HaarFile\haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ " + name + "." + str(_serialNo) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    # display the frame
                    cv2.imshow('Taking Images', img)
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 30
                elif sampleNum > 30:
                    break
            cam.release()
            cv2.destroyAllWindows()
            # res = "Images Taken for ID : " + Id
            res = ""
            '''
            #row = [serial, '', Id, '', name, '', con,'',voterName,'',passWord]
            with open('VotingData\VoterData.csv', 'a+', newline='') as csvFile:
                print("")
                #writer = csv.writer(csvFile)
                #writer.writerow(row)
            csvFile.close()
           '''
            self.message1.configure(text=res)
        else:
            if (name.isnumeric() == False):
                res = "Enter Correct name"
                mess.showwarning(res,"Incorrect Name")



    def psw(self):
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
        #     to=str(self.txt.get())
        # )

        self.assure_path_exists("TrainingImageLabel/")
        exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
        if exists1:
            tf = open("TrainingImageLabel\psd.txt", "r")
            key = tf.read()
        else:
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
            else:
                tf = open("TrainingImageLabel\psd.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered', message='New password was registered successfully!!')
                return
        password = tsd.askstring('OTP', 'Enter OTP', show='*')
        print(password)
        otp=self.otp
        print(otp)

        self.TrainImages() #remove this line

        #uncoment these lines

        # if str(password) == str(otp):
        #     self.TrainImages()
        # elif (password == None):
        #     mess._show(title='Null Error', message='OTP can not be null')
        # else:
        #     mess._show(title='Wrong OTP', message='You have entered wrong OTP')



    def takeImage_command(self):

        # /////////////// sorting file before adding new voter ////////////////
        allRows = []
        fileToSort = open("VotingData\VoterData.csv", 'r')
        csvFileReader = csv.reader(fileToSort, delimiter = ',')
        sortedFile = sorted(csvFileReader, key = operator.itemgetter(0))
        sortedFile = sortedFile[-1:] + sortedFile[:-1]
        # print(sortedFile)
        for eachLine in sortedFile:
            allRows.append(eachLine)
        updateFile("VotingData\VoterData.csv", allRows)
        # /////////////////////////////////////////////////////////////////////


        regex = "(\+\w{5})\w{7}"
        if len(self.txt.get()) == 0 or len(self.txt2.get()) == 0 or len(self.constituency.get()) == 0 or len(
                self.name.get()) == 0 or len(self.passWord.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            if not re.search(regex, str(self.txt.get())) or len(self.txt.get()) != 13:
                mess.showwarning("Wrong Phone Number", "Please enter a valid phone number.\n\nFor Example: +923001234567")
            else:
                if len(self.txt2.get()) != 13:
                    mess.showwarning("CNIC Warning", "Please enter a 13 digit CNIC without dashes\nYou entered "
                                     + str(len(self.txt2.get())) + " digit CNIC")
                else:
                    CNICExists=False
                    serial = -1
                    with open("VotingData\VoterData.csv", "r") as f:
                        reader = csv.reader(f)
                        for l in reader:
                            serial = serial + 1
                        # serial = (serial // 2)
                        for line_num, content in enumerate(reader):
                            if content[4] == str(self.txt2.get()):
                                CNICExists=True

                                break
                    f.close()
                    if CNICExists==False:
                        self.TakeImages()
                    else:
                        mess.showinfo("Already Exists","User Exists")



    def GButton_520_command(self):
        self.controller.show_frame("ElectionCommisionClass")



    def GButton_629_command(self):
        self.controller.show_frame("PollingAgentClass")



    def GButton_737_command(self):
        self.controller.show_frame("VoterClass")



    def GButton_499_command(self):
        regex = "(\+\w{5})\w{7}"
        if len(self.txt.get()) == 0 or len(self.txt2.get()) == 0 or len(self.constituency.get()) == 0 or len(
                self.name.get()) == 0 or len(self.passWord.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            if not re.search(regex, str(self.txt.get())) or len(self.txt.get()) != 13:
                mess.showwarning("Wrong Phone Number",
                                 "Please enter a valid phone number.\n\nFor Example: +923001234567")
            else:
                if len(self.txt2.get()) != 13:
                    mess.showwarning("CNIC Warning", "Please enter a 13 digit CNIC without dashes\nYou entered "
                                     + str(len(self.txt2.get())) + " digit CNIC")
                else:
                    serial = 0
                    CNICExists = False
                    with open("VotingData\VoterData.csv", "r") as f:
                        reader = csv.reader(f)
                        for l in reader:
                                serial = serial + 1
                        serial = (serial // 2)
                        for line_num, content in enumerate(reader):
                            if content[4] == str(self.txt2.get()):
                                CNICExists = True
                                break
                    f.close()
                    if len(self.txt.get()) == 0 or len(self.txt2.get()) == 0 or CNICExists==True :
                        mess.showwarning("Incomplete Data", "Please Fill all Details")
                    else:
                        self.psw()

    def enterCnicDialog(self):
        cnic = simpledialog.askstring("Voter's CNIC", "Please enter your CNIC as a Voter.")

        if (len(cnic) == 13):
            _count = 0
            allRows = []
            exists = os.path.isfile("VotingData/VoterData.csv")
            if exists:
                with open("VotingData/VoterData.csv", "r") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                    for row in csv_reader:
                        if len(row) != 0:
                            if row[4] == cnic:
                                _count += 1
                                print(row)

                                string_array = str(row).replace('"', '').split(",")

                                _phone = string_array[2].replace("'", "")

                                _cnic = string_array[4].replace("'", "")

                                _cons = string_array[6].replace("'", "")

                                _name = string_array[8].replace("'", "")

                                _password = string_array[10].replace("'", "")
                                _password = _password[:-1]

                                print("Name: " + _name + "\nCNIC: " + _cnic +"\nPassword: " + _password + "\nPhone: " + _phone)

                                self.name.delete(0, 'end')
                                self.txt.delete(0, 'end')
                                self.txt2.delete(0, 'end')
                                self.passWord.delete(0, 'end')

                                self.name.insert(0, _name.lstrip())
                                self.txt.insert(0, _phone.strip())
                                self.txt2.insert(0, _cnic.strip())
                                self.txt2.configure(state='disabled')
                                self.constituency.set(_cons.strip())
                                self.passWord.insert(0, _password.strip())

                                print("Done")
                                self.editButton.place_forget()
                                self.updateButton.place(x=240, y=370, width=90, height=25)

                csv_file.close()

                if (_count < 1):
                    mess._show(title='No Record', message='No record found with this CNIC')
                    return ()

    def updateVoter(self):
        _count = 0

        # ///////////////first we will delete the previous record///////////////////
        name = self.name.get()
        phone = self.txt.get()
        cnic = self.txt2.get()
        cons = self.constituency.get()
        password = self.passWord.get()

        nameLength = len(name)
        phoneLength = len(phone)
        cnicLength = len(cnic)
        passwordLength = len(password)

        if nameLength == 0 or phoneLength == 0 or cnicLength == 0 or passwordLength == 0:
            mess.showwarning("Incomplete Data", "Please fill all fields" + "\n Name Length: " + str(nameLength) + "\n Phone Length: " + str(phoneLength) +
                             "\n CNIC Length: " + str(cnicLength) + "\n Password Length: " + str(passwordLength))
        else:
            if phoneLength == 13:
                allRows = []
                exists = os.path.isfile("VotingData/VoterData.csv")
                if exists:
                    with open("VotingData/VoterData.csv", "r") as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                        for row in csv_reader:
                            if row[4] == cnic:
                                print(row)

                                string_array = str(row).replace('"', '').split(",")
                                _serialNo = string_array[0].replace("'", "")
                                _serialNo = _serialNo[1:]

                                print(_serialNo)
                                _count += 1
                            else:
                                allRows.append(row)
                    csv_file.close()
                if (_count > 0):
                    updateFile("VotingData/VoterData.csv", allRows)

                    # ////////////////// Now adding new record as updated record///////////////////////////////////////////////
                    columns = ['SerialNumber', '', 'PhoneNumber', '', 'CNIC', '', 'Constituency', '', 'VoterName', '',
                               'Password']
                    # exists = os.path.isfile("VotingData\VoterData.csv")
                    # serial = -1
                    # if exists:
                    #     with open("VotingData\VoterData.csv", 'r', newline='') as csvFile1:
                    #         reader1 = csv.reader(csvFile1)
                    #         for l in reader1:
                    #             serial = serial + 1
                    #     # serial = (serial // 2)
                    #     csvFile1.close()
                    # else:
                    #     with open("VotingData\VoterData.csv", 'a+', newline='') as csvFile1:
                    #         writer = csv.writer(csvFile1)
                    #         writer.writerow(columns)
                    #         serial = 1
                    #     csvFile1.close()

                    _Id = phone
                    _name = cnic
                    _con = cons
                    _voterName = name
                    _passWord = password

                    row = [_serialNo, '', _Id, '', _name, '', _con, '', _voterName, '', _passWord]
                    with open('VotingData\VoterData.csv', 'a+', newline='') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(row)
                    csvFile.close()

                    mess._show(title='Voter Updated', message='Voter successfully update.')

                    # /////////////// sorting file before adding new voter ////////////////
                    allRows = []
                    fileToSort = open("VotingData\VoterData.csv", 'r')
                    csvFileReader = csv.reader(fileToSort, delimiter=',')
                    sortedFile = sorted(csvFileReader, key=operator.itemgetter(0))
                    sortedFile = sortedFile[-1:] + sortedFile[:-1]
                    print(sortedFile)
                    for eachLine in sortedFile:
                        allRows.append(eachLine)
                    updateFile("VotingData\VoterData.csv", allRows)
                    # /////////////////////////////////////////////////////////////////////

                    self.name.delete(0, 'end')
                    self.txt.delete(0, 'end')
                    self.txt.insert(0, '+92')
                    self.txt2.configure(state='normal')
                    self.txt2.delete(0, 'end')
                    self.passWord.delete(0, 'end')

                    self.editButton.place(x=240, y=370, width=90, height=25)
                    self.updateButton.place_forget()
                    # /////////////////////////////////////////////////////////////////////////////////////////////////////////

                else:
                    mess._show(title='No Record', message='There is no user existed with this CNIC.')


                    self.name.delete(0, 'end')
                    self.txt.delete(0, 'end')
                    self.txt.insert(0, '+92')
                    self.txt2.configure(state='normal')
                    self.txt2.delete(0, 'end')
                    self.passWord.delete(0, 'end')

                    self.editButton.place(x=240, y=370, width=90, height=25)
                    self.updateButton.place_forget()
            elif (phoneLength != 13):
                mess._show(title='Length Error', message='Please enter a valid phone number.\nLike +923001234567')
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////



    def deleteVoter(self):

        cnic = self.txt2.get()
        cnicLength = len(cnic)

        # mess._show(title = 'CNIC', message = 'CNIC: ' + cnic + '\nCNIC Length: ' + str(cnicLength))

        _count = 0
        if cnicLength == 0:
            mess.showwarning("Incomplete Data", "CNIC is must.")
        else:
            if cnicLength == 13:
                allRows = []
                exists = os.path.isfile("VotingData/VoterData.csv")
                if exists:
                    with open("VotingData/VoterData.csv") as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                        for row in csv_reader:
                            if row[4] == cnic:
                                print(row)
                                _count += 1
                            else:
                                allRows.append(row)
                    csv_file.close()
                if (_count > 0):
                    updateFile("VotingData/VoterData.csv", allRows)
                    mess._show(title='User Deleted', message='User has been deleted successfully.')

                    self.name.delete(0, 'end')
                    self.txt.delete(0, 'end')
                    self.txt.insert(0, '+92')
                    self.txt2.configure(state='normal')
                    self.txt2.delete(0, 'end')
                    self.passWord.delete(0, 'end')

                    self.editButton.place(x=240, y=370, width=90, height=25)
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



if __name__ == "__main__":
    app = SampleApp()
    app.title("Presiding Officer")
    app.mainloop()