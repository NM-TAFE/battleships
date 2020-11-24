import Grid

pos = "H10"
type_of_ships = ["Patrol Boat", "Patrol Boat", "Destroyer", "Destroyer", "Cruiser", "Submarine", "Submarine",
                 "Submarine", "Battleship", "Aircraft Carrier"]


def intTryParse(value):
    """A function that check to see if the value can be convert to integer value or not"""
    try:
        return int(value), True
    except ValueError:
        return value, False


def placement_option():
    """Displaying Options for ship placement and tool tip"""

    print(f"\n\nNumber of tiles for {type_of_ships[0]} : 1", end=" " * 5)
    print(f"Number of tiles for {type_of_ships[1]} : 2", end=" " * 5)
    print(f"Number of tiles for {type_of_ships[2]} : 3")
    print(f"Number of tiles for {type_of_ships[3]} : 4", end=" " * 5)
    print(f"Number of tiles for {type_of_ships[4]} : 5", end=" " * 5)
    print(f"Number of tiles for {type_of_ships[5]} : 6")
    print("Please Use Value between A-J and 1-10: Example Input: A2, J10, G5")


def placement(player1, player2):
    """Determined player ship placement position"""
    player1 = player1
    player2 = player2
    placement_option()
    boat_number = 0
    max_ship = 10
    placing = True

    while placing:
        placing_direction = True
        ship_position = input(f"\nWhere would you like to place your {type_of_ships[boat_number]}: ")
        if ship_position == "":
            ship_position = "jj"
        alp_value = ship_position[0].upper()
        num_value, test = intTryParse(ship_position[1:])
        if test and (10 >= num_value > 0):
            if alp_value in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                while placing_direction:
                    print("\nShip Direction:")
                    print("1.Left  |  2.Right  |  3.Top  |  4.Bottom")
                    print("Choose ship direction, Input Example: 2")
                    ship_direction = input("Enter ship direction in Number Value: ")
                    direction, test = intTryParse(ship_direction)
                    if test and (4 >= direction > 0):
                        print("Good")
                        # working on detecting already placed ships
                        boat_type = ["PB", "PB", "D", "D", "C", "S", "S", "S", "B", "A"]
                        player1, place = place_ship(player1, alp_value, num_value, direction, boat_type[boat_number])
                        if place:
                            boat_number += 1
                            if boat_number == max_ship:
                                placing = False
                            Grid.display_grid(player1, player2)
                            break
                        else:
                            placing_direction = False

                    else:
                        print("Incorrect Input")

            else:
                print("Please Use Value between A-J and 1-10: Example Input: A2, J10, G5")
        else:
            print("Please Use Value between A-J and 1-10: Example Input: A2, J10, G5")
    return player1


def place_ship(table, alp_value, num_value, direction, boat_type):
    """Checks for ship placement overlaps and assign ships Tag to grid
        direction value 1.Left 2.Right 3.Top 4.Bottom
    """

    location = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    vector_alpha_location = 0
    for i in range(len(location)):
        if location[i] == alp_value:
            vector_alpha_location = i

    if boat_type == "PB":
        if table[alp_value][num_value - 1] == " ":
            table[alp_value][num_value - 1] = boat_type
        else:
            print("There is not enough room to place ship at this location")
            return table, False

    elif boat_type == "D":

        if direction == 1:
            if num_value - 1 < 1:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value - 2] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[alp_value][num_value - 2] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 2:
            if num_value + 1 > 10:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[alp_value][num_value] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 3:
            for up in range(len(location)):
                if alp_value == location[up]:
                    if up - 1 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

            if table[alp_value][num_value - 1] == " " and table[location[vector_alpha_location - 1]][
                    num_value - 1] == " ":
                table[alp_value][num_value - 1] = boat_type
                table[location[vector_alpha_location - 1]][num_value - 1] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        else:
            for down in range(len(location)):
                if alp_value == location[down]:
                    if down + 1 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False

            if table[alp_value][num_value - 1] == " " and table[location[vector_alpha_location + 1]][
                    num_value - 1] == " ":
                table[alp_value][num_value - 1] = boat_type
                table[location[vector_alpha_location + 1]][num_value - 1] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

    elif boat_type == "C" or boat_type == "S":
        if direction == 1:
            if num_value - 2 < 1:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value - 2] == " " and table[alp_value][
                    num_value - 3] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[alp_value][num_value - 2] = boat_type
                table[alp_value][num_value - 3] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 2:
            if num_value + 2 > 10:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value] == " " and table[alp_value][
                    num_value + 1] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[alp_value][num_value] = boat_type
                table[alp_value][num_value + 1] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 3:
            for up in range(len(location)):
                if alp_value == location[up]:
                    if up - 2 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

            if table[alp_value][num_value - 1] == " " and table[location[vector_alpha_location - 1]][
                    num_value - 1] == " " and table[location[vector_alpha_location - 2]][num_value - 1] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[location[vector_alpha_location - 1]][num_value - 1] = boat_type
                table[location[vector_alpha_location - 2]][num_value - 1] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        else:
            for down in range(len(location)):
                if alp_value == location[down]:
                    if down + 2 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False
            if table[alp_value][num_value - 1] == " " and table[location[vector_alpha_location + 1]][
                    num_value - 1] == " " and table[location[vector_alpha_location + 2]][num_value - 1] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[location[vector_alpha_location + 1]][num_value - 1] = boat_type
                table[location[vector_alpha_location + 2]][num_value - 1] = boat_type
            else:
                print("There is not enough room to place ship at this location")

    elif boat_type == "B":
        if direction == 1:
            if num_value - 3 < 1:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value - 2] == " " and table[alp_value][
                    num_value - 3] == " " and table[alp_value][num_value - 4] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[alp_value][num_value - 2] = boat_type
                table[alp_value][num_value - 3] = boat_type
                table[alp_value][num_value - 4] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 2:
            if num_value + 3 > 10:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value] == " " and table[alp_value][
                    num_value + 1] == " " and table[alp_value][num_value + 2] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[alp_value][num_value] = boat_type
                table[alp_value][num_value + 1] = boat_type
                table[alp_value][num_value + 2] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 3:
            for up in range(len(location)):
                if alp_value == location[up]:
                    if up - 3 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

            if table[alp_value][num_value - 1] == " " and table[location[vector_alpha_location - 1]][
                num_value - 1] == " " and table[location[vector_alpha_location - 2]][num_value - 1] == " " \
                    and table[location[vector_alpha_location - 3]][num_value - 1] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[location[vector_alpha_location - 1]][num_value - 1] = boat_type
                table[location[vector_alpha_location - 2]][num_value - 1] = boat_type
                table[location[vector_alpha_location - 3]][num_value - 1] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        else:
            for down in range(len(location)):
                if alp_value == location[down]:
                    if down + 3 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False
            if table[alp_value][num_value - 1] == " " and table[location[vector_alpha_location + 1]][
                num_value - 1] == " " and table[location[vector_alpha_location + 2]][num_value - 1] == " " \
                    and table[location[vector_alpha_location + 3]][num_value - 1] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[location[vector_alpha_location + 1]][num_value - 1] = boat_type
                table[location[vector_alpha_location + 2]][num_value - 1] = boat_type
                table[location[vector_alpha_location + 3]][num_value - 1] = boat_type
            else:
                print("There is not enough room to place ship at this location")

    elif boat_type == "A":
        if direction == 1:
            if num_value - 4 < 1:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value - 2] == " " and table[alp_value][
                num_value - 3] == " " and table[alp_value][num_value - 4] == " " \
                    and table[alp_value][num_value - 5] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[alp_value][num_value - 2] = boat_type
                table[alp_value][num_value - 3] = boat_type
                table[alp_value][num_value - 4] = boat_type
                table[alp_value][num_value - 5] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 2:
            if num_value + 4 > 10:
                print("Ship cannot be place outside of grid")
                return table, False

            if table[alp_value][num_value - 1] == " " and table[alp_value][num_value] == " " and table[alp_value][
                num_value + 1] == " " and table[alp_value][num_value + 2] == " " \
                    and table[alp_value][num_value + 3] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[alp_value][num_value] = boat_type
                table[alp_value][num_value + 1] = boat_type
                table[alp_value][num_value + 2] = boat_type
                table[alp_value][num_value + 3] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        elif direction == 3:
            for up in range(len(location)):
                if alp_value == location[up]:
                    if up - 4 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

            if table[alp_value][num_value - 1] == " " and table[location[vector_alpha_location - 1]][
                num_value - 1] == " " and table[location[vector_alpha_location - 2]][num_value - 1] == " " \
                    and table[location[vector_alpha_location - 3]][num_value - 1] == " " \
                    and table[location[vector_alpha_location - 4]][num_value - 1] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[location[vector_alpha_location - 1]][num_value - 1] = boat_type
                table[location[vector_alpha_location - 2]][num_value - 1] = boat_type
                table[location[vector_alpha_location - 3]][num_value - 1] = boat_type
                table[location[vector_alpha_location - 4]][num_value - 1] = boat_type
            else:
                print("There is not enough room to place ship at this location")
                return table, False

        else:
            for down in range(len(location)):
                if alp_value == location[down]:
                    if down + 4 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False
            if table[alp_value][num_value - 1] == " " and table[location[vector_alpha_location + 1]][
                num_value - 1] == " " and table[location[vector_alpha_location + 2]][num_value - 1] == " " \
                    and table[location[vector_alpha_location + 3]][num_value - 1] == " " \
                    and table[location[vector_alpha_location + 4]][num_value - 1] == " ":

                table[alp_value][num_value - 1] = boat_type
                table[location[vector_alpha_location + 1]][num_value - 1] = boat_type
                table[location[vector_alpha_location + 2]][num_value - 1] = boat_type
                table[location[vector_alpha_location + 3]][num_value - 1] = boat_type
                table[location[vector_alpha_location + 4]][num_value - 1] = boat_type
            else:
                print("There is not enough room to place ship at this location")
    return table, True
    pass
