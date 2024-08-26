# Resolution selection algorithm
import random

first_names = ["Lebron", "Quan", "Sam", "Carl", "Scott", "Loretta", "Stone", "Matt", "Matthew", "Taylor", "Lucy"]
last_names = ["James", "Smith", "Brown", "Johnson", "Stevenson", "Hernandez", "Garcia", "Martin", "Jones", "Moore"]


def test_create_account_info():
    #  first_name, last_name, email,
    first_name = first_names[random.randint(0, len(first_names))]
    print(first_name)


def test_res():
    num = 10
    resolutions_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    results = []

    for i in range(num):
        random_resolution = resolutions_list[random.randint(0, len(resolutions_list)) - 1]
        results.append(random_resolution)

    print(results)


if __name__ == "__main__":
    test_create_account_info()