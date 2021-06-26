'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-25
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-25
@Title : To find harmonic series
/**********************************************************************************
'''
def harmonic_series():
    end_value_of_harmonic_series_n = int(input("Enter value of N - "))
    series_string = ""
    addition_of_series = 0
    if end_value_of_harmonic_series_n > 0:
        for value in range(1,end_value_of_harmonic_series_n+1):
            generate_value = 1/value
            addition_of_series = addition_of_series + generate_value
            if value == end_value_of_harmonic_series_n:
                series_string += f"1/{value} = "
            else:
                series_string += f"1/{value} + "
    else:
        print("value should not be 0 or less than 0")
    addition_of_series = round(addition_of_series,2)
    series_string += f"{addition_of_series}"
    print(series_string)

harmonic_series()