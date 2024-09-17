def task_1(): # Lists
    print("what your name: ")
    name = input()
    origional_list = ["Geoff", "Jeff", "Jeffrey"]
    origional_list.insert(0,name)
    origional_list.pop(2)
    new_list = origional_list.copy()

    return new_list


def task_2(): # Dictionaries

    keys = ("name", "age", "profession", "car")
    values = ("Geoff", 35, "technician", "car")
    geoff = dict(zip(keys, values))
    
    key = ("make", "model", "engine", "colour")
    val = ("ford", "focus", 1.6, "blue")
    car = dict(zip(key, val))
    
    person = {
        "geoff" : geoff,
        "car" : car,
    }

    return person


def task_3(): # Tuples
    print("what is your name: ")
    name = input()
    print("what is the subject you do: ")
    subject = input()
    print("What was your score: ")
    score = int(input())
    student_1 = ("Geoff", "Maths", 80)
    student_2 = (name, subject, score)
    students = student_1 + student_2

    return students


def task_4(): # Sets
    fruits_1 = {"apple", "banana", "cherry", "grape", "mango", "pineapple", "papaya","sprite", "orange", "lemon", "strawberry"}
    fruits_2 = {"raspberry", "banana", "cherry", "grape", "mango", "blueberry", "papaya", "melon", "lemon", "steak"}
    fruits_1.remove("sprite")
    fruits_2.remove("steak")
    symmetric_difference = fruits_1.symmetric_difference(fruits_2)
    intersection = fruits_1.intersection(fruits_2)

    duplicate_fruits = intersection # This should be a tuple containing all the fruits in both tuples
    individual_fruits = symmetric_difference # This should be a tuple containing only the individual fruits


    return [duplicate_fruits, individual_fruits] # Note - functions can only return one data item - so both tuples
                                                 # are contained inside a single list