print("Hello world")

my_name = "Reuven Rubi"
print(my_name)

age = 16

print(age)

is_male = True
print(is_male)

hobbies = ["Tennis", "Football"]

# tuple object
hobbies_tuple = ("Tennis", "Football")

print(hobbies)
hobbies[0] = "DevOps"
print(hobbies)

my_self = ["Reuven", "Rubi", "Cohen", 17]
my_self_dict = {
    "name": "Rubi",
    "last": "Cohen",
    "age": 18,
    "kids": ["David", "Moshe", "Yair"]
}

print(my_self_dict)

name = "Rubi"
last = "Cohen"
age = 16
print("My name is ", name, " my age ", age)
print("My name is " + name + " my age " + str(age))

#string interpalation
print(f"My name is {name} and my age is {age}")
#formatin
print("My name is %s and my age is %d" % (name, age))

