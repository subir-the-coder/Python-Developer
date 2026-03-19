# Count vowels in a String, and frequency of the vowels appeared vowels

class VowelCounter:
    def __init__(self, s):
        self.string = s
    def theCounter(self):
        print(f"# Given String is: {self.string}")
        vowels = ['a', 'e', 'i', 'o', 'u']
        counter = 0
        freq = {}
        for i in self.string:
            if i in vowels:
                counter +=1
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
        print(f"Number of vowels found is : {counter}")
        for k, v in freq.items():
            print(f"{k} appeared {v} times")
if __name__ == "__main__":
    user_input = input("# Enter a string : ").strip().lower()
    VowelCounter(user_input).theCounter()

