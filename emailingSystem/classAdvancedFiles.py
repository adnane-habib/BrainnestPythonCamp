import os
from typing import List

class MYFiles:
     
    def __init__(self, mypath = os.getcwd()):
        try: 
            os.chdir(mypath)
                        
        except:
            print("invalid path")
            self.muFiles = []
        
        else:
            self.mypath = os.getcwd()
            self.myFiles = os.listdir(self.mypath)


    def getFiles(self):
            return self.myFiles

        
    def __str__(self):
            return "Files are: "+str(self.myFiles)


if __name__=='__main__':
    myFile = MYFiles(r"C:\Users\MedAdnane\AppData\Local\Programs\Python\Python37\myReports")
    print(*myFile.getFiles())
    print(myFile)


