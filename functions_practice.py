def hello():
    print("Hello there!")

hello()

def pack(lunch, drink, snack):
    return(lunch, drink, snack)

print(pack("sandwich", "water", "apple"))

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else: 
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else: 
                print(f"Next I eat {my_list[i]}")

eat_lunch([])
eat_lunch(("food",))
eat_lunch(("sandwich", "apple", "granola bar"))