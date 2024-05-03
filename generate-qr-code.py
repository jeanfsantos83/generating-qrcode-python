import pyqrcode
import png
from pyqrcode import QRCode

# Link desejado para o QRCCode #
QRString = 'https://github.com/jeanfsantos83'

# Monta o QRCode #
url = pyqrcode.create(QRString)

# Salva o QRCode gerado no local desejado #
url.png(r'qr.png', scale=8)