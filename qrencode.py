__author__ = 'kevin.zhu'

import base64
import qrcode


def genQRcode(method,password,hostname,port):
    s = method + ':' + password + '@' + hostname + ':' + port
    encode = base64.b64encode(s)
    url = 'ss://'+encode
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    img.show()



