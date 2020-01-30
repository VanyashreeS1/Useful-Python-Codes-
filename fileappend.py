import os

if os.path.exists("demofile3.txt"):
    os.remove("demofile2.txt")
    print("file removed")
else:
    print("file doesnot exists")