def main():
    file_name = take_input()
    check_extension(file_name)

def take_input():
    file_name = input("File name: ")
    return file_name.lower().strip()

def check_extension(file_name):
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        print("image/jpeg",end="")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()