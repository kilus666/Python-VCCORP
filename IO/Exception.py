# test
try:
    f= open('ancutkhong.txt')
    # if f.name== 'ancutkhong.txt':
    #     raise Exception

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Error vcl")
else:
    print(f.read())
    f.close()
finally:
    print("executing finally")


         