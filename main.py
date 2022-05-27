from twofish import Twofish
T = Twofish(b'123456789611')
x = T.encrypt(b'YELLOWSUBMARINES')
print(x)
print(T.decrypt(x).decode())
