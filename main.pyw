########################################################### CREDITS ##############################################################################################

'''
                                                  WELCOME TO THE calorie_tracker

         THIS PROGRAM CALCULATES THE NUMBER OF CALORIES A USER HAS BURNED DURING A WORKOUT, SHOWS THEM AND STORES THEM IN A CSV

                                                    MADE BY : ARYAN RATHORE 
                                            COMPUTER SCIENCE ENGINEER AT VIT BHOPAL

                                                        CONTACT INFO
                                                aryanrathore13572002@gmail.com
                                               aryan.rathore2021@vitbhopal.ac.in
                                          github :- https://github.com/aryanrathore1012
                                    LINKEDIN - https://www.linkedin.com/in/aryan-rathore-b15459215/
'''

########################################################### IMPORTS ##############################################################################################

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as tmsg
import numpy as np
import pandas as pd
from xgboost import XGBRegressor
import datetime as dt
from tkinter import ttk
from csv import DictWriter

########################################################### FUNCTIONS ###################################################################0#########################

'''                                                             IMPORTANT NOTE                                                              
                                  BEFORE YOU RUN THE PROGRAM MAKE SURE YOU READ AND FOLLOW THE LINES BELOW  
                                                       OTHERWISE THE PROGRAM WONT RUN                                                      '''

# 1

'''          THERE ARE IN TOTAL OF 4 FUNCTIONS THAT CALL EACH OTHER, "EVERY FUNCTION HAS A DOCSTRING LIKE THIS SPECIFIES WHAT THAT FUNCTION DOES
                                                        AND HOW THE THE FUNCTION WORKS"                                                      '''
# 2

'''   MAKE SURE YOU READ THE "calorie_exercise_workout_model_analysis.ipynb" BEFORE USING THIS AS IT HAS THE INFO ON THE DATA
                                               AND WHY USED THE XGBREGRESSOR FOR MY PREDICTIONS                                         '''

# 3

'''   I HAVE TO SPECIFY A FILE PATH TO read the data from (WORKOUT.CSV, workout_logs.csv and all the images and icons) FILES IF 
    YOU ARE USING OR COPY PASTING MY CODE MAKE YOU CHANGE THE FILE PATHS I HAVE SPECIFIED WHICH FUNCTIONS NEED A 'FILE PATH CHANGE' 
                                                    SO MAKE SURE YOU CHANGE THEM FIRST '''

# 4

'''
                  ||||||| JUST CHANGE THE FILE PATHS FROM LINE 80 TO 83 AND YOU CAN RUN THE PROGRAM FOR YOURSELF |||||||
'''
            
class calorie_predictor:

# _________________________________________________________________________________________________________________________________________


# 1 this is runs first and initializes everything


    def __init__(self): # CHANGE FILE PATHS IN THIS FUNCTION LINE (80 - 83)

        '''
            This function reads the workout.csv and uses the data to train the XGBRegressor model (There is no need to test the model as i have
            already done it in the "calorie_exercise_workout_model_analysis.ipynb" before)

            0. initialize the path variables
            1. reads the data from the workouts.csv
            2. makes the XGBRegressor and feeds all the data and makes path and object variables
            3. runs the main_window function

        '''
        

        # path variables (you will have to change these paths in order to run the program)
        self.workout_csv_path = "F://aryans_code_notes//machine_learning//calorie_predictor//workout.csv"
        self.icon_path = "F://aryans_code_notes//machine_learning//calorie_predictor//calorie_icon.ico"
        self.calorie_img_path = "F://aryans_code_notes//machine_learning//calorie_predictor//calorie_img.png"
        self.workout_logs_csv_path = "F://aryans_code_notes//machine_learning//calorie_predictor//workout_logs.csv"

        # -------------------------------------------------------------------------------------------------------
        # 1. reads the data from the workouts.csv

        try:
            workout_df = pd.read_csv(self.workout_csv_path)
            workout_df.drop(columns=workout_df.columns[0], axis=1,  inplace=True)
        except:
            tmsg.showerror("read error", "Could'nt read the workouts.csv")
            quit()

        # -------------------------------------------------------------------------------------------------------
        # 2. makes the XGBRegressor and feeds all the data and makes path and object variables

        X = workout_df.drop(columns=["Calories", "User_ID"])
        Y = workout_df[["Calories"]]

        # object variables
        self.XGBR_model = XGBRegressor().fit(X, Y)
        self.XGBR_model_r2_score = self.XGBR_model.score(X, Y) # the score of the model is 0.99 which is almost perfect and same as "calorie_exercise_workout_model_analysis.ipynb"
        self.height = None
        self.age = None
        self.weight = None
        self.Gender = None
        self.Duration = None
        self.Heart_Rate = None
        self.Body_Temp = None        
        self.i = 1
        self.workout = [] # [[self.Gender, self.age, self.height, self.weight, self.Duration, self.Heart_Rate, self.Body_Temp, exe_name]] 2d array that looks like this 
        
        # -------------------------------------------------------------------------------------------------------
        # 3. runs the main_window function

        self.main_window()

# _________________________________________________________________________________________________________________________________________


# 2 this will greet the user and ask for their info


    def main_window(self):

        '''
            this is the function that:
            1. creates a window with 3 frames 
            2. greets the user and asks for Height, Weight, Age, Gender
            3. checks if the user has entered correct values. if invalid answers are entered shows error msg
            4. if values are correct it updates the object variables and calls the workout_entry() function
        '''

        # -------------------------------------------------------------------------------------------------------
        # 1. creates a window with 3 frames 

        main_window = Tk()
        main_window.geometry("1200x750")
        main_window.wm_iconbitmap(self.icon_path)
        main_window.title("Calorie_Tracker by Aryan Rathore")
        main_window.config(bg = "#121212")

        top_frame = Frame(main_window, bg="#121212")
        top_frame.pack(side=TOP,fill=BOTH)

        form_frame = Frame(main_window, bg="#121212")
        form_frame.pack(side=TOP,fill=BOTH)

        bottom_frame = Frame(main_window, bg="#121212")
        bottom_frame.pack(side=BOTTOM,fill=BOTH)


        # -------------------------------------------------------------------------------------------------------
        # 2. greets the user and asks for Height, Weight, Age, Gender

        calorie_image = Image.open(self.calorie_img_path).resize((200,200), Image.ANTIALIAS)
        calorie_image = ImageTk.PhotoImage(calorie_image)

        Label(top_frame, image=calorie_image,borderwidth=10,relief=RAISED,anchor=CENTER).pack(side=TOP,pady=(25,0))

        Label(top_frame, text="Welcome to python Calorie Tracker",font=("Cascadia Mono SemiBold", 20, "bold italic"),anchor=CENTER,bg='#404040',fg='white',borderwidth=2,relief=RIDGE).pack(side=TOP,pady=(25,10),fill=X)
        
        Label(top_frame, text="the r2 Score of the model is : {:0.4f}".format(self.XGBR_model_r2_score),font=("Cascadia Mono SemiBold", 15, "bold italic"),fg='white',bg="#404040",anchor=CENTER).pack(side=TOP,pady=(10,10),fill=X)

        Label(top_frame, text="Please Fill the form the below",font=("Cascadia Mono SemiBold", 15, "bold italic"),fg='white',bg="#404040",anchor=CENTER).pack(side=TOP,pady=(10,10),fill=X)

        height_var = IntVar()
        weight_var = IntVar()
        age_var = IntVar()
        gender_var = StringVar()

        Label(form_frame,text="Height in cm",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#121212").grid(row=0,column=0,padx=(325,5),pady=10,sticky=W)
        Entry(form_frame,textvariable=height_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=1,padx=(150,10),pady=10,sticky=W)

        Label(form_frame,text="weight in kg",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#121212").grid(row=1,column=0,padx=(325,5),pady=10,sticky=W)
        Entry(form_frame,textvariable=weight_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=1,column=1,padx=(150,10),pady=10,sticky=W)

        Label(form_frame,text="Age",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#121212").grid(row=2,column=0,padx=(325,5),pady=10,sticky=W)
        Entry(form_frame,textvariable=age_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=2,column=1,padx=(150,10),pady=10,sticky=W)

        Label(form_frame,text="Gender 'M' or 'F'",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#121212").grid(row=3,column=0,padx=(325,5),pady=10,sticky=W)
        Entry(form_frame,textvariable=gender_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=3,column=1,padx=(150,10),pady=10,sticky=W)

        # -------------------------------------------------------------------------------------------------------
        # 3. checks if the user has entered correct values. if invalid answers are entered shows error msg

        def check_values():
            try:

                if str(height_var.get()).isdigit() == False or str(weight_var.get()).isdigit() == False or str(age_var.get()).isdigit() == False:
                    tmsg.showerror("incorrect values", "height, weight, age should can only be integers and not empty")

                elif gender_var.get() not in ["M", "F"]:
                    tmsg.showerror("invalid value for Gender","Gender can only be 'M' for male and 'F' for female and not empty")
                else:
                    

                    # -------------------------------------------------------------------------------------------------------
                    # 4. if values are correct it updates the object variables and calls the workout_entry() function
     
                    self.height = height_var.get()
                    self.age = age_var.get()
                    self.weight = weight_var.get()
                    self.Gender = gender_var.get()
                    self.workout_entry(main_window)

            except TclError:
                tmsg.showerror("invalid value","Height, Weight and Age must be integers only and not empty. ")

        Button(text="SUBMIT",borderwidth=10,relief=RAISED,font=("",20,""),bg="#5CB8E4",command=check_values).pack(anchor=S,pady=15)
        
        main_window.mainloop()

# _________________________________________________________________________________________________________________________________________


# 3 then this will run and save the workout and predicted calories


    def workout_entry(self, main_window):
        '''
            this function creates a window that asks the user for info on their workout like Duration, Avg heart Rate, Body_Temp
            
            0. destroys the main window
            1. calculates the BMR of the person
            2. creates a window with 3 frames 
            3. greets the user and asks for Duration, Avg heart Rate, Body_Temp
            4. checks if the user has entered correct values (Submit exercise button). if invalid answers are entered shows error msg
            5. if values are correct, it predicts how many calories the user has burned and saves the information in the self.workout list 
            6. if the (finish workout button) is pressed it calls the finish_workout()

        '''

        # -------------------------------------------------------------------------------------------------------
        # 0. destroys the main window

        main_window.destroy()

        # -------------------------------------------------------------------------------------------------------
        # 1. calculates the BMR of the person

        if self.Gender == "F":

            self.BMR = ( 9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age) + 447.593
        elif self.Gender == "M":
            self.BMR = (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age) + 88.362
        else:
            tmsg.showerror("BMR error", "Could'nt calculate BMR")

        # -------------------------------------------------------------------------------------------------------
        # 2. creates a window with 3 frames 

        exercise_window = Tk()
        exercise_window.geometry("1200x750")
        exercise_window.wm_iconbitmap(self.icon_path)
        exercise_window.title("Calorie_Tracker by Aryan Rathore")
        exercise_window.config(bg = "#121212")

        top_frame = Frame(exercise_window, bg="#121212")
        top_frame.pack(side=TOP,fill=BOTH)

        form_frame = Frame(exercise_window, bg="#121212")
        form_frame.pack(side=TOP,fill=BOTH)

        bottom_frame = Frame(exercise_window, bg="#121212")
        bottom_frame.pack(side=BOTTOM,fill=BOTH)


        # -------------------------------------------------------------------------------------------------------
        # 3. greets the user and asks for Duration, Avg heart Rate, Body_Temp

        calorie_image = Image.open(self.calorie_img_path).resize((150,150), Image.ANTIALIAS)
        calorie_image = ImageTk.PhotoImage(calorie_image)

        Label(top_frame, image=calorie_image,borderwidth=10,relief=RAISED,anchor=CENTER).pack(side=TOP,pady=(25,0))

        Label(top_frame, text=f"click the submit exercise button to submit info of one exercise. \nclick the finish workout button when all exercises are done\n\nNumber of calories you need to eat in a day {int(self.BMR)}. ",font=("Cascadia Mono SemiBold", 15, "bold italic"),fg='white',bg="#404040",anchor=CENTER).pack(side=TOP,pady=(10,10),fill=X)

        statusvar = StringVar()
        statusvar.set(f"enter the info of exercise {self.i}")

        status_Label = Label(top_frame, textvariable=statusvar,font=("Cascadia Mono SemiBold", 20, "bold italic"),anchor=CENTER,bg='#404040',fg='white',borderwidth=2,relief=RIDGE)
        status_Label.pack(side=TOP,pady=(25,10),fill=X)

        Duration_var = IntVar()
        Heart_Rate_var = IntVar()
        Body_Temp_var = IntVar()
        name_var = StringVar()


        Label(form_frame,text="Name of exercise",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#121212").grid(row=0,column=0,padx=(150,5),pady=10,sticky=W)
        Entry(form_frame,textvariable=name_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=1,padx=(150,10),pady=10,sticky=W)

        Label(form_frame,text="Duration in minute",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#121212").grid(row=1,column=0,padx=(150,5),pady=10,sticky=W)
        Entry(form_frame,textvariable=Duration_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=1,column=1,padx=(150,10),pady=10,sticky=W)

        Label(form_frame,text="Heart_Rate (Avarage)",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#121212").grid(row=2,column=0,padx=(150,5),pady=10,sticky=W)
        Entry(form_frame,textvariable=Heart_Rate_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=2,column=1,padx=(150,10),pady=10,sticky=W)

        Label(form_frame,text="Body Temprature in celcius",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#121212").grid(row=3,column=0,padx=(150,5),pady=10,sticky=W)
        Entry(form_frame,textvariable=Body_Temp_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=3,column=1,padx=(150,10),pady=10,sticky=W)

        # -------------------------------------------------------------------------------------------------------
        # 4. checks if the user has entered correct values (Submit exercise button). if invalid answers are entered shows error msg

        
        def Submit_exercise(statusvar, status_label):
            try:

                if str(Duration_var.get()).isdigit() == False or str(Heart_Rate_var.get()).isdigit() == False or str(Body_Temp_var.get()).isdigit() == False or name_var.get() == "":
                    tmsg.showerror("incorrect values for exercise", "all entries must not be empty and should be integers")

                else:

                    # ------------------------------------------------------------------------------------------------------------------------------
                    # 5. if values are correct, it predicts how many calories the user has burned and saves the information in the self.workout list

                    if self.Gender == "M":
                        self.Gender = 0
                    elif self.Gender == "F":
                        self.Gender = 1

                    self.Duration = Duration_var.get()
                    self.Heart_Rate = Heart_Rate_var.get()
                    self.Body_Temp = Body_Temp_var.get() 

                    
                    prediction = self.XGBR_model.predict(np.asarray([[self.Gender, self.age, self.height, self.weight, self.Duration, self.Heart_Rate, self.Body_Temp]]))
                    
                    self.workout.append([dt.date.today(), self.age, self.height, self.weight, name_var.get(), self.Duration, self.Heart_Rate, self.Body_Temp, int(prediction[0])])

                    # showing the measage to user
                    tmsg.showinfo("calories predicted", f"The amount of calories burned during {name_var.get()} are : {prediction}\n-----------------------------------------------\nsubmit another exercise using submit exercise\n------------------------------------------\nor get workout insights from finish workout")
                    
                    self.i += 1
                    statusvar.set(f"enter the info of exercise {self.i}")
                    status_label.update() 
                    
            except TclError:
                tmsg.showerror("invalid value","Height, Weight and Age must be integers only and not empty. ")

        Button(form_frame, text="Submit\nexercise",borderwidth=10,relief=RAISED,font=("",20,""),bg="#5CB8E4",command=lambda: Submit_exercise(statusvar, status_Label)).grid(row=4,column=0,padx=(150, 0),pady=10,sticky=W)
        
        # 6. if the (finish workout button) is pressed it calls the finish_workout()
        Button(form_frame, text="Finish\nworkout",borderwidth=10,relief=RAISED,font=("",20,""),bg="#5CB8E4",command=lambda: self.finish_workout(self.workout,exercise_window)).grid(row=4,column=1,padx=(150, 0),pady=10,sticky=W)
        
        main_window.mainloop()

# _________________________________________________________________________________________________________________________________________


# 4 this will run last it will show the user the workout and save it in a csv


    def finish_workout(self, workout, exercise_window):

        '''
            after getting the workout info and predicting calories this function will show user the output in a tabular format and save it 
            in workout_logs.csv

            1. destroys the execise_window
            2. makes a output window with 2 frames which shows the user the workout in a tabular format
            3. save the workout in a csv and ends the program

        '''

        # -------------------------------------------------------------------------------------------------------
        # 1. destroys the execise_window

        exercise_window.destroy()

        # -------------------------------------------------------------------------------------------------------
        # 2. makes a output window with 2 frames which shows the user the workout in a tabular format

        output_window = Tk()
        output_window.geometry("1000x700")
        output_window.wm_iconbitmap(self.icon_path)
        output_window.title("Hotel_manager")
        output_window.config(bg = "#231A14")

        # frames

        top_frame = Frame(output_window, bg="#231A14")
        top_frame.pack(side=TOP,fill=BOTH)

        bottom_frame = Frame(output_window, bg="#231A14")
        bottom_frame.pack(side=TOP,fill=BOTH)

        calorie_image = Image.open(self.calorie_img_path).resize((150,150), Image.ANTIALIAS)
        calorie_image = ImageTk.PhotoImage(calorie_image)

        photo_label = Label(top_frame,image=calorie_image,borderwidth=10,relief=RAISED,anchor=CENTER)
        photo_label.image = calorie_image
        photo_label.pack(side=TOP,pady=(25,0))

        Label(top_frame,text=f"Your workout is as follows: ",font=("Cascadia Mono SemiBold", 15, "bold italic "),fg='white',bg="#121212",anchor=CENTER,borderwidth=5,relief=SOLID).pack(side=TOP,pady=(15,5),fill=X)
        

        total_calories = 0
        for exercise in workout:
            total_calories += exercise[-1]

        Label(top_frame,text=f"Total Calories Burned During The Workout: {total_calories}",font=("Cascadia Mono SemiBold", 15, "bold italic "),fg='white',bg="#121212",anchor=CENTER,borderwidth=5,relief=SOLID).pack(side=TOP,pady=(5,5),fill=X)

        # -------------------------------------------------------------------------------------------------------
        style=ttk.Style()
        style.configure("Treeview", rowheight=25)
        style.map("Treeview")

        # ([dt.date.today(), self.age, self.height, self.weight, name_var.get(), self.Duration, self.Heart_Rate, self.Body_Temp, int(prediction[0])]
        columns = ("Date", "Age", "Height", "Weight", "exercise", "Duration", "Heart_Rate", "Body_temp", "Calories")

        logins_table=ttk.Treeview(bottom_frame, height=12, columns=columns, show="headings")

        logins_table.column("Date", anchor=CENTER, width=80)
        logins_table.column("Age", anchor=CENTER, width=70)
        logins_table.column("Height", anchor=CENTER, width=70)
        logins_table.column("Weight", anchor=CENTER, width=70)
        logins_table.column("exercise", anchor=CENTER, width=120)
        logins_table.column("Duration", anchor=CENTER, width=100)
        logins_table.column("Heart_Rate", anchor=CENTER, width=90)
        logins_table.column("Body_temp", anchor=CENTER, width=100)
        logins_table.column("Calories", anchor=CENTER, width=110)

        logins_table.heading("Date", text="Date", anchor=CENTER)
        logins_table.heading("Age", text="Age", anchor=CENTER)
        logins_table.heading("Height", text="Height", anchor=CENTER)
        logins_table.heading("Weight", text="Weight", anchor=CENTER)
        logins_table.heading("exercise", text="exercise", anchor=CENTER)
        logins_table.heading("Duration", text="Duration", anchor=CENTER)
        logins_table.heading("Heart_Rate", text="Heart_Rate", anchor=CENTER)
        logins_table.heading("Body_temp", text="Body_temp", anchor=CENTER)
        logins_table.heading("Calories", text="Calories", anchor=CENTER)

        for index in range(0, len(workout)):
            logins_table.insert('', index="end", values=workout[index])

        scrollbary = ttk.Scrollbar(bottom_frame, orient=VERTICAL, command=logins_table.yview)
        logins_table.configure(yscroll=scrollbary.set)

        logins_table.grid(row=0,column=0,padx=(100,0),pady=(25,0))
        scrollbary.grid(row=0,column=1,sticky=NS,pady=(25,0))


        # -------------------------------------------------------------------------------------------------------
        # 3. save the workout in a csv and ends the program
        
        # this button ends the program
        def finish_window():

            tmsg.showinfo("Workout saved", "Workout has been saved in the workout_logs.csv")
            output_window.destroy()
            quit()
        Button(bottom_frame,text="quit",relief=RAISED,bg="#90EE90",fg='black',borderwidth=10,font=("Helvetica",10,"bold italic"),command=finish_window).grid(row=2,column=0)

        # saving the workout

        # this saves the workout in the workout_logs csv and shows msg
        try:        
            with open(self.workout_logs_csv_path, 'a') as f_object:
                dictwriter_object = DictWriter(f_object, fieldnames=columns)
                for exercise in workout:
                    ex_dict = {"Date":exercise[0], "Age":exercise[1], "Height":exercise[2], "Weight":exercise[3], "exercise":exercise[4], "Duration":exercise[5], "Heart_Rate":exercise[6], "Body_temp":exercise[7], "Calories":exercise[8]}
                    dictwriter_object.writerow(ex_dict)

        except:
            tmsg.showerror("workot_logs_error","could'nt save workout info to workout_logs.csv")
            quit()
        
        tmsg.showinfo("Success", "workout has been saved to the workout_logs.txt successfully. ")
        f_object.close()
        output_window.mainloop()


# _________________________________________________________________________________________________________________________________________

s1 = calorie_predictor()

########################################################### CREDITS ##############################################################################################

'''
                                                  WELCOME TO THE calorie_tracker

         THIS PROGRAM CALCULATES THE NUMBER OF CALORIES A USER HAS BURNED DURING A WORKOUT, SHOWS THEM AND STORES THEM IN A CSV

                                                    MADE BY : ARYAN RATHORE 
                                            COMPUTER SCIENCE ENGINEER AT VIT BHOPAL

                                                        CONTACT INFO
                                                aryanrathore13572002@gmail.com
                                               aryan.rathore2021@vitbhopal.ac.in
                                          github :- https://github.com/aryanrathore1012
                                    LINKEDIN - https://www.linkedin.com/in/aryan-rathore-b15459215/
'''