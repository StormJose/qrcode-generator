import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# data = "https://awoiaf.westeros.org/index.php/Main_Page"

print('Insira seu link')

data = input()



qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr_code.png")

