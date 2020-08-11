# Extract CRT & KEY From P12 File

openssl pkcs12 -in filename.pfx -nocerts -out filename.key

openssl pkcs12 -in filename.pfx -clcerts -nokeys -out filename.crt

# Decrypt Private Key

openssl rsa -in ssl.key.encrypted -out ssl.key.decrypted
