#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from csv import writer
from csv import reader
import math


# # 1- SHOW ALL STUDENT DATA

# In[2]:


def show(filename):
    # initializing the titles and rows list
    fields = []
    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    #printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

    #  printing data with customized format 
    print('\n rows are:\n')
    for row in rows[:]:
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')


# # 2- SHOW COUNTS OF STUDENTS 

# In[3]:


def count ():
    filename = "data.csv"
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        line_count = 0
        for row in csvreader:
                line_count += 1
        return line_count-1


# ##  addtional function to add column to dataset 

# In[4]:


def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj,             open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


# #  3- SCORE CALCULATION

# In[5]:


def compute_score ():
    filename = "data.csv"

    rows = []
    scores= []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
                rows.append(row)
        for row in rows[1:]:
            total = int(row[2])+int(row[3])
            row.append(total)
        for row in rows[:]:
            for itr in row[4:]:
                i = itr 
                scores.append(i)
    return scores


# In[6]:


def append_score ():
    score = compute_score ()
    l=[]
    l.append("score")
    rows = count()
    for i in range(rows):
        val = score[i]
        l.append(val)
    add_column_in_csv('data.csv', 'data1.csv', lambda row, line_num: row.append(l[line_num - 1]))
    return
    


# In[7]:


def show_score ():
    append_score()
    filename = 'data1.csv'
    show(filename)


# #  4- GRADE CALCULATION

# In[8]:


def compute_grade():
    scores = compute_score ()
    a = range(90, 100)
    b = range(75, 90)
    c = range(60, 75)
    d = range(50, 60)
    f = range (0,50)
    grades = []

    for i in scores:
            if i in a :
                grade="A"
                grades.append(grade)
            if i in b :
                grade="B"
                grades.append(grade)
            if i in c :
                grade="C"
                grades.append(grade)
            if i in d :
                grade="D"
                grades.append(grade)
            if i in f :
                grade="F"
                grades.append(grade)
    return grades


# In[9]:


def append_grade ():
    append_score ()
    grade = compute_grade ()
    l=[]
    l.append("grades")
    rows = count()
    for i in range(rows):
        val = grade[i]
        l.append(val)
    add_column_in_csv('data1.csv', 'data2.csv', lambda row, line_num: row.append(l[line_num - 1]))
    return
    


# In[10]:


def show_grade ():
    append_grade()
    filename='data2.csv'
    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

            # extracting each data row one by one
        for row in csvreader:
                rows.append(row)

        #printing the field names
        print('Field names are:' + ', "student_id, name, grades"')

        #  printing data (student_id , student_name , grade )
        print('\n Student grades are:\n')
        for row in rows[1:]: 
            for col in row[:2] :
                print("%10s"%col,end=" "),
            for g in row[5:]:
                print("%10s"%g,end=" "),
            print('\n')


# ##  helper functions to calculate statistics 

# In[11]:


def average(data):
    avg = sum(data) / len(data)
    return avg


# In[12]:


def calculate_var(data):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n)


# In[13]:


def calculate_std(data):
    n = len(data)
    mean = sum(data) / n
    variance= sum((x - mean) ** 2 for x in data) / (n)
    return math.sqrt(variance)


# # 5- SHOW SCORE STATISTICS

# In[14]:


def calculate_stat (data):
    # -----------------------------------
    maxe = max(data)
    print (f"Maxium equals to {maxe}")
    # -----------------------------------
    mine = min(data)
    print (f"Minum equals to {mine}")
    # -----------------------------------
    avg = average(data)
    print (f"Average equals to {float(avg)}")
    # -----------------------------------
    var = calculate_var(data)
    print (f"Variance equals to {var}")
    # -----------------------------------
    std = calculate_std(data)
    print (f"Standered Diviation equals to {std}")
    # -----------------------------------
    return


# #  6- SHOW STUDENTS WITH GRADE "A"

# In[15]:


def show_A(filename):
    # initializing the titles and rows list
    fields = []
    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    #printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

    #  printing data
    print('\n Students has A grade are:\n')
    for row in rows[:]:
        for col in row[4:]:
                if col == "A":
                    print (row)


# # 7- SEARCH BY NAME OR PART OF NAME 

# In[16]:


def search(filename,key):
    # initializing the titles and rows list
    append_grade()
    fields = []
    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    #printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

    #  printing result if found
    print('\n Students are:\n')
    for row in rows[:]:
        for col in row[1:2]:
            if key in col :
                print (row)
            


# # 8- END PROGRAM

# In[17]:


def bye():
     print ("THANK YOU FOR USING THIS APPLICATION .. GOOD BYE")


# #  MENU 

# In[18]:


def show_menu():
    print('''
        HELLO..NICE TO MEET YOU , HOW CAN I HELP YOU ?
    
        1 ==> SHOW ALL STUDENTS 
        2 ==> SHOW COUNT OF ALL STUDENTS 
        3 ==> COMPUTE SCORES 
        4 ==> COMPUTE GRADES
        5 ==> SHOW SCORE STATISTICS
        6 ==> SHOW STUDENTS WITH GRADE "A" 
        7 ==> SEARCH BY NAME OR PART OF NAME
        8 ==> END 
        ''')


# # MAIN FUNCTION 

# In[19]:


def run_last():
    window = 0 
    filename = "data.csv"
    filename1 = "data2.csv"
    while window == 0 :
        show_menu()
        cursor = input(" ENTER THE NUMBER OF THE METHOOD YOU NEED ! ")
        if cursor == "1" :
            print("-----------------------------------------")
            show(filename)
            print("-----------------------------------------")
# -----------------------------------          
        if cursor == "2" :
            print("-----------------------------------------")
            line_count=count()
            print(f'Total Number of Student equals :  {line_count} .')
            print("-----------------------------------------")
# -----------------------------------
        if cursor == "3" :
            print("-----------------------------------------")
            score = compute_score ()
            show_score()
            print("-----------------------------------------")
# -----------------------------------
        if cursor == "4" :
            print("-----------------------------------------")
            grade = compute_grade ()
            show_grade()
            print("-----------------------------------------")
# -----------------------------------
        if cursor == "5" :
            print("-----------------------------------------")
            score = compute_score ()
            calculate_stat(score)
            print("-----------------------------------------")
# -----------------------------------
        if cursor == "6" :
            print("-----------------------------------------")
            show_A(filename1)
            print("-----------------------------------------")
# -----------------------------------
        if cursor == "7" :
            print("-----------------------------------------")
            keyword=input(" ENTER THE NAME OR PART OF NAME ")
            search(filename1,keyword)
            print("-----------------------------------------")
# -----------------------------------
        if cursor == "8" : 
            print("-----------------------------------------")
            bye()
            window = 1
            print("-----------------------------------------")
            


# In[20]:


run_last()


# In[ ]:




