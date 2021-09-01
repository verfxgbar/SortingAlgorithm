def bubble(numbers):
    final = [0] * len(numbers)
    count = 0
    while(count < len(numbers) - 1):
        if(int(numbers[count]) < int(numbers[count + 1])):
            stored = numbers[count]
            numbers[count] = numbers[count + 1]
            numbers[count + 1] = stored
        count += 1
    return numbers

def split(numbers):
    array = numbers.split(",")
    return array

input = input("Bitte schreibe die Nummern wiefolgt (1,2,3,4) \n")
splitted = split(input)
for i in splitted:
    sorted = bubble(splitted)
print("Sortierte Nummern >>", sorted)
print("Maxim >>", maximBubble(splitted))
