def compute_destiny(input_name1, input_name2):
    x = 0
    flames = ["Friends", "Lovers", "Admirers", "Marriage", "Enemies", "Secret Lovers"]
    name1 = input_name1.lower().replace(" ", "")
    name2 = input_name2.lower().replace(" ", "")

    unique1 = "".join(set(name1))
    unique2 = "".join(set(name2))

    for letter in unique1:
        for letter2 in unique2:
            if letter == letter2:
                x += 1

    numberToEvaluate = ((len(name1) - x) + (len(name2) - x)) % 6

    return flames[numberToEvaluate - 1]
