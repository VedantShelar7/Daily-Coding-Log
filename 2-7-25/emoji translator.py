def emoji_translator(sentence):
    words = sentence.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😞",
        "<3": "❤️",
        ":D": "😄"
    }
    translated = " ".join([emojis.get(word, word) for word in words])
    return translated

msg = input("Type a message: ")
print("Translated:", emoji_translator(msg))


