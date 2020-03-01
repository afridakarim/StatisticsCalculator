import random
import pprint
import decimal

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
