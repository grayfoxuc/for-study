name1 = input("Enter Name 1: ").lower().replace(" ", "")
name2 = input("Enter Name 2: ").lower().replace(" ", "")

x = 0
flames = ["Friends", "Lovers", "Admirers", "Marriage", "Enemies", "Secret Lovers"]

unique1 = "".join(set(name1))
unique2 = "".join(set(name2))

for letter in unique1:
    for letter2 in unique2:
        if letter == letter2:
            x = x + 1
numberToEvaluate = ((len(name1) - x) + (len(name2) - x)) % 6

print(flames[numberToEvaluate - 1])
