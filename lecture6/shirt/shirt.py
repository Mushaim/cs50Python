import sys
from PIL import Image,ImageOps

if len(sys.argv) != 3:
    sys.exit("Number of arguments not correct")

extensions = ["png","jpg","jpeg"]

input_file = sys.argv[1].lower()
output_file = sys.argv[2].lower()

if not (input_file.endswith(ext) for ext in extensions):
    sys.exit("Input does not have valid extension")
if not (output_file.endswith(ext) for ext in extensions):
    sys.exit("Output does not have valid extension")

if input_file.split(".")[-1] != output_file.split(".")[-1]:
    sys.exit("Extensions do not match")

try:
    img = Image.open(input_file)
    shirt = Image.open("shirt.png")
except FileNotFoundError as e:
    sys.exit(f"File not found {e}")

resized = ImageOps.fit(img,shirt.size)
resized.paste(shirt,shirt)
resized.save(output_file)



