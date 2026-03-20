class Frequency:
    def __init__(self, sentence):
        self.sentence = sentence
        print("# Given sentence is: " + sentence)
        self.counter()

    def counter(self):
        freq = {}
        for char in self.sentence:
            freq[char] = freq.get(char, 0) + 1

        print("\n# Character Frequencies:")
        for char, count in sorted(freq.items()):
            print(f"  '{char}' : {count}")

if __name__ == "__main__":
    ip = input("# Enter the sentence: ")
    Frequency(ip)
