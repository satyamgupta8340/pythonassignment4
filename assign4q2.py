
# 2.Write a function to compute 8/0 and use try/except to catch the exceptions.

def cal():
    try:
        x=8/0
        print(x)
    except Exception as e:
         print(Exception)
         print('Exception is:',e)
    
    cal()