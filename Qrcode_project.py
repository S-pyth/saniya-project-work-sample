import qrcode 
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_data("My skill in python")
qr.make(fit=True)
image=qr.make_image(fill_color="brown",back_color="white")
image.save("project_1.png")
