from tkinter import *
from tkinter import StringVar, ttk
import tkinter  
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter.messagebox
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 


class SupportVectorMachine:
    selectedFeatures=[]
    selectedTargetVairable=""
    score=0    

    def main(self,dataPath):
        app = tk.Tk()
        cellSize = 15
        df = pd.read_csv(dataPath)
        df = df.dropna()
        numberColumns = len(df.columns)
        width = cellSize*numberColumns*10
        height = 500
        app.minsize(width,height)

        yPosition = 10

        label_textFeild = Label(app,text="Peek to Selected Data frame")
        label_textFeild.place(x=width/12,y=yPosition,width=155,height=15)


        textHeight = 5*25
        textFeild = Text(app,height=int(textHeight),width=int(width*0.8))
        yPosition+=25
        textFeild.place(x=width/12,y=yPosition,width=width*0.8,height=textHeight)        
        textFeild.insert(tk.END,df.head(5))
        yPosition+=textHeight


        label_checkBox = Label(app,text="Select the Features")
        yPosition+=10
        label_checkBox.place(x=width/12,y=yPosition,width=100,height=15)

        yPosition+=20
        checkBoxCount=[]
        for x in range(numberColumns):
            checkBoxCount.append(False)
        c=[]
        var=[]
        
        for x in range(numberColumns):
            var.append(tk.IntVar(app))
        
        
        
        
        def checkBoxClicked():                                  
            print("Check box clicked ",)

        
        new_x = width/4
        new_y = yPosition

        featureName=[]
        for x in df.columns:
            featureName.append(x)
        


        for x in range(numberColumns):
            if(x>5):
                c.append(tk.Checkbutton(app,text=featureName[x],variable=var[x],onvalue=1,offvalue=0,command=checkBoxClicked))
                c[x].place(x=new_x,y=new_y,width=200,height=15)
                new_y+=20
                continue
            c.append(tk.Checkbutton(app,text=featureName[x],variable=var[x],onvalue=1,offvalue=0,command=checkBoxClicked))
            c[x].place(x=width/12,y=yPosition,width=200,height=15)
            yPosition+=20
        
        
        label_targetValue = Label(app,text="Select Target Variable")
        yPosition+=30
        label_targetValue.place(x=width/20,y=yPosition,width=200,height=15)
        
        dropDownMenu = ttk.Combobox(app,values=featureName,
                                            state="readonly")
        yPosition+=20
        dropDownMenu.place(x=width/12,y=yPosition,width=150,height=25)

        yPosition+=30
        selectKernel_label = Label(app,text="Select kernel")
        selectKernel_label.place(x=width/12,y=yPosition,width=100,height=25)

        yPosition+=30
        kernelName = ["Gaussian Kernel Radial Basis Function",
                        "Sigmoid",
                        "Polynomial",
                        "Linear"]
        kernelCode = ["rbf",
                        "sigmoid",
                        "poly",
                        "linear"]
        selectKernel_dropDownMenu = ttk.Combobox(app,values=kernelName,
                                            state="readonly")
        selectKernel_dropDownMenu.place(x=width/20,y=yPosition,width=200,height=25)
        
        
        def predictFutureButtonClicked(event=None):

            # global var
           
        
            for x in range(numberColumns):
                if(var[x].get()==1):
                    
                    self.selectedFeatures.append(featureName[x])
            
            self.selectedTargetVairable = dropDownMenu.get()
            if(not self.selectedTargetVairable):
                tkinter.messagebox.showinfo('Error!','Select a target variable first')
                return
            if(len(self.selectedFeatures)==0):
                tkinter.messagebox.showinfo('Error!','Select atleast one feature')
                return
            if( not selectKernel_dropDownMenu.get()):
                tkinter.messagebox.showinfo('Error!','Select a kernel')
            performSVM()


        predictFutureButton = tk.Button(app,text="Predict the Future",command=predictFutureButtonClicked)    
        yPosition+=40
        predictFutureButton.place(x=width/3,y=yPosition,width=350,height=25)

        def performSVM():
            
            index=-1
            for x in range(len(kernelName)):
                if(kernelName[x]==selectKernel_dropDownMenu.get()):
                    index=x
                    break
            
            if(index==-1):
                return

            x = df[self.selectedFeatures]
            y = df[self.selectedTargetVairable]
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
            from sklearn.preprocessing import StandardScaler
            sc_x = StandardScaler()
            x_train = sc_x.fit_transform(x_train)
            from sklearn.svm import SVC
            svc = SVC(kernel=kernelCode[index],random_state=0)
            svc.fit(x_train,y_train)

            accuracy = svc.score(sc_x.transform(x_test),y_test)*100
            message = "Model predicted with " + str(accuracy) + " % accuracy"
            tkinter.messagebox.showinfo('Success!',message)

            
            


            return        
            
        app.title("Support Vector Machine")
        app.mainloop()


# lr = LinearRegression()
# lr.main("C:/Users/chunc/OneDrive/Computer Science and Engineering/Codes/Python/HouseData.csv")