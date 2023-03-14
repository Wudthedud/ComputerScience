"""Movie Theatre Ticketing System - Version 4
Calculate Ticket Price
Create by Daniel Wu"""

# Component 3
def get_price(type_):
    prices = [["A", 12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price [0] == type_:
            return price[1]


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
        print(f"\nYou have ordered {num_tickets} {ticket_type}(s) at a cost of ${cost * num_tickets:.2f}!")
    ticket_wanted = input("Do you want to sell another ticket? (Y/N) \n").upper()



# Main Routine
sell_ticket()


