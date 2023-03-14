"""Movie Theatre Ticketing System - Version 4
Calculate Ticket Price
Create by Daniel Wu"""


# Component 3
def get_price(type_):
    prices = [["A", 12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]


# Component 4
def confirm_order(ticket, number, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"\nYou have ordered {num_tickets} {ticket_type}(s) at a cost of ${cost * num_tickets:.2f}!\n"
                        f"Confirm? (Y/N) \n>>").upper()
        if confirm == "Y":
            return True
        elif confirm == "N":
            return False
        else:
            print("Please choose (Y/N)")




# Component 1 - Welcome screen and set up variables
def sell_ticket():
    print("********** Fanfare Movies - Ticketing System **********\n")
    adult_tickets = 0
    child_tickets = 0
    student_tickets = 0
    gift_vouchers = 0
    tickets_sold = 0
    total_sales = 0


# Component 2
ticket_wanted = "Y"
total = float(0)
while ticket_wanted == "Y":
    ticket_type = input("What kind of ticket do you want: \n"
                        "\t 'A' - Adult Ticket \n"
                        "\t 'S' - Student Ticket \n"
                        "\t 'C' - Child Ticket \n"
                        "\t 'G' - Gift Voucher \n"
                        ">> ").upper()
    if ticket_type not in ["A", "S", "C", "G"]:
        print("Invalid input. Please enter 'A', 'S', 'C', or 'G'.")

    else:
        num_tickets = int(input(f"How many {ticket_type} tickets do you want? \n "))
        cost = get_price(ticket_type)
        if confirm_order(ticket_type, num_tickets, cost):
            print("Order Confirmed")
        else:
            print("Order Cancelled")

        total = total + cost

    ticket_wanted = input("Do you want to sell another ticket? (Y/N) \n").upper()

# Main Routine
sell_ticket()
