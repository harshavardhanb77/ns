import io
try:
    f=open("text.txt")
    f.writelines(input("Add line"))
except io.UnsupportedOperation as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("Done")