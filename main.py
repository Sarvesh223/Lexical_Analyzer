import re
#now we are assigning taking all 32 keywords in the form of list
keywrds = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
           'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
           'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
           'try', 'while', 'with', 'yield']
built_infunction = ['printf(','scanf(','main()','getch(','clrsrc(']
operators = ['+','-','=','*','/','%','==','!=','>','<','>=','<=','&&','||','!','&','|','^','~','>>','<<','=','+=','-=','*=','**']
sp_symbols=['@','#','$','_','!']
seprate = [',',':',';','\n','\t','{','}','(',')','[',']']
# now we are using the concept of file handling
# we are taking a file from the path and giving command to read the file
file = open('lexicalanal.txt','r+')
content = file.read()
#now we are spilliting code
splitcode = content.split()                                                                               #it works with space correctly
#this will spilt the source code w.r.t spaces
length = len(splitcode)
# now we are starting for loop
for i in range(0,length):
    if splitcode[i] in keywrds:
        print("Keywords : ",splitcode[i])
    if splitcode[i] in built_infunction:
        print("Built in Functions : ",splitcode[i])
    if splitcode[i] in operators:
        print("Operators : ",splitcode[i])
    if splitcode[i] in sp_symbols:
        print("Special Symbols : ",splitcode[i])
    if splitcode[i] in seprate:
        print("Seprators : ",splitcode[i])
    if re.match(r'(#include*)', splitcode[i]):
        print("Header File : ", splitcode[i])
    if re.match(r'^[-+]?[0-9]+$',splitcode[i]):
        print("Numbers: ",splitcode[i])
        continue
    if re.match(r'^[^\d\W]\w*\Z', splitcode[i]):
        print("Identifier : ",splitcode[i])
                
           
