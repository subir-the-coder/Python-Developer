class FindingSecondLargest:
    def numArray(self, a):
        largest = float('-inf') # assuming the smallest possible value as largest
        second = float('-inf') # taking it for comparing

        for num in a:
            if num > largest:
                second = largest
                largest = num
            elif num > second and num != largest:
                second = num

        print("Second largest number is:", second)


if __name__ == "__main__":
    counter = 1
    numberArray = []

    while True:
        user_input = input(f"# Enter the {counter} number: (Press Q if done): ")

        if user_input.lower() == 'q':
            break
        else:
            numberArray.append(int(user_input))
            counter += 1

    fsl = FindingSecondLargest()
    fsl.numArray(numberArray)