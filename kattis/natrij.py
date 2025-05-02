# Problem: Natrij
hour1,minute1,second1 = map(int, input().split(":"))
hour2,minute2,second2 = map(int, input().split(":"))

current_seconds = hour1 * 3600 + minute1 *60 + second1
explosion_seconds = hour2 * 3600 + minute2 * 60 + second2


if explosion_seconds > current_seconds:
    delta = explosion_seconds - current_seconds
else:
    delta =  (24*3600 - current_seconds) + explosion_seconds

# print(delta)

hours = delta // 3600
delta %=3600
minutes = delta //60
seconds = delta %60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")