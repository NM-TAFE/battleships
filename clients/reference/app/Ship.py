import Grid

pos = "H10"
type_of_ships = ["Patrol Boat", "Patrol Boat", "Destroyer", "Destroyer", "Cruiser", "Submarine", "Submarine",
                 "Submarine", "Battleship", "Aircraft Carrier"]


def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def placement_option():
    print(f"\n\nNumber of tiles for {type_of_ships[0]} : 1", end=" " * 5)
    print(f"Number of tiles for {type_of_ships[1]} : 2", end=" " * 5)
    print(f"Number of tiles for {type_of_ships[2]} : 3")
    print(f"Number of tiles for {type_of_ships[3]} : 4", end=" " * 5)
    print(f"Number of tiles for {type_of_ships[4]} : 5", end=" " * 5)
    print(f"Number of tiles for {type_of_ships[5]} : 6")
    print("Please Use Value between A-J and 1-10: Example Input: A2, J10, G5")


def placement(player1, player2):
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
                        count = 0
                        # working on detecting already placed ships
                        boat_type = ["PB", "PB", "D", "D", "C", "S", "S", "S", "B", "A"]
                        player1, place = place_ship1(player1, alp_value, num_value, direction, boat_type[boat_number])
                        if place:
                            boat_number += 1
                            if boat_number == max_ship:
                                placing_direction = False
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


def place_ship1(table, alp_value, num_value, direction, boat_type):
    count = 0
    position1 = "Not Empty"
    position2 = "Not Empty"
    position3 = "Not Empty"
    position4 = "Not Empty"
    position5 = "Not Empty"
    alp_location = ["S", "S", "S", "S"]
    location = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    # direction value 1.Left 2.Right 3.Top 4.Bottom
    if boat_type == "PB":
        for item in table[alp_value]:
            count += 1
            if count == num_value:
                if item == " ":
                    position1 = " "
                else:
                    print("There is not enough room to place ship at this location")
                    return table, False
            if position1 == " ":
                table[alp_value].pop(num_value - 1)
                table[alp_value].insert(num_value - 1, boat_type)

    elif boat_type == "D":
        if direction == 1:
            for item in table[alp_value]:
                count += 1
                if num_value - 1 < 1:
                    print("Ship cannot be place outside of grid")
                    return table, False

                if count == num_value - 1:
                    if item == " ":
                        position2 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if position1 == " " and position2 == " ":
                    table[alp_value].pop(num_value - 1)
                    table[alp_value].insert(num_value - 1, boat_type)
                    table[alp_value].pop(num_value - 2)
                    table[alp_value].insert(num_value - 2, boat_type)

        elif direction == 2:
            for item in table[alp_value]:
                count += 1
                if num_value + 1 > 10:
                    print("Ship cannot be place outside of grid")
                    return table, False
                if count == num_value + 1:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value:
                    if item == " ":
                        position2 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if position1 == " " and position2 == " ":
                    table[alp_value].pop(num_value - 1)
                    table[alp_value].insert(num_value - 1, boat_type)
                    table[alp_value].pop(num_value)
                    table[alp_value].insert(num_value, boat_type)

        elif direction == 3:
            for item in table[alp_value]:
                count += 1
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
            for i in range(len(location)):
                if alp_value == location[i]:
                    if i - 1 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position2 = " "
                                alp_location[0] = location[i - 1]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            if position1 == " " and position2 == " ":
                table[alp_value].pop(num_value - 1)
                table[alp_value].insert(num_value - 1, boat_type)
                table[alp_location[0]].pop(num_value - 1)
                table[alp_location[0]].insert(num_value - 1, boat_type)

        else:
            for item in table[alp_value]:
                count += 1
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
            for i in range(len(location)):
                if alp_value == location[i]:
                    if i + 1 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False

                    count = 0
                    for item in table[location[i + 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position2 = " "
                                alp_location[0] = location[i + 1]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            if position1 == " " and position2 == " ":
                table[alp_value].pop(num_value - 1)
                table[alp_value].insert(num_value - 1, boat_type)
                table[alp_location[0]].pop(num_value - 1)
                table[alp_location[0]].insert(num_value - 1, boat_type)

    elif boat_type == "C" or boat_type == "S":
        if direction == 1:
            for item in table[alp_value]:
                count += 1
                if num_value - 2 < 1:
                    print("Ship cannot be place outside of grid")
                    return table, False
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value - 1:
                    if item == " ":
                        position2 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value - 2:
                    if item == " ":
                        position3 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if position1 == " " and position2 == " " and position3 == " ":
                    table[alp_value].pop(num_value - 1)
                    table[alp_value].insert(num_value - 1, boat_type)
                    table[alp_value].pop(num_value - 2)
                    table[alp_value].insert(num_value - 2, boat_type)
                    table[alp_value].pop(num_value - 3)
                    table[alp_value].insert(num_value - 3, boat_type)

        elif direction == 2:
            for item in table[alp_value]:
                count += 1
                if num_value + 2 > 10:
                    print("Ship cannot be place outside of grid")
                    return table, False
                if count == num_value + 1:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value:
                    if item == " ":
                        position2 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value + 2:
                    if item == " ":
                        position3 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if position1 == " " and position2 == " " and position3 == " ":
                    table[alp_value].pop(num_value - 1)
                    table[alp_value].insert(num_value - 1, boat_type)
                    table[alp_value].pop(num_value)
                    table[alp_value].insert(num_value, boat_type)
                    table[alp_value].pop(num_value + 1)
                    table[alp_value].insert(num_value + 1, boat_type)

        elif direction == 3:

            for item in table[alp_value]:
                count += 1
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    if i - 2 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position2 = " "
                                alp_location[0] = location[i - 1]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position3 = " "
                                alp_location[1] = location[i - 2]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            if position1 == " " and position2 == " " and position3 == " ":
                table[alp_value].pop(num_value - 1)
                table[alp_value].insert(num_value - 1, boat_type)
                table[alp_location[0]].pop(num_value - 1)
                table[alp_location[0]].insert(num_value - 1, boat_type)
                table[alp_location[1]].pop(num_value - 1)
                table[alp_location[1]].insert(num_value - 1, boat_type)

        else:
            for item in table[alp_value]:
                count += 1
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
            for i in range(len(location)):
                if alp_value == location[i]:
                    if i + 2 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False

                    count = 0
                    for item in table[location[i + 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position2 = " "
                                alp_location[0] = location[i + 1]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i + 2]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position3 = " "
                                alp_location[1] = location[i + 2]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            if position1 == " " and position2 == " " and position3 == " ":
                table[alp_value].pop(num_value - 1)
                table[alp_value].insert(num_value - 1, boat_type)
                table[alp_location[0]].pop(num_value - 1)
                table[alp_location[0]].insert(num_value - 1, boat_type)
                table[alp_location[1]].pop(num_value - 1)
                table[alp_location[1]].insert(num_value - 1, boat_type)

    elif boat_type == "B":
        if direction == 1:
            for item in table[alp_value]:
                count += 1
                if num_value - 3 < 1:
                    print("Ship cannot be place outside of grid")
                    return table, False
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value - 1:
                    if item == " ":
                        position2 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value - 2:
                    if item == " ":
                        position3 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value - 3:
                    if item == " ":
                        position4 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if position1 == " " and position2 == " " and position3 == " " and position4 == " ":
                    table[alp_value].pop(num_value - 1)
                    table[alp_value].insert(num_value - 1, boat_type)
                    table[alp_value].pop(num_value - 2)
                    table[alp_value].insert(num_value - 2, boat_type)
                    table[alp_value].pop(num_value - 3)
                    table[alp_value].insert(num_value - 3, boat_type)
                    table[alp_value].pop(num_value - 4)
                    table[alp_value].insert(num_value - 4, boat_type)

        elif direction == 2:
            for item in table[alp_value]:
                count += 1
                if num_value + 3 > 10:
                    print("Ship cannot be place outside of grid")
                    return table, False
                if count == num_value + 1:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value:
                    if item == " ":
                        position2 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value + 2:
                    if item == " ":
                        position3 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

                if count == num_value + 3:
                    if item == " ":
                        position4 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

                if position1 == " " and position2 == " " and position3 == " " and position4 == " ":
                    table[alp_value].pop(num_value - 1)
                    table[alp_value].insert(num_value - 1, boat_type)
                    table[alp_value].pop(num_value)
                    table[alp_value].insert(num_value, boat_type)
                    table[alp_value].pop(num_value + 1)
                    table[alp_value].insert(num_value + 1, boat_type)
                    table[alp_value].pop(num_value + 2)
                    table[alp_value].insert(num_value + 2, boat_type)

        elif direction == 3:

            for item in table[alp_value]:
                count += 1
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    if i - 3 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position2 = " "
                                alp_location[0] = location[i - 1]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position3 = " "
                                alp_location[1] = location[i - 2]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position4 = " "
                                alp_location[2] = location[i - 3]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            if position1 == " " and position2 == " " and position3 == " " and position4 == " ":
                table[alp_value].pop(num_value - 1)
                table[alp_value].insert(num_value - 1, boat_type)
                table[alp_location[0]].pop(num_value - 1)
                table[alp_location[0]].insert(num_value - 1, boat_type)
                table[alp_location[1]].pop(num_value - 1)
                table[alp_location[1]].insert(num_value - 1, boat_type)
                table[alp_location[2]].pop(num_value - 1)
                table[alp_location[2]].insert(num_value - 1, boat_type)

        else:
            for item in table[alp_value]:
                count += 1
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
            for i in range(len(location)):
                if alp_value == location[i]:
                    if i + 2 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False

                    count = 0
                    for item in table[location[i + 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position2 = " "
                                alp_location[0] = location[i + 1]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i + 2]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position3 = " "
                                alp_location[1] = location[i + 2]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i + 3]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position4 = " "
                                alp_location[2] = location[i + 3]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            if position1 == " " and position2 == " " and position3 == " " and position4 == " ":
                table[alp_value].pop(num_value - 1)
                table[alp_value].insert(num_value - 1, boat_type)
                table[alp_location[0]].pop(num_value - 1)
                table[alp_location[0]].insert(num_value - 1, boat_type)
                table[alp_location[1]].pop(num_value - 1)
                table[alp_location[1]].insert(num_value - 1, boat_type)
                table[alp_location[2]].pop(num_value - 1)
                table[alp_location[2]].insert(num_value - 1, boat_type)

    elif boat_type == "A":
        if direction == 1:
            for item in table[alp_value]:
                count += 1
                if num_value - 3 < 1:
                    print("Ship cannot be place outside of grid")
                    return table, False
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value - 1:
                    if item == " ":
                        position2 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value - 2:
                    if item == " ":
                        position3 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value - 3:
                    if item == " ":
                        position4 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value - 4:
                    if item == " ":
                        position5 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

                if position1 == " " and position2 == " " and position3 == " " and position4 == " " and position5 == " ":
                    table[alp_value].pop(num_value - 1)
                    table[alp_value].insert(num_value - 1, boat_type)
                    table[alp_value].pop(num_value - 2)
                    table[alp_value].insert(num_value - 2, boat_type)
                    table[alp_value].pop(num_value - 3)
                    table[alp_value].insert(num_value - 3, boat_type)
                    table[alp_value].pop(num_value - 4)
                    table[alp_value].insert(num_value - 4, boat_type)
                    table[alp_value].pop(num_value - 5)
                    table[alp_value].insert(num_value - 5, boat_type)

        elif direction == 2:
            for item in table[alp_value]:
                count += 1
                if num_value + 3 > 10:
                    print("Ship cannot be place outside of grid")
                    return table, False
                if count == num_value + 1:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value:
                    if item == " ":
                        position2 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
                if count == num_value + 2:
                    if item == " ":
                        position3 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

                if count == num_value + 3:
                    if item == " ":
                        position4 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

                if count == num_value + 4:
                    if item == " ":
                        position5 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

                if position1 == " " and position2 == " " and position3 == " " and position4 == " " and position5 == " ":
                    table[alp_value].pop(num_value - 1)
                    table[alp_value].insert(num_value - 1, boat_type)
                    table[alp_value].pop(num_value)
                    table[alp_value].insert(num_value, boat_type)
                    table[alp_value].pop(num_value + 1)
                    table[alp_value].insert(num_value + 1, boat_type)
                    table[alp_value].pop(num_value + 2)
                    table[alp_value].insert(num_value + 2, boat_type)
                    table[alp_value].pop(num_value + 3)
                    table[alp_value].insert(num_value + 3, boat_type)

        elif direction == 3:

            for item in table[alp_value]:
                count += 1
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    if i - 3 < 1:
                        print("Ship cannot be place outside of grid")
                        return table, False

                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position2 = " "
                                alp_location[0] = location[i - 1]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position3 = " "
                                alp_location[1] = location[i - 2]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position4 = " "
                                alp_location[2] = location[i - 3]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i - 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position5 = " "
                                alp_location[3] = location[i - 4]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            if position1 == " " and position2 == " " and position3 == " " and position4 == " " and position5 == " ":
                table[alp_value].pop(num_value - 1)
                table[alp_value].insert(num_value - 1, boat_type)
                table[alp_location[0]].pop(num_value - 1)
                table[alp_location[0]].insert(num_value - 1, boat_type)
                table[alp_location[1]].pop(num_value - 1)
                table[alp_location[1]].insert(num_value - 1, boat_type)
                table[alp_location[2]].pop(num_value - 1)
                table[alp_location[2]].insert(num_value - 1, boat_type)
                table[alp_location[3]].pop(num_value - 1)
                table[alp_location[3]].insert(num_value - 1, boat_type)

        else:
            for item in table[alp_value]:
                count += 1
                if count == num_value:
                    if item == " ":
                        position1 = " "
                    else:
                        print("There is not enough room to place ship at this location")
                        return table, False
            for i in range(len(location)):
                if alp_value == location[i]:
                    if i + 2 > 10:
                        print("Ship cannot be place outside of grid")
                        return table, False

                    count = 0
                    for item in table[location[i + 1]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position2 = " "
                                alp_location[0] = location[i + 1]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i + 2]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position3 = " "
                                alp_location[1] = location[i + 2]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i + 3]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position3 = " "
                                alp_location[2] = location[i + 3]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False
            for i in range(len(location)):
                if alp_value == location[i]:
                    count = 0
                    for item in table[location[i + 4]]:
                        count += 1
                        if count == num_value:
                            if item == " ":
                                position4 = " "
                                alp_location[3] = location[i + 4]
                            else:
                                print("There is not enough room to place ship at this location")
                                return table, False

            if position1 == " " and position2 == " " and position3 == " " and position4 == " " and position4 == " ":
                table[alp_value].pop(num_value - 1)
                table[alp_value].insert(num_value - 1, boat_type)
                table[alp_location[0]].pop(num_value - 1)
                table[alp_location[0]].insert(num_value - 1, boat_type)
                table[alp_location[1]].pop(num_value - 1)
                table[alp_location[1]].insert(num_value - 1, boat_type)
                table[alp_location[2]].pop(num_value - 1)
                table[alp_location[2]].insert(num_value - 1, boat_type)
                table[alp_location[3]].pop(num_value - 1)
                table[alp_location[3]].insert(num_value - 1, boat_type)
    return table, True
    pass
