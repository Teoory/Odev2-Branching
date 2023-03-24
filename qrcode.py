import qrcode



qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)

data = 'https://oyunveuygulamaakademisi.com'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(Fill='black', back_color='white')
img.save('test_Code5.png')