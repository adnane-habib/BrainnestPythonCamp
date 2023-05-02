from emailingSystem.classMIMEEmail import MYEmail


        

if __name__=='__main__':
    #username = input("Enter your email username\n")
    #password = input("Enter your email password\n")
    myEmail = MYEmail()
    myEmail.serverLogin()
    myEmail.serverLogout()
    #myEmail.displayServerSetings()
    #myEmail.sendEmail(["adnane_h.yahoo.fr", "adnanou.habibou@gmail.com", "fsd.devops.adnane.habib@gmail.com"], mypath = r"C:\Users\MedAdnane\AppData\Local\Programs\Python\Python37\myReports")
    #myFile = MYFiles(r"C:\Users\MedAdnane\AppData\Local\Programs\Python\Python37\myReports")
    #for file in myFile.getFiles():
        #displayFileEmail(file)
    #print(myEmail.logFile)
    myEmail.printLogFile()
