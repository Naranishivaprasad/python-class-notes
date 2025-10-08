
# #first question 
# #snake_case
# user_name="shiva"
# college_name="vjit"
# course_name="python"
# batch_no="67"
# pass_out="2025"
# print("user_name:", user_name)
# print("college_name:", college_name)
# print("course_name:", course_name)
# print("batch_no:", batch_no)
# print("pass_out:", pass_out)
# print("\n")
# #camelCase
# userName="shiva"
# collegeName="vjit"
# courseName="python"
# batchNo="67"
# passOut="2025"
# print("userName:",userName)
# print("collegeName:",collegeName)
# print("courseName:",courseName)
# print("batchNo:",batchNo)
# print("passOut:",passOut)
# print("\n")
# #PascalCase
# UserName="shiva"
# CollegeName="vjit"
# CourseName="python"
# BatchNo="67"
# PassOut="2025"
# print("UserName:",UserName)
# print("CollegeName:",CollegeName)
# print("CourseName:",CourseName)
# print("BatchNo:",BatchNo)
# print("PassOut:",PassOut)


#second question 
#trying invalid variable name and observethe error 


# $name="shiva"


    # #thrid question 

    # my_int=67
    # percentage_float=7.5
    # name_str="shiva prasad"
    # feepaid_bool=True

    # print(type(my_int))
    # print(type(percentage_float))
    # print(type(name_str))
    # print(type(feepaid_bool))
    # print(id(my_int))
    # print(id(percentage_float))
    # print(id(name_str))
#     # print(id(feepaid_bool))

# # print("\n")

# # #intermediate task(manipulation and conversions)

# # #first  question

# players = ["Rohit", "Virat", "Gill", "Dhoni"]
# players[2]="surya"
# #Replace "Gill" with "Surya".
# players.append("jadeja")
# #Add "Jadeja" at the end.
# print(players)
# print(len(players))
# print(players[-2])


# print("\n")
# #secound question


laptop_info = ("HP", "16GB", "512GB SSD", 2024, True)
print(laptop_info[-2:]) 
print("\n")

    #third question 


# countries = {"India", "USA", "India", "Canada", "UK", "USA"}        
# countries.add("germany")
# countries.remove("UK")
# print(countries)


# #fourth questio


# frozen_marks = frozenset([90, 85, 75, 85])

# print(type(frozen_marks))

# print("\n")
# Advanced Tasks (Nesting & Real-time)

# first question'

# car_info = {
#  "brand": "Tesla",
#  "model": "Model S",
#  "price": "1.5Cr",
#  "features": ["Autopilot", "Electric", "Sunroof"]
# }

# car_info["color"]="white"

# car_info["price"]="1.7cr"
# car_info["insurance"]={
#     "provider": "HDFC", "valid_till": "2026"
# }
# print(car_info)

# print("\n")

# secound question
# books=[
# {"title": "Atomic Habits", "author": ["James Clear"]},
#  {"title": "Ikigai", "author": "Héctor García"},
#  {"title": "Zero to One", "author": "Peter Thiel"}
# ]

# new_books=[{"title":"deep wills",'author':'James clear'}]
# books=books+new_books

# books[1]["author"]="Francesc Miralles"
# print(books)
# print("\n")

# # third question



# laptop = {
#     "brand": "Apple",
#     "specs": {"ram": "16GB", "storage": "1TB SSD", "chip": "M2"},
#     "price": "2L"
# }
# print("chip:" ,laptop["specs"]["chip"])
# print(f"{laptop["brand"]} laptop comes with {laptop["specs"]["chip"]} chip and cost {laptop["price"]}")

# print("\n")

#chellenge tasks

# # first question 
# ott_data = [
#     {"platform": "Netflix", "shows": ["Stranger Things", "Wednesday"]},
#     {"platform": "Prime", "shows": ["Mirzapur", "Farzi"]},
#     {"platform": "Hotstar", "shows": ["Special Ops", "The Freelancer"]}
# ]

# # Add "Kingdom" to Prime's show list
# for item in ott_data:
#     if item["platform"] == "Prime":
#         item["shows"].append("Kingdom")

# print(ott_data)



# # secound question

a=10
b=10
print(id(a))
print(id(b))


print(5<<3)
print(bin(40));

print(5>>2);
print(bin(1));
print(5&3);


# functions

# def sample(eamcet,student_name):
#     if(eamcet>200):
#         print("You are eligible for engineering")
#     else:
#         print(" you are eligible for degree")
# sample(250,"shiva") 

# def even_or_odd(num):
#     if(num%2):
#         print("it is even number")
#     else:
#         print("the number is odd")
# even_or_odd(5)
    


# using bitwise operator

# def even_or_odd(num):
#     if (num & 1== 0) :
#         print(f"the {num} is even number")
#     else:
#         print(f"{num} is odd number")

# even_or_odd(5)


# num=1547890
# id=num%10
# if id in (0,2,4,6,8):
#     print("the num is even")
# else:
#     print("the number is odd")


# def eligibility(eamcet):
#     if(eamcet>200):
#         print(f"{eamcet} you are eligible for eamcet")
#     elif(eamcet>=150):
#         print(" you are eligible for degree")
#     else:
#         print("do a business or try again")
# eligibility(155)



# a=10
# b=5
# c=a+b;
# print(f"the addition  of {a} and {b} is {c}")


# s=5;
# s*=s
# print(s)


# l=20;
# b=10;
# print(l*b)


# amount=7652
# a=amount//1000
# b=amount-(a*1000)
# c=b//500
# d=b-(c*500)
# print(f"1000s:{a} 500s:{c} 100s:{d}")



# Calculate sum of 3 numbers without using functions
# Simple input and calculation

# Get input from user
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# # Calculate sum
# sum_result = a + b + c

# # Display result
# print(f"The sum of {a}, {b}, and {c} is: {sum_result}")


# a=input("enter the number")
# if  a%2==0 and a%3==0  and a%6==0 :
#     print("the number is satisfy"

# # terinary operator
# # it is also know asconditional operator 
# # it is used to write if else in shorthand form in single line 
# # with thise can asign the values to a varibales conditionally
# # we will use this only for simple and short requirement purpose  only 



# print("true statement") if not True else print("false statement")


username_match=True
password_match=False
# print("login succuess")if username_match and password_match else print("login failed")
print("login succuess")if username_match and password_match else print("user name is  incorrect") if not username_match and password_match else print("password in corect")  
# print("both incorrect") if not username_match and not password_match



def name():
    a=20
    def name2():
        nonlocal a
        a=30

    name2()
    print(a)
name()
#       # Output: 30

# for i in range(20,51):
#     if(i%3==0):
#        print(i)

str="something"
for x in range(len(str)-1,-1,-1):
    print(str[x])

ip="hello"
op=""
for x in range(len(ip)-1,-1,-1):
    op+=ip[x]   
print(op)    





l1=["sravan","harish","aravind","akhil"]
l2=[24,17,20,18]

for x in range(0,len(l1)):
    if l2[x]>=18:
        print("eligibel")
    else:
        print  (" not eligible")


# addition of integer number sum 
n=123498
m=str(n)
res=0
for i in range(len(str(n))):
  res+=  int(m[i])
print(res)

# greatest  amoung the interger value

# n = 123498
# m = str(n)
# res = -1
# for digit in m:
#     if int(digit) > res:
#         res = int(digit)
# print("Maximum digit:", res)


ip=['s','h','i','v','a']
op=""
for x in ip:
    op+=x
print(op)

ip=['s','h','i','v','a']
op=""
for x in range(len(ip)-1,-1,-1):
    op+=ip[x]
    op+="_"
print(op)


n = 123498
m = str(n)
res = 1
for digit in m:
     if int(digit) <=res:
         res = int(digit)
print("Maximum digit:", res)


# ip=[4,7,9,1,2,6]
# smallest=ip[0]
# for x in ip:
#      if x<smallest:
#           smallest=x
#           print(smallest)          


lod=[{ 'movie':'coolie', 'language':'tamil', 'budget':300},
{ 'movie':'war2', 'language':'hindi', 'budget':300}
     ,{ 'movie':'kingdom', 'language':'telugu', 'budget':300}
,{ 'movie':'f2', 'language':'english', 'budget':300}]
for x in lod:
    if (x['language']=='telugu'):
        print(x)




# ip=125478
# rev=0
# while(ip>0):
#     id=ip%10
#     rev=rev*10+id
#     ip=ip//10
# print(rev)


# ip=125
# sum=0
# while(ip>0):
#     id=ip%10
#     sum+=id
#     ip=ip//10
# print(sum)    


  
# ip=125
# count=0
# while(ip>0):
#     count+=ip%10
#     ip=ip//10
# print(count)

# ip=1256
# count=0
# while(ip>0):
#     count+=1
#     ip=ip//10
# print(count)


ip=1234
count=0
id=0
while(ip>0):
    rem=ip%10
    if rem%2==0:
        print("even")
    else:
        print("odd")
    ip//=10    

# def is_Armstrong(n):
#     temp = n
#     power = 0
#     # Count digits
#     while temp > 0:
#         power += 1
#         temp //= 10

#     temp = n
#     total = 0
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** power
#         temp //= 10

#     return total == n
# print(is_Armstrong(153))


# create a list of numbers using compresssion

# op=[x**2 for x in range(1,11) ]
# print(op)

# create list of even number usong list compresions
   
# op=[x for x in range(1,11) if x%2==0]
# print(op)


# ip=[1,4,7,9,11,13,24,56,108,234,225]
# op=[ x*2 for x in ip  if x%2==0]
# print(op)



# num=123
# res=0
# while num>0:
#     r=num%10
#     res+=r
#     num//=10
# print(res)



num=(int(input()))
res=num**2
sul=0
while res>0:
    r=res%10
    sul+=r
    res//=10
if sul==num:
        print("neon number")
else:
        print("not neon number")

# n=11
# f=0
# for i  in range(2,n):
#    if i%2==0:
#       f=1
#       break
# if(f==0 and n>1):
#     print("prime number")
# else:
#     print("not a  prime number")



# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         i%2==0
#         return False
#     return True
# n=11
# print(is_prime(n))

# n=17
# f=0
# for i in range(1,n//2):
#     if i**2==n:
#         f=1
#         break
# if f==0:
#     print("not perfect square")
# else:
#     print("perfect square")    


# n=145
# a=n 
# res=0
# while n>0:
#     r=n%10
#     f=1
#     for i in range(1,r+1):
#         f*=i
#     res+=f
#     n//=10
# if res==a:
#     print("strong number")
# else:
#     print("not strong number")



x="aabbaaccbb"
count={}
for i in x:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
res=""

for i in count:
    res=res+i+str(count[i])
print(res)



s="aaaabbbb"
l=[]
res="" 
for i in s :
    if i not in l:
        l.append(i)
        res=res+i+str(count[i])
print(count[i])
print(res)




s="aabbccaabbcc"
res=s[0]
c=1 
for i in  range(1, len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        res=res+str(c)+s[i]
        c=1
res+=str(c)
print(res)


a=10
b=20
c=4

if a>b and a>c:
    if b>c:
        print(a+b)
    else:
        print(a+c)
elif b>a and b>c:
    if a>c:
        print(a+b)
    else:
        print(b+c)
else:
     if a>b:
         print(a+c)
     else:
         print(a+b)



a=[1,2,3,4,5]

l1=a[len(a)-2::]+a[0:len(a)-2]
print(l1)






    




       










    

      
    
    









   
      
    
