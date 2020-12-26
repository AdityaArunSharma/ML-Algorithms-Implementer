
from tkinter import *
from tkinter import StringVar, ttk
import tkinter  
import tkinter.messagebox
import tkinter as tk
from numpy.core.fromnumeric import choose
from linearRegression import LinearRegression
from polynomialRegression import PolynomialRegression
from logisticRegression import LogisticRegression
from supportVectorMachine import SupportVectorMachine
from kMeansClustering import kMeansClustering


class Home:
    selectedDataFilePath = ""
    selectedAlgo = ""  
    
    def main(self):
        yPosition_chooseAlgo_label = 30
        xPosition_chooseAlgo_label = 100
        
        dropDownListItems = [
                                    "Linear Regression",
                                    "Polynomial Regression",                                
                                    "Logistic Regression",
                                    "Support Vector Machine",
                                    "K Means Clusturing"]
        app = tk.Tk()
        app.geometry("300x400")        
        app.minsize(340,500)
        chooseAlgo_label = tk.Label(app,text="Choose the ML Algorithm")
        chooseAlgo_label.place(x=xPosition_chooseAlgo_label,y=yPosition_chooseAlgo_label,width=150,height=25)
        dropDownMenu = ttk.Combobox(app,values=dropDownListItems,
                                            state="readonly")
        dropDownMenu.place(x=xPosition_chooseAlgo_label,y=yPosition_chooseAlgo_label+40,width=150,height=25)
        def dropDownItemClicked(event):            
            self.selectedAlgo = dropDownMenu.get()
            print("Selected Algo : ",self.selectedAlgo)
    
        dropDownMenu.bind("<<ComboboxSelected>>",dropDownItemClicked)

  


        chooseData_label = tk.Label(app,text="Upload Data File")
        chooseData_label.place(x=xPosition_chooseAlgo_label+15,y=yPosition_chooseAlgo_label+160,width=120,height=25)


        selectedFileLabel_text = StringVar()
        selectedFileLabel_text.set("")
        selectedFile_label = tk.Label(app,textvariable=selectedFileLabel_text)
        selectedFile_label.place(x=0,y=yPosition_chooseAlgo_label+250,width=300,height=25)


        from tkinter import filedialog

        def uploadButtonClicked(event=None):            
            filename = filedialog.askopenfilename()
            if(filename):
                index = filename.rfind(".")
                fileType = filename[index+1:len(filename)]
                if(fileType!="csv"):
                    tkinter.messagebox.showinfo('Error!','Only CSV format supported')
                    return

            if(filename):
                self.selectedDataFilePath = filename
                index_lastSlash = self.selectedDataFilePath.rfind("/")
                selectedFileName = self.selectedDataFilePath[index_lastSlash+1:len(self.selectedDataFilePath)]
                selectedFileLabel_text.set("Selected Data File : "+selectedFileName)
                print('Selected : ', selectedFileName)

        button = tk.Button(app, text='Upload', command=uploadButtonClicked)
        button.place(x=xPosition_chooseAlgo_label+45,y=yPosition_chooseAlgo_label+200,width=50,height=25)

        def startButtonClicked(event=None):    
           
            if(not self.selectedAlgo):
                tkinter.messagebox.showinfo('Error!','Please Select a algorithm to proceed')
                return
            if(not self.selectedDataFilePath):
                tkinter.messagebox.showinfo('Error!','Please Select a Data File to proceed')
                return

            print("Algorithm selected : ",self.selectedAlgo)
            print("File selected      : ",self.selectedDataFilePath)
            if(self.selectedAlgo==dropDownListItems[0]):
                lR = LinearRegression()
                lR.main(self.selectedDataFilePath)
            if(self.selectedAlgo==dropDownListItems[1]):
                pR = PolynomialRegression()
                pR.main(self.selectedDataFilePath)
            if(self.selectedAlgo==dropDownListItems[2]):
                lR = LogisticRegression()
                lR.main(self.selectedDataFilePath)
            if(self.selectedAlgo==dropDownListItems[3]):
                SupportVectorMachine().main(self.selectedDataFilePath)
            if(self.selectedAlgo==dropDownListItems[4]):
                kMeansClustering().main(self.selectedDataFilePath)


        start_button = tk.Button(app,text="Proceed",command=startButtonClicked)
        start_button.place(x=70,y=yPosition_chooseAlgo_label+300,width=200,height=25)

        app.title("ML Algorithms Implementer")
        app.mainloop()