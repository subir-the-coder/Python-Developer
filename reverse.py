class ReverseProcessor:
    def __init__(self,text):
        self.text = text

    def rev(self):
        print("String to reverse is: ", self.text)
        reversed_text = ""
        for i in self.text:
            reversed_text = i + reversed_text
        return reversed_text


if __name__ == "__main__":
    user_input = input("# Enter the string to reverse: ").strip()
    rp = ReverseProcessor(user_input)
    print("# Reversed text is: ", rp.rev())