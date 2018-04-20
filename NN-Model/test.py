import pandas as pd

while True:
    try:
        str = input("please input")
        arr = str.split("||||")
        print(str)
        print(arr)
        if len(arr) != 2:
            continue
        df = pd.DataFrame({"test_id":0,"question1":[arr[0]],"question2":[arr[1]]})
        print(df)
        print('$1.0')
    except Exception as e: 
    	print(e)