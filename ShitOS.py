import time
print("welcome to ArtyOS v1.0!")
print("loading...    ")
print("rom = 5mb")
print("ram = 90mb")
print("please wait...")
print("full memory= 95mb")
while True:
 command1 = input("print command: ")
 if command1 == "info" : 
  print(" ...........")
  print(" ArtyOS v.1.0")
  print("ShitRTX 4090ti")
  print("Shintel core i5-6500")
 if command1 == "data" : 
   print(" ...........")
   print("folder: system")
   print("folder: programs")
   print("folder: files")
   itm = input("select: ")
   if itm == "system" :
     print(" ...........")
     print("file: code")
     print("folder: nothing")
     sysdat = input("select: ")
     if sysdat == "code" :
      print("1488 by Artemhender!")
   if itm == "programs" :
    print(" ...........")
    print("pys: calculator")
    print("pys: word compilator")
    print("pys: time")
    promdat = input("select: ")
    if promdat == "calculator" :
     print(" ...........")
     a = float(input("one: "))
     b = float(input("two: "))
     c = a + b
     print(c)
    if promdat == "time" :
     print(" ...........")
     t = time.localtime(time.time())
     localtime = time.asctime(t)
     str = "Current Time:" + time.asctime(t)
 
     print(str);
    