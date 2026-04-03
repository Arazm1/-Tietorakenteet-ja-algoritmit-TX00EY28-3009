def custom_encoder(text):

    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    positions = []

    for char in text:
        char_lowercased = char.lower()
        if char_lowercased in reference_string:
            positions.append(reference_string.index(char_lowercased))
        
        else:
            positions.append(-1)

    return positions
