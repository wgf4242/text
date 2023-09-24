from cryptography.fernet import Fernet

f=Fernet(b'Erj5UoZfpxT47Bjpg8qg1XmMCKZyKBj1bJ0otszVZPk=')
miwen=b'gAAAAABk2vY8KwxIv0n9XgVk8EPbQimR9iCqSX_crxcRSf-z2RV2rX2Ol1KHmbeAsxOyGR_i73vrl0FgLDCHHP9wWaXz37r5NmaWFXCwETQ2tYJM8vIFJVZ1Ptmtt2O7fXPQg6xA5-_dFOi-FYjF2RiqfXc39rbBLA=='
mingwen=f.decrypt(miwen).decode()
print(mingwen)

## here is your flag CnHongKe{*****************}