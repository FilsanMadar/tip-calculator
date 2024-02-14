#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line

def tip_calculator():
    # inputs needed
    bill = float(input("Input your total bill: "))
    total_people = int(input("How many people will split the bill? "))
    chosen_tip = int(input("Would you like to tip 10%, 12%, or 15%? "))

    # change % to decimal
    tip = chosen_tip / 100

    # calculate the tip toward the bill
    total_tip_needed = bill * tip

    # add the tip to the bill
    total_bill = bill + total_tip_needed

    # divide between the number of people 
    print("Each person should pay $", (round(total_bill / total_people, 2)))

tip_calculator()