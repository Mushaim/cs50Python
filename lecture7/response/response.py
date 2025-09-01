import validators

def main():
    print(validate(input("Whats your email address: ")))

def validate(e):
    if(validators.email(e)):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()

