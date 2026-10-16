# import turtle
#
# # Create a screen object
# screen = turtle.Screen()
# timmy = turtle.Turtle()# from this we see how to create an object from blueprint
# timmy.shape("turtle")#from this we know how to call methods
# timmy.color("red")
# timmy.forward(200)
# print(screen.canvheight)#from this we see how to access attributes from objects
# screen.exitonclick()
#

from prettytable import PrettyTable
table=PrettyTable() #ceating table
print(table) # without data
table.add_column("pokemon name",["pikachu","squirtle","charmander"])
table.add_column("Type",["electric","water","fire"])
print(table)#with data inside by adding column
table.align="l"
print(table)

#coffe machine using oop


# TODO: 3. PROCESS COINS
# TODO: 4. CHEEK TRANSACTION SSUCCESSFUL
# TODO: 5. MAKE COFFE
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#TODO: 1. print report
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
is_on = True

# TODO: 2. CHEEK RESOURCE SUFFICENT?
while is_on:
    options=menu.get_items()
    choice=input(f"what would you like? {options}")
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
           if money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)

