import time
print ('Hello and welcome to my BMI calculator')
time.sleep(2)
print ('BMI stands for Body Mass Index, it is a measure of body fat based on height and weight')
time.sleep(2)
weight = float(input('Please enter your weight in kilograms: '))
height = float(input('Please enter your height in centimeters: '))
height = height / 100  # Convert centimeters to meters
bmi = weight / (height ** 2)
print ('Your BMI is: {:.2f}'.format(bmi))
if bmi < 18.5:
    print ('You are underweight.')
elif 18.5 <= bmi < 24.9:
    print ('You have a normal weight.')
elif 25 <= bmi < 29.9:
    print ('You are overweight.')
else:
    print ('You are obese.')
time.sleep(2)
print ('Thank you for using my BMI calculator! Have a great day!')
time.sleep(0.50)
print ('P.S. Please remember to always consult with a healthcare professional for personalized advice regarding your health and BMI.')
time.sleep(2)
print ('Goodbye!')
print ('This program was created by Johnathan Samet and VS Code.')
print ('If you have any questions or feedback, please feel free to reach out to me at sametjohnathan@gmail.com')
time.sleep(2)
