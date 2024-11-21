print("================Body Mass Index Calculator===================")

print("------You are about to start you weight measurement----------")
# Collecting the persons weight and Height
weight=float(input("Enter your Weight in Kilogram:  "))
height=float(input("Enter you height in meters:  "))

# setting the formular to calculate BMI

BMI=weight/(height*height)


if BMI<=18.5:
    print('your BMI is',BMI, "You are too light")
elif BMI<=24.9:
    print('your BMI is',BMI,"Your weight is normal")
elif BMI<=29.9:
    print('You are a bit heavy')
elif BMI>=30:
    print("YOu are obess",BMI)