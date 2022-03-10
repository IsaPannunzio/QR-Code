import pyqrcode

site = input('Digite um site: ')
pyqrcode.create(site).png('qrcode.png', scale=20)