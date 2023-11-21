import qrcode
from PIL import Image


qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=30,border=10)

qr.add_data("https://www.youtube.com/watch?v=_zIUMus7ybw")
qr.make(fit=True)
img=qr.make_image(fill_color="orange",back_color="black")
img.save("peking_espanol_youtube.png")