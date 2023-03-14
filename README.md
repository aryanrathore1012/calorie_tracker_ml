# calorie_tracker_ml

a python calorie tracker that uses machine learning models to predict the calories burned during a workout with dark theme UI
and saves the record in workout_logs csv

# need of the model:

there are many apps that track the amount of calories you eat but not many who calculate the amount of calories you burn during a workout this can be a standalone app that calculates the calories  burnt or this model can be implimented in other apps like healtifyme to show the calories eaten throughout the day aswell the calories burnt throughout the day. giving the user a complet insight on their diet

### about the dataset

the csv has 4 datasets exercise, calories, workout and workout_logs

### exercise dataset:-

this csv contains all the info on the person's workout (has our independet features)

| #   | Column     | Non-Null Count | Dtype   |
|:---: | :------: | :--------------: | :-----: |
| 0   | User_ID    | 15000 non-null | int64   |
| 1   | Gender     | 15000 non-null | object  |
| 2   | Age        | 15000 non-null | int64   |
| 3   | Height     | 15000 non-null | float64 |
| 4   | Weight     | 15000 non-null | float64 |
| 5   | Duration   | 15000 non-null | float64 |
| 6   | Heart_Rate | 15000 non-null | float64 |
| 7   | Body_Temp  | 15000 non-null | float64 |

the Column are self-Exploratory

### calories dataset:-

this csv contains calories burned by all workouts in exercise (has our target value / dependent feature "calories")

| #   | Column    | Non-Null Count  | Dtype    | 
| :---:  | :------: | :--------------: | :-----: | 
| 0   | User_ID   | 15000 non-null  | int64    |
| 1   | Calories  | 15000 non-null  | float64  |

1. User_ID: unique id for each person
2. Calories: the the total calories they burned during their workout

### workout:-

* this is our main csv, this is a combination of all Columns from
exercise (features) and calories burned in each workout (target)

* both calorie_exercise_workout_model_analysis.ipynb and main.pyw
use this csv for training their models


| #  |  Column     |  Non-Null Count | Dtype   |
|:---: |  :------: |  :--------------: | :-----: |
| 0  |  User_ID    |  15000 non-null | int64   |
| 1  |  Gender     |  15000 non-null | object  |
| 2  |  Age        |  15000 non-null | int64   |
| 3  |  Height     |  15000 non-null | float64 |
| 4  |  Weight     |  15000 non-null | float64 |
| 5  |  Duration   |  15000 non-null | float64 |
| 6  |  Heart_Rate |  15000 non-null | float64 |
| 7  |  Body_Temp  |  15000 non-null | float64 |
| 8  |  Calories   |  15000 non-null | float64 |

this is a combination of exercise and calories csv

### workout_logs:-

* this csv just saves the workout info with calories burnt for the purpose of keeping track and logging

# insights

### 1. ratio of male to female

![image](https://user-images.githubusercontent.com/91218998/223949818-621a734a-e112-4a9f-a7c3-5788eeee44c3.png)

the ratio of male to female is almost equal, but the number of females is a little bit more

### 2. Age range of people 

![image](https://user-images.githubusercontent.com/91218998/223950036-3b2dc960-7812-435b-8b1a-174aa2c8b4b9.png)


### there are many more insights i have grabbed from the dataset they are saved in the calorie_exercise_workout_model_analysis.ipynb

# Roadmap of the project:-

### the calorie_exercise_workout_model_analysis.ipynb :

the Preliminary data analysis, Exploratory data analysis, Data pre-processing, Model development & classifictaion have been done in this ipynb

### 1.Preliminary data analysis:
Edit the data to prepare it for further analysis, describe the key features of the data, and summarize the results.

* the program makes workout csv file by joining all columns from exercise csv with calories columns from calories csv file 

### 2.Exploratory data analysis:

Investigate data sets and summarize their main characteristics, often employing data visualization methods

* major Exploratory data analysis has been done of all columns some of the insights are shown above, many more insights have been visualized and stated in the calorie_exercise_workout_model_analysis.ipynb

### 3. Data pre-processing:

The dataset is preprocessed in order to check missing values, noisy data, and other inconsistencies before executing it to the algorithm.

* there were no missing values in the dataset and all columns were int64 or float64 

* the Gender was the only column with Categorical variables male and female which was transformed to 'male': 0 ,'female': 1  


### 4. Correlations of calories column with all the features:-

![image](https://user-images.githubusercontent.com/91218998/223950798-ba628823-087b-48a0-9b78-ae30b11eb719.png)

calories column is at the end and has a strong Correlation with Duration, Heart_Rate, Body_Temp and itself the regression plot graphs have been stated in the jupyter note book

### 5. Model development & comparison:

Model comparison involves comparing the performance of different models on a given task to identify which model is most effective.

* data is fitted into diffrent models and there respective testing r2 scores are as follows:-
 
![image](https://user-images.githubusercontent.com/91218998/223951370-074a0713-3d66-41b1-9585-cd0b32381439.png)

### the graph of r2 mea mse scores:-

![image](https://user-images.githubusercontent.com/91218998/225086896-e7b2049f-cf61-4e39-9fa9-40959ce6a1e1.png)

### now that we have chosen XGBRregressor as our model this program main.py:

1. initializes all the path, object variables and trains the XGBR_model using data read from workout csv

2. maakes a window that greets the user asking for their age, height, weight, gender

3. makes a window that asks for Duration, body_temp, name of the exercise and heart_rate and shows the user how many calories they predicted

4. when the finish workout and show user the table of the exercises they entered with predicted calories

5. saves the workout in the workout_logs csv

# ---------------------------------------

# inputs and outputs of main.py :-

### i would reccomond you watch the demo_video attached in the files as it would give you a clear image on what the project looks like but here are some Screenshots of the GUI

### 1.asking for height, weight, age, gender 

![image](https://user-images.githubusercontent.com/91218998/223958596-b8b3b652-b513-43e8-82fe-df7a2193d5c3.png)

### 2. asking for body temprature, duration of the exercise, avarage heart rate during the exercise 1

![image](https://user-images.githubusercontent.com/91218998/223958388-9ca811d5-483a-4174-a2a6-145f28387e36.png)

### 3. calories burnt in exercise 1 (output)

![image](https://user-images.githubusercontent.com/91218998/223958900-961b8b7d-7024-40a5-81fa-12e5800f248a.png)

### 4. asking for body temprature, duration of the exercise, avarage heart rate during the exercise 2

![image](https://user-images.githubusercontent.com/91218998/223959166-1a2f05e2-7a66-48f3-b361-5ec3f7afa285.png)

### 5. calories burnt in exercise 2

![image](https://user-images.githubusercontent.com/91218998/223959345-d013170a-ea3d-4c93-85eb-7033d07dd8c8.png)

### 6. final output

![image](https://user-images.githubusercontent.com/91218998/223959498-90ea2783-398b-45b7-822e-4b4cabb05e38.png)

# workout_logs csv after saving the workout

![image](https://user-images.githubusercontent.com/91218998/225088450-af63292d-6239-49d1-b504-615b435ee0eb.png)

# Limitations

* there are not that many Limitations as the program works well and predicts a correct amount of calories 

* the program does not have a proper website or app 

* the program asks body_temp, something users cant measure while working out so some other feature can be added

# future ugrades

* building a dedicated website or app so the program can be avaible
on both pc and mobile

* finding more features for calorie prediction

# credits and contact info:-

* made by Aryan Rathore
* LinkedIn : https://www.linkedin.com/in/aryan-rathore-b15459215/
* email: aryanrathore13572002@gmail.com, aryan.rathore2021@vitbhopal.ac.in


# ---------------------------------------


