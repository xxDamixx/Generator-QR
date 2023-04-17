# -*- coding: utf-8 -*-
# autor: Damian Popławski
import qrcode
from PIL import Image


print("Podaj link lub tekst do utworzenia kodu QR")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(str(input()))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
print("Podaj nazwę dla utworzonego pliku")
img.save((str(input())) + ".png")
