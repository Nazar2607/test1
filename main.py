from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")

top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")

print(top_text, bottom_text)

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")

image_number = int(input("Введите номер"))

if image_number == 1:
  image_file = ("Кот в ресторане.png")
elif image_number == 2:
  image_file = ("Кот в очках.png")


image = Image.open(image_file) #открываем изображение для редоктирования
width, height = image.size#ширина и высота картинки

draw = ImageDraw.Draw(image)#добовляем текст на картинку

font = ImageFont.truetype("arial.ttf",size=70)#создаём шрифт

text = draw.textbbox((0, 0), top_text, font))#узнаём сколько по ширине и высоте(верхний текст)
text_width = text[2]


draw.text(((width - text_width)/ 2, 10), top_text, font=font, fill = "black")#указываем координаты текста(делаем так чтобы надпись была по середине)

text = draw.textbbox((0, 0), bottom_text, font)#узнаём сколько по ширине и высоте(нижний текст)
text_width = text[2]#второй компанент text(ширина)
text_height = text[3]#(высота)

draw.text(((width - text_width)/ 2, height - text_height - 10), bottom_text, font=font, fill = "black") #делаем зазоры в нижним и верхним тексте тексте


image.save("new_name.jpg")