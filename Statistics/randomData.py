import random
import pprint



def random_code():
    random.seed(6)
    randomData1 = []
    randomData2 = []
    i = 0
    while i < 6:
        rand_value = random.randint(1,50)
        randomData1.append(rand_value)
        value = random.random()
        rand_value_decimal =round (value, 2)
        randomData2.append(rand_value_decimal)
        i += 1
        num_list = randomData1 + randomData2


    rand_one = random.randint(1,50)
    rand_two = round(value,2)

    pprint.pprint(rand_one)
    pprint.pprint(rand_two)
    pprint.pprint(num_list)

def random_code_no_seed():
    random.seed()
    randomData1 = []
    randomData2 = []
    i = 0
    while i < 6:
        rand_value = random.randint(1,50)
        randomData1.append(rand_value)
        value = random.random()
        rand_value_decimal =round (value, 2)
        randomData2.append(rand_value_decimal)
        i += 1
        num_list = randomData1 + randomData2


    rand_one = random.randint(1,50)
    rand_two = round(value,2)

    pprint.pprint(rand_one)
    pprint.pprint(rand_two)
    pprint.pprint(num_list)

def random_select():
    random.seed(6)
    randomData1 = []
    randomData2 = []

    i = 0
    rand_list = [10,20,30,40,50,60]
    rand_valueList = random.choices(rand_list,k=4)
    randomData1.append(rand_valueList)
    i+=1

    rand_value = random.choice(rand_list)
    randomData2.append(rand_value)

    pprint.pprint(randomData1)
    pprint.pprint(randomData2)

def random_select_no_seed():
    random.seed()
    randomData1 = []
    randomData2 = []

    i = 0
    rand_list = [10, 20, 30, 40, 50, 60]
    rand_valueList = random.choices(rand_list, k=4)
    randomData1.append(rand_valueList)
    i += 1

    rand_value = random.choice(rand_list)
    randomData2.append(rand_value)

    pprint.pprint(randomData1)
    pprint.pprint(randomData2)
