import math
pi = math.pi

def find_volume_sphere(radius):
    return((4/3) * pi * radius ** 3)
def find_volume_cube(side):
    return(side**3)

radius = input("Enter the gum ball radius (in.) => ")
radius = radius.strip()
print(radius)
radius = float(radius)

weekly_sales = input("Enter the weekly sales => ")
weekly_sales = weekly_sales.strip()
print(weekly_sales)
weekly_sales = float(weekly_sales)

total_gumballs = math.ceil(1.25 * weekly_sales)
gumballs_side = math.ceil(total_gumballs**(1/3))

diameter = radius * 2
length = gumballs_side * diameter

gumball_fit = math.ceil(gumballs_side ** 3)
gumball_extra = gumball_fit - total_gumballs

vol_gum = find_volume_sphere(radius)
vol_cube = find_volume_cube(length)

wasted = vol_cube - (vol_gum * total_gumballs)
wasted2 = vol_cube - (vol_gum * (gumballs_side**3))

print("\nThe machine needs to hold", gumballs_side, "gum balls along each edge.")
print("Total edge length is {:.2f}".format(length), "inches.")
print("Target sales were", str(total_gumballs) + ", but the machine will hold", gumball_extra, "extra gum balls.")
print("Wasted space is {:.2f}".format(wasted), "cubic inches with the target number of gum balls,")
print("or {:.2f}".format(wasted2), "cubic inches if you fill up the machine.")