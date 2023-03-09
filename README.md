# calorie_tracker_ml
a python calorie tracker that uses machine learning models to predict the calories burned during a workout with dark theme UI.

#_____________________________________________________________________________________________________________________________________

made by Aryan rathore 
linkedin :- https://www.linkedin.com/in/aryan-rathore-b15459215/ 
email :- aryanrathore13572002@gmail.com, aryan.rathore2021@vitbhopal.ac.in

#_______________________________________________________________________________________________________________________________________

# Goal of the Project:-
to predict the amount of calories burned based on features like body temprature, duration of the exercise, avarage heart rate during the exercise etc.

# inputs and outputs of the main.py at the end (check demo video to see how to use the application)

#________________________________________________________________________________________________________________________________________

# how the projects work :- 

# The project has 2 parts 

### 1. the calorie_exercise_workout_model_analysis.ipynb :

the Preliminary data analysis, Exploratory data analysis, Data pre-processing, Model development & classifictaion have been done in this ipynb

1. it conduncts Preliminary data analysis and Data pre-processing on calories and exercise csv and in the proccess removes missing values and handles errors from them and then creates the workout csv. this is our main csv with the features variables and the target variable calories

2. then it explores the workout csv to see the distribution of data and what are the trends in the data for example:-

2 A. ratio of male to female

![image](https://user-images.githubusercontent.com/91218998/223949818-621a734a-e112-4a9f-a7c3-5788eeee44c3.png)

2 B. Age range of people 

![image](https://user-images.githubusercontent.com/91218998/223950036-3b2dc960-7812-435b-8b1a-174aa2c8b4b9.png)

and many more (check the ipynb for more insights on the data)

3. after the exploratory analysis of data of workout csv we check the correlation of all features with calories via a heatmap

![image](https://user-images.githubusercontent.com/91218998/223950798-ba628823-087b-48a0-9b78-ae30b11eb719.png)

calories is highly corelated with duration, heart_rate, body_temp, and ofc itself

4. then data is fitted into diffrent models and then scores them the model and there respective scores are as follows in descing order of r2 score:-

![image](https://user-images.githubusercontent.com/91218998/223951370-074a0713-3d66-41b1-9585-cd0b32381439.png)

5. the XGBRregressor is the best out the ones used has a r2 score of 0.99 and error of just 1.5 calories

#________________________________________________________________________________________________________________________________________

### 2. main.py :

now that we have chosen XGBRregressor as our model this program:

1. initializes all the path, object variables and trains the XGBR_model using data read from workout csv

2. maakes a window that greets the user asking for their age, height, weight, gender

3. makes a window that asks for Duration, body_temp, name of the exercise and heart_rate and shows the user how many calories they predicted

4. when the finish workout and show user the table of the exercises they entered with predicted calories

5. saves the workout in the workout_logs csv

#________________________________________________________________________________________________________________________________________

# inputs and outpus of main.py (refer to demo_video for a better input output):-

### asking for height, weight, age, gender 

![image](https://user-images.githubusercontent.com/91218998/223958596-b8b3b652-b513-43e8-82fe-df7a2193d5c3.png)

asking for body temprature, duration of the exercise, avarage heart rate during the exercise 1

![image](https://user-images.githubusercontent.com/91218998/223958388-9ca811d5-483a-4174-a2a6-145f28387e36.png)

### calories burnt in exercise 1 (output)

![image](https://user-images.githubusercontent.com/91218998/223958900-961b8b7d-7024-40a5-81fa-12e5800f248a.png)

### asking for body temprature, duration of the exercise, avarage heart rate during the exercise 2

![image](https://user-images.githubusercontent.com/91218998/223959166-1a2f05e2-7a66-48f3-b361-5ec3f7afa285.png)

### calories burnt in exercise 2

![image](https://user-images.githubusercontent.com/91218998/223959345-d013170a-ea3d-4c93-85eb-7033d07dd8c8.png)

### final output

![image](https://user-images.githubusercontent.com/91218998/223959498-90ea2783-398b-45b7-822e-4b4cabb05e38.png)

### workout_logs csv after saving the workout

![image](https://user-images.githubusercontent.com/91218998/223959640-edd0e76e-2886-47ee-a49a-643eef679f11.png)

#________________________________________________________________________________________________________________________________________

made by Aryan rathore 
linkedin :- https://www.linkedin.com/in/aryan-rathore-b15459215/ 
email :- aryanrathore13572002@gmail.com, aryan.rathore2021@vitbhopal.ac.in
