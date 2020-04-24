def CodeWord(sentens):
    result = []
    for letter in sentens:
        cod_letter = ord(letter)
        result.append(cod_letter)
    print(result)


def DecodeWord(arr_decode):
    result = ''
    for word in arr_decode:
        result += chr(word)
    print(result)

CodeWord('ping sese')

DecodeWord([112, 105, 110, 103, 32, 115, 101, 115, 101])