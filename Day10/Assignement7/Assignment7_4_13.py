#13> Write a program to convert temperature from Fahrenheit to Celsius.


b=float(input("Enter the temp in farhenheit: "))
c = lambda a:(5/9)*(a-32)
print("The tenp in celcius is: ",c(b))