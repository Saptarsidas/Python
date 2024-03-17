s=lambda a,b,c:a if a>b and a>c else  b if  b>c and b>a else c 
# print("The Biggest of 10,20,30 is :",s(10,20,30))  
# print("The Biggest of 100,200,300 is:",s(100,200,300))   
a,b,c=int(input("Enter  three numbers") )
print("The Biggest of three",s(a,b,c))