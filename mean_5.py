#inputs 5 numbers from user and sums the numbers
#define a function
def sum_5():
#initialize the sum to 0
    sum_n = (0)
#loop over 5 times using for loop
    for i in range(5):
#prompt use to enter a number
        n = int(input("Enter a whole number: "))
#add the number to the sum each time you loop
        sum_n = sum_n + n
#calcualte average
        average = sum_n/5
#use the f string to print the sum and average
    print(f"The sum of numbers is {sum_n} and average is {average}")
#call the funtion
sum_5()
