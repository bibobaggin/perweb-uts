

# def fibo(n):
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
    
# print(fibo(5))

# call_count = 0
# def fibo(n):
#     global call_count
#     call_count += 1
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# print(fibo(5))
# print(f"fibo was called {call_count} times")

c={
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

for x in c:
    print(x,end="#")

for y in c.values():
    print(y,end="#")
a=("kucing","kambing","kangguru","kelinci","komodo","kera")
print((a[2:6]))

print(c)