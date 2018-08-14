from PIL import Image
img = Image.open("/home/junior/Downloads/1-dados-bancarios.jpg")
w = int(img.size[0] / 3)
h = int(img.size[1] / 3)
img = img.resize((w, h), Image.ANTIALIAS)
print(img.size)
img.save("/home/junior/Downloads/1-dados-bancarios_low.jpg", quality=95)
#img.save("/home/junior/Downloads/identidade_res2.jpg", optimize=True, quality=65)