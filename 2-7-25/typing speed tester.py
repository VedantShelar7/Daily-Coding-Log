import time

test_sentence = "Python is powerful and fun!"
print("Type the following:")
print(test_sentence)
input("Press Enter when ready...")

start = time.time()
typed = input("Start typing: ")
end = time.time()

elapsed = end - start
accuracy = sum(1 for a, b in zip(test_sentence, typed) if a == b) / len(test_sentence) * 100

print(f"\nTime taken: {elapsed:.2f} seconds")
print(f"Accuracy: {accuracy:.2f}%")

