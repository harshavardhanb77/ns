l=['a',2,0]
for i in l:
    try:
        print("Reciprocal ",1/i)
    except ZeroDivisionError as e:
        print("Zero cannot be divided",e)
    except TypeError as e:
        print("only num")
    except Exception as e:
        print(e)
    finally:
        print("All done")