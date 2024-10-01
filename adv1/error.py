#Error Handling

while True: #until we get proper input
    try:
        age = int(input('age?'))
        print(10/age)
        #raise ValueError('hey cut it out') it stops from entering except
    except ValueError: #if error occurs in try block for value error
        print('pls enter a no')
    except ZeroDivisionError as err: #for zero division error case
        print(f'pls enter a no more than 0 {err}')
    #generally no need to to specify errors though recommended
    #u can also handle multiple errors in one except by zipping then into one tuple
    else: #if no error in try
        print('thankyou')
        break

    finally: #always gets executes
        print('ok i am done')

