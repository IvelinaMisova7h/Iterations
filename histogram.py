numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(0, numbers):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number >= 200 and current_number < 400:
        p2 += 1
    elif current_number >= 400 and current_number < 600:
        p3 += 1
    elif current_number >= 400 and current_number < 600:
        p4 += 1
    else:
        p5 += 1

p1_percentage = p1 * 100 / numbers
p2_percentage = p2 * 100 / numbers
p3_percentage = p3 * 100 / numbers
p4_percentage = p4 * 100 / numbers
p5_percentage = p5 * 100 / numbers

print("%.2f" % p1_percentage + "%")
print("%.2f" % p2_percentage + "%")
print("%.2f" % p3_percentage + "%")
print("%.2f" % p4_percentage + "%")
print("%.2f" % p5_percentage + "%")
