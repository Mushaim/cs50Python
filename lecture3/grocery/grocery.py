grocery = {}

def add_grocery():
    if item in grocery:
        grocery[item] += 1
    else:
        grocery[item] = 1

while True:
    try:
        item = input().strip().lower()
        add_grocery()
    except EOFError:
          break

for item in sorted(grocery):
    print(grocery[item],item.upper())


