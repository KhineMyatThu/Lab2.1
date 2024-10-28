def display_main_menu():
    print ("display_main_menu")
    print("Enter some numbers separated by comas(eg. 5,67,32)")
def get_user_input():
    print ("get_user_input")
    user_input=input()
    string_list=user_input.split(", ")
    float_list=[float(number) for number in string_list]
    return float_list
def calc_average(float_list):
    print("calc_average")
    total =sum(float_list)
    count=len(float_list)
    average=total/count
    return average
def find_min_max(float_list):
    print("find_min_max")
    min_value=min(float_list)
    max_value=max(float_list)
    return[min_value,max_value]
def sort_temperature(float_list):
    print("sort_temperature")
    return sorted(float_list)
def calc_median_temperature(float_list):
    print("calc_median_temperature")
    sorted_list=sorted(float_list)
    n=len(float_list)
    if n%2 !=0: median=sorted_list[n//2]
    else:
        m1=sorted_list[n // 2-1]
        m2=sorted_list[n//2]
        median=(m1+m2)/2
    return median
def main():
    print("ET0735(DevOps for AIoT)-Lab 2 -Introduction to Python")
    display_main_menu()
    float_list=get_user_input()
    print("Average="+str(calc_average(float_list)))
    print("Min and Max"+str(find_min_max(float_list)))
    print("Sorted Temperature="+str (sort_temperature(float_list)))
    print("Median="+str (calc_median_temperature(float_list)))

if __name__=="__main__":
    main()