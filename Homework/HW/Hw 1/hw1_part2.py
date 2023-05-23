minute = int(input("Minutes ==> "))
print(minute)

second = input("Seconds ==> ")
print(second)
second = int(second)

mile = input("Miles ==> ")
print(mile)
mile = float(mile)

target = input("Target Miles ==> ")
print(target)
target = float(target)

totalMin = float((second/60) + minute)
paceMin = int(totalMin/mile)
paceSec = int(((totalMin/mile) - paceMin) * 60)

speed = (mile / (totalMin / 60))

targetMin = int((target/speed) * 60)
targetSec = int(((target/speed * 60) - targetMin) * 60)

print("\nPace is", paceMin, "minutes and", paceSec, "seconds per mile.")
print("Speed is {:.2f}".format(speed), "miles per hour.")
print("Time to run the target distance of {:.2f}".format(target), "miles is", targetMin, "minutes", "and", targetSec, "seconds.")