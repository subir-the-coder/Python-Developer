#!usr/bin/python3

def check(num):
   significantStarts = False
   counter = 0
   for i in num:
       if i == ".":
           continue
       if i != "0":
           counter +=1
           significantStarts = True
       else:
           if significantStarts:
               counter+=1
   if "." not in num:
       for i in range(len(num)-1, -1, -1):
           if num[i] == "0":
               counter -=1
           else:
               break
   print("Significant digits found: "+str(counter))
if __name__ == "__main__":
    while True:
        num = input("[#] Enter a number: ")
        check(num)
