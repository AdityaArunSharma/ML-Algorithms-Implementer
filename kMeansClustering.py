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


class kMeansClustering:
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

        
        new_x = width/4
        new_y = yPosition

        featureName=[]
        for x in df.columns:
            featureName.append(x)
   
        
        label_targetValue = Label(app,text="Select Target Variable")
        yPosition+=30
        label_targetValue.place(x=width/20,y=yPosition,width=200,height=15)
        
        dropDownMenu = ttk.Combobox(app,values=featureName,
                                            state="readonly")
        yPosition+=20
        dropDownMenu.place(x=width/12,y=yPosition,width=150,height=25)

        yPosition+=30
        selectClusters_label = Label(app,text="Select number of clusters")
        selectClusters_label.place(x=width/20,y=yPosition,width=250,height=25)
        yPosition+=30
        numberOfClusters_textfeild = Text(app)        
        numberOfClusters_textfeild.place(x=width/12,y=yPosition,width=50,height=22)


        selectXaxisValue_label = Label(app,text="Select feature")
        yPosition+=30
        selectXaxisValue_label.place(x=width/20,y=yPosition,width=300,height=25)

        selectXaxisValue_dropdownMenu = ttk.Combobox(app,values=featureName,state="readonly")
        yPosition+=30
        selectXaxisValue_dropdownMenu.place(x=width/20,y=yPosition,width=200,height=25)

        def RepresentsInt(s):
            try: 
                int(s)
                return True
            except ValueError:
                return False

        

        
        
        def predictFutureButtonClicked(event=None):

            # global var
            
            if(not RepresentsInt(numberOfClusters_textfeild.get("1.0", "end-1c"))):
                tkinter.messagebox.showinfo('Error!','Wrong input for number of clusters')
                return

            if(not selectXaxisValue_dropdownMenu.get()):
                tkinter.messagebox.showinfo('Error!','Select feature')
                return
       
            self.selectedTargetVairable = dropDownMenu.get()
            if(not self.selectedTargetVairable):
                tkinter.messagebox.showinfo('Error!','Select a target variable first')
                return        
            performkMeans()


        predictFutureButton = tk.Button(app,text="Predict the Future",command=predictFutureButtonClicked)    
        yPosition+=40
        predictFutureButton.place(x=width/3,y=yPosition,width=350,height=25)

        def performkMeans():
            

           x = df[selectXaxisValue_dropdownMenu.get()]
           y = df[self.selectedTargetVairable]
           newDf = df[[selectXaxisValue_dropdownMenu.get(),self.selectedTargetVairable]].copy()         

           from sklearn.cluster import KMeans

           kmeans = KMeans(n_clusters=int(numberOfClusters_textfeild.get("1.0", "end-1c"))).fit(newDf)
           centroids = kmeans.cluster_centers_

           plt.scatter(x,y,c = kmeans.labels_.astype(float),s=50,alpha=0.5)
           plt.scatter(centroids[:,0],centroids[:,1],c="red",s=50)
           plt.show()



           return        
            
        app.title("K Means Clustering")
        app.mainloop()
