def main(num):
    if num <=2:
        print(f"{num} is prime")
        # return True
    else:
        for i in range(3, num): # 遍历完此处
            if num%i == 0:
                print(f"{num} is not prime")
                return
        print(f"{num} is Prime.")
        return 
        

main(5)
main(8)
