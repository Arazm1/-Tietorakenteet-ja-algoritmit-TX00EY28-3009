# Greedy algorithms

#“What is the fewest number of coins I need to make a certain amount?”
def min_coins(face_values, amount):
    result = []
    for face_value in sorted(face_values, reverse=True):
        calculated = amount // face_value
        amount -= calculated * face_value
        result.append(calculated)

    return result