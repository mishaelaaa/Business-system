import qrcode
#qr code lib

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

#data for qr code
_val_ = input("Enter the number of machine and detail number : ");
data = _val_
print(data)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('demo_1.png')
#create img with qr