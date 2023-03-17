"""Movie Theatre Ticketing System - Version 5
Update Totals
Created by Daniel Wu"""


adult_tickets = 0
child_tickets = 0
student_tickets = 0
gift_vouchers = 0
tickets_sold = 0
total_sales = 0


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
        confirm = input(
            f"\nYou have ordered {num_tickets} {ticket_type} ticket(s) at a cost of ${cost * num_tickets:.2f}!\n"
            f"Confirm? (Y/N) \n>>").upper()
        if confirm == "Y":
            return True
        elif confirm == "N":
            return False
        else:
            print("Please choose (Y/N)")


# Component 1 - Welcome screen and set up variables
def sell_ticket():
    print(f"********** Fanfare Movies - Ticketing System **********\n"
          f"\t Adult Tickets Sold: {adult_tickets}\n"
          f"\t Student Tickets Sold: {student_tickets}\n"
          f"\t Child Tickets Sold: {child_tickets}\n "
          f"\t Gift Vouchers Used: {gift_vouchers}\n"
          "******************\033[1m Totals \033[0m ******************\n"
          f"\t Total Tickets Sold: {tickets_sold}\n"
          f"\t Total Sales: {total_sales}\n")


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
            total_sales += cost
            tickets_sold += num_tickets
            if ticket_type == "A":
                adult_tickets += num_tickets
            elif ticket_type == "S":
                student_tickets += num_tickets
            elif ticket_type == "C":
                child_tickets += num_tickets
            elif ticket_type == "G":
                gift_vouchers += num_tickets
        else:
            print("Order Cancelled")

    ticket_wanted = input("Do you want to sell another ticket? (Y/N) \n").upper()

# Main Routine
sell_ticket()
