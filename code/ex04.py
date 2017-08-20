cars = 100 # car的数量
space_in_a_car = 4.0 # car的容量
drivers = 30 # driver的数量
passengers = 90 # 乘客数量
cars_not_driven = cars - drivers # 没有司机的车的数量
cars_driven = drivers # 有司机的车的数量
carpool_capacity = cars_driven * space_in_a_car # 载人数量
average_passengers_per_car = passengers / cars_driven # 每车平均载人量


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers are available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
