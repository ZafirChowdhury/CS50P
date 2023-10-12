import sys
from PIL import Image, ImageOps

extension = ["jpg", "jpag", "png"]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    if "." not in (sys.argv[1] + sys.argv[2]):
        sys.exit("File extension missing")

    else:
        name1, ex1 = sys.argv[1].split(".")
        name2, ex2 = sys.argv[2].split(".")

        if ex1 != ex2 and ex1 in extension and ex2 in extension:
            sys.exit("Input and output have different extensions")

        if ex1 not in extension or ex2 not in extension:
            sys.exit("Invalid output")

        try:
            shirt = Image.open("shirt.png")
            size = shirt.size

            with Image.open(sys.argv[1]) as image:
                image = ImageOps.fit(image, size)
                image.paste(shirt, shirt)
                image.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("Input does not exist")