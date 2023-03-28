data = [
    [
        {"seat_name": "a1", "isTaken": True},
        {"seat_name": "a2", "isTaken": False},
        {"seat_name": "a3", "isTaken": True},
        {"seat_name": "a4", "isTaken": True},
        {"seat_name": "a5", "isTaken": False},
    ],
    [
        {"seat_name": "b1", "isTaken": False},
        {"seat_name": "b2", "isTaken": False},
        {"seat_name": "b3", "isTaken": True},
        {"seat_name": "b4", "isTaken": False},
        {"seat_name": "b5", "isTaken": True},
    ],
    [
        {"seat_name": "c1", "isTaken": False},
        {"seat_name": "c2", "isTaken": True},
        {"seat_name": "c3", "isTaken": True},
        {"seat_name": "c4", "isTaken": True},
        {"seat_name": "c5", "isTaken": False},
    ],
]
vagon = int(input("ვაგონის ნომერი"))
seat = input("ადგილის ნომერი")
free_seats = []

for vagon_num in data:
    free_seats.append([])
    for inx, st in enumerate(vagon_num):
        if not st["isTaken"]:
            free_seats[-1].append(inx)

if len(data) >= vagon:
    for index, seat_num in enumerate(data[vagon]):
        if seat == seat_num["seat_name"] and not seat_num["isTaken"]:
            print(seat_num)
        elif seat == seat_num["seat_name"] and seat_num["isTaken"]:
            if free_seats:
                for id, free in enumerate(free_seats):
                    if free:
                        closest = min(free, key=lambda x: abs(x-index))
                        print(data[id][closest])
                        break
                    else:
                        continue
        else:
            print("ადგილის ნომერი არასწორია")
            break
else:
    print("ვაგონის ნომერი არასწორია")

