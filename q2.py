inc = int(input("Enter income:"))
num_of_dep = int(input("Enter the number of dependants:"))
taxinc = (inc - 10000) - (num_of_dep*3000)
print("Tax to be paid is ",taxinc/5)
