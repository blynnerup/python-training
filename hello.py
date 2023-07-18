msg = "Hello, World!"
print(msg)

times = input("How many times do I need to tell you to clean your room?")
times = int(times)

for t in range(times):
    print ("CLEAN YOUR ROOM!")
    
for num in range(1,21):
    if int(num) == 4 or num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")