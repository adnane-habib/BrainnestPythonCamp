import re
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from emailingSystem.classAdvancedFiles import MYFiles
from typing import List
import datetime
from datetime import datetime 




class MYEmail:
       
    senderEmail = "fsd.devops.adnane.habib@gmail.com"
    password = "vqvousbiitcyxopu"#input("Please enter your password: ")
    __defaultServer__ = 'smtp.gmail.com'
    __defaultServerPort__ = 587
    logFile = []
    
    html = ''' <html>
                <body>
                <h1> Periodic Reports </h1>
                <p1> Dear, Kindly find attached your report(s). </p>
                </body>
                </html>
            '''
    
    def __init__(self, account = (senderEmail, password), message = html, path = os.getcwd(), server = __defaultServer__ , port = __defaultServerPort__, logFile = []):
        #initializing the class and setting default values in case not provided
        self.senderEmail = account[0]
        self.password = account[1]
        self.message = message
        self.__defaultServer__ = server
        self.__defaultServerPort__ = port
        self.path = path
        self.logFile = logFile
  

    def setServer(self, server = __defaultServer__ , port = __defaultServerPort__):
        #A method to help settingserver settings
        self.__defaultServer__ = server
        self.__defaultServerPort__ = 587

    def displayServerSetings(self):
        #A method to help getting current server settings
        print("server is",self.__defaultServer__)
        print("port is",self.__defaultServerPort__)

    #loging to server and reporting catching error
    def serverLogin (self):
        try:
            self.smtpObj = smtplib.SMTP(self.__defaultServer__, self.__defaultServerPort__)
            self.smtpObj.starttls()
            self.smtpObj.login(self.senderEmail, self.password)
        except Exception as e:
            print("ERROR LOGIN\n")
            print("If you are using gmail, think about activating app passwords.")
            print("Visit your google account security settings, and activate 2-steps verification.")
            print("You can then activate app password and use it to access the app.")
            print(e)
            self.logFile.append("ERROR LOGIN")
            return False
        else:
            self.logFile.append("Logged in successfully")
            #print("Logged in successfully")
            return True
    #loging out from server and reporting catching error
    def serverLogout (self):
        try:            
            self.smtpObj.quit()
        except Exception as e:
            print("error logout")
            self.logFile.append("ERROR LOGOUT")
            print(e)
            return False
        else:
            #print("Logged out successfully")
            self.logFile.append("Logged out successfully")
            return True
    #Sending emails
    def sendEmail (self, recipient, message = html, mypath = None):
        #if mailing list, iterating through the list
        if type(recipient) == list:
            for element in recipient:
                self.sendEmailRecipient (recipient = element, message = message, mypath = mypath)
        else:
            self.sendEmailRecipent (recipient, message = message, mypath = mypath)            
       
    #mailing each element
    def sendEmailRecipient (self, recipient, message = html, mypath = None):
        #initially using directly smtplib, and then using MIME                    
        self.__sendingMIMEText__(recipient = recipient, message = message, mypath = mypath)
        return True
    





   #using MIME to send emails         
    def __sendingMIMEText__ (self, recipient, message = html, mypath = None):
        #checking emails validity
        def isValid(email):
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') 
            if re.fullmatch(regex, email):
                self.logFile.append("valid email address")
                return True
            else:
                self.logFile.append("invalid email address")
                return False
            
        #Managimg file attachement
        def attachFileEmail(email_message, fileName):
            self.logFile.append("attaching "+fileName)
            try:
                with open(fileName, "rb") as file:
                    fileAttachment = MIMEApplication(file.read())
                
                fileAttachment.add_header(
                    "Content-Disposition",
                    "attachment", filename = fileName)
                    
                email_message.attach(fileAttachment)
                #print("File "+fileName+" attached")
                self.logFile.append("valid attachment")
            except Exception as e:
                print("Error attaching file attachFileName method")
                self.logFile.append("invalid attachment")
                print(e)
                pass
        self.logFile.append("emailing "+recipient)    
        #ensuring that email address is valid     
        try:
            if not(isValid(recipient)):
                raise Exception
        except Exception as e:
            print(recipient,"is not valid email address")
        else:
            #formatting email
            email_message = MIMEMultipart()
            email_message['from'] = self.senderEmail
            email_message['To'] = recipient
            email_message['Subject'] = f" Periodic Reports"

            email_message.attach(MIMEText(message, "html"))

            #email_string = email_message.as_string()
            
            #trying to attach files via file lists
            if (mypath!=None):                
                try:
                    myFile = MYFiles(mypath)                    
                    for fileName in myFile.getFiles():                       
                        #print(fileName)
                        attachFileEmail(email_message, fileName)    
                except Exception as e:
                    print("Error adding attachment mypath is NONE")
                    print(e)
                    
            #trying to attach files via file lists                   
            email_string = email_message.as_string()

        #logging in, emailing and logging out
            try:            
                self.serverLogin()
                #self.smtpObj.sendmail(self.senderEmail, recipent, email_string)
                self.logFile.append("Email sent successfully")
            except Exception as e:
                print("Error sending email.")
                self.logFile.append("Error sending email")
                print(e)
                return False
            else:
                #print("Email sent successfully.")
                self.serverLogout()
                return True
            
        def printLogFile(self):
            print("printing log file")
            os.getcwd()
            myFile =  "LogFile"+datetime.now().strftime("%d_%m_%Y %H_%M_%S"+".txt")
            with open(myFile,'a') as fp:
                fp.write("Log file created on "+ datetime.now())
                for element in self.logFile:
                    fp.write("\n"+elment)
                fp.write('End of Log file')
                  
            





      
if __name__=='__main__':
    myEmail = MYEmail()
    myEmail.displayServerSetings()
    myEmail.sendEmail(["adnane_h.yahoo.fr", "adnanou.habibou@gmail.com", "fsd.devops.adnane.habib@gmail.com"], mypath = r"C:\Users\MedAdnane\AppData\Local\Programs\Python\Python37\myReports")


