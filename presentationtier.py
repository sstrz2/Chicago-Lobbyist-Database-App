import sqlite3
import objecttier


def choice1(dbConn):
    name = input(
        "\nEnter lobbyist name (first or last, wildcards _ and % supported):\n"
    )
    lobbys = objecttier.get_lobbyists(dbConn, name)
    print("\nNumber of lobbyists found:", len(lobbys), "\n")
    if len(lobbys) <= 100:
        for person in lobbys:
            print(
                person.Lobbyist_ID,
                ":",
                person.First_Name,
                person.Last_Name,
                "Phone:",
                person.Phone,
            )
    else:
        print(
            "\nThere are too many lobbyists to display, please narrow your search and try again..."
        )


def choice2(dbConn):
    lobid = input("\nEnter Lobbyist ID: ")
    lobby = objecttier.get_lobbyist_details(dbConn, lobid)
    if lobby == None:
        print("\nNo lobbyist with that ID was found.")
    else:
        print("\n")
        print(lobby.Lobbyist_ID, ":")
        print(
            "  Full Name:",
            lobby.Salutation,
            lobby.First_Name,
            lobby.Middle_Initial,
            lobby.Last_Name,
            lobby.Suffix,
        )
        print(
            "  Address:",
            lobby.Address_1,
            lobby.Address_2,
            ",",
            lobby.City,
            ",",
            lobby.State_Initial,
            lobby.Zip_Code,
            lobby.Country,
        )
        print("  Email:", lobby.Email)
        print("  Phone:", lobby.Phone)
        print("  Fax:", lobby.Fax)
        print("  Years Registered: ", end="")
        for year in lobby.Years_Registered:
            print(year, ", ", sep="", end="")
        print("\n  Employers: ", end="")
        for employer in lobby.Employers:
            print(employer, ", ", sep="", end="")
        print("\n  Total Compensation: $", f"{lobby.Total_Compensation:,.2f}", sep="")


def choice3(dbConn):
    count = 1
    n = input("\nEnter the value of N: ")
    n = int(n)
    if n < 1:
        print("Please enter a positive value for N...")
    else:
        year = input("Enter the year: ")
        tops = objecttier.get_top_N_lobbyists(dbConn, n, year)
        for row in tops:
            print()
            print(count, ".", row.First_Name, row.Last_Name)
            count += 1
            print("  Phone:", row.Phone)
            print("  Total Compensation: $", f"{row.Total_Compensation:,.2f}", sep="")
            print("  Clients: ", end="")
            for person in row.Clients:
                print(person, ", ", sep="", end="")


def choice4(dbConn):
    year = input("\nEnter year: ")
    lobid = input("Enter the lobbyist ID: ")

    if objecttier.add_lobbyist_year(dbConn, lobid, year) == 1:
        print("\nLobbyist successfully registered.")
    else:
        print("\nNo lobbyist with that ID was found.")


def choice5(dbConn):
    lobid = input("\nEnter the lobbyist ID: ")
    sal = input("Enter the salutation: ")

    if objecttier.set_salutation(dbConn, lobid, sal) == 0:
        print("\nNo lobbyist with that ID was found.")
    else:
        print("\nSalutation successfully set.")


##################################################################
#
# main
#
dbConn = sqlite3.connect("Chicago_Lobbyists.db")
lobbys = objecttier.num_lobbyists(dbConn)
employers = objecttier.num_employers(dbConn)
clients = objecttier.num_clients(dbConn)
print("** Welcome to the Chicago Lobbyist Database Application **\n")
print("General Statistics:")
print("  Number of Lobbyists:", f"{lobbys:,}")
print("  Number of Employers:", f"{employers:,}")
print("  Number of Clients:", f"{clients:,}")


choice = input("\nPlease enter a command (1-5, x to exit): ")
while choice != "x":
    if choice == "1":
        choice1(dbConn)
    elif choice == "2":
        choice2(dbConn)
    elif choice == "3":
        choice3(dbConn)
    elif choice == "4":
        choice4(dbConn)
    elif choice == "5":
        choice5(dbConn)
    else:
        print("**Error, unknown command, try again...")

    choice = input("\nPlease enter a command (1-5, x to exit): ")


#
# done
#
