def main():
    height = get_height
    for i in range(height):
        print("#")

def get_height():
    while True:
        try:
            h = int(input("Enter a height: "))
            if h > 0:
                break
        except:
            print("It is not an integer")
    return h

main()
