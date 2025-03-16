import bisect

def find_dormitory_and_room(dorm_rooms, letters):
    prefix_sum = []
    suma = 0
    for room in dorm_rooms:
        suma+=room
        prefix_sum.append(suma)

    for letter in letters:
        dorm_index = bisect.bisect_left(prefix_sum, letter) + 1  
        previous_sum = prefix_sum[dorm_index - 2] if dorm_index > 1 else 0
        room_number = letter - previous_sum
        print(f"{dorm_index} {room_number}")
    


n, m = list(map(int, input().split()))

dorm_rooms = list(map(int, input().split()))
letters = list(map(int, input().split()))

find_dormitory_and_room(dorm_rooms, letters)
