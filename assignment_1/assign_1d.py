# Splits sentence using a seperator ' '
def my_split(sentence, separator=' '):
    result = []
    current_word = ''

    for character in sentence:
        if character == separator:
            result.append(current_word)
            current_word = ''
        else:
            current_word += character

    # add the last word if it exists
    if current_word:
        result.append(current_word)

    return result


def my_join(items, separator=','):

    result = ''
    for i, item in enumerate(items):
        result += str(item)
        if i < len(items) - 1:
            result += separator

    return result


# Main program
def main():
    sentence = input("Please enter sentence:")

    # Splits into words
    words = my_split(sentence)

    print(my_join(words, ','))

    for word in words:
        print(word)


main()
