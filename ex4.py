cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be",cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
#附加题，Traceback ( most recent call last ):
#File "ex4.py" , line 8 , in <module>
#average_passengers_per_car = car_pool_capacity / passenger
#NameError : name ' car_pool_capacity ' is not defined
#错误之处：第八行car_pool_capacity未赋值
#更改后，carpool_capacity的运算结果将不再对应浮点数
