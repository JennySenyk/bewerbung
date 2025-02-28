import time


weitermachen = 'y'
while weitermachen == 'y':       
    f_num = float(input("Input first number:"))
    oper = input("Select operation:")
    s_num = float(input("Input second number:"))
    if oper == '+':
        print("Loading...")
        time.sleep(3)
        print(f_num + s_num)
    elif oper == '-':
        print("Loading...")
        time.sleep(3)
        print(f_num - s_num)   
    elif oper == '*':
        print("Loading...")
        time.sleep(3)
        print(f_num * s_num) 
    elif oper == '/':
        print("Loading...")
        time.sleep(3)
        print(f_num / s_num)       
    else:
        print("Error")  
        
    weitermachen = input("Press 'y' to continue or any other button to end")     
