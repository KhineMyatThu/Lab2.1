def calculate_bmi(height,weight):
    print ("Height="+str(height))
    print("Weight="+str(weight))
    bmi=(weight/height*height)
    print("bmi is "+str(bmi))
    if bmi<18.5:
        print("It is under weight")
        return -1
    elif 18.5<=bmi<=25.0:
        print("It is normal weight")
        return 0
    elif bmi>25.0:
        return 1
    