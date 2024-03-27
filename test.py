import phonenumbers
from phonenumbers import geocoder

def joylashuvni_aniqlash(raqam):
    try:
        raqam_obj = phonenumbers.parse(raqam, None)
        if not phonenumbers.is_valid_number(raqam_obj):
            return "Noto'g'ri telefon raqami formati"
        joylashuv = geocoder.description_for_number(raqam_obj, "uz")
        return joylashuv
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Noto'g'ri telefon raqami formati"

# Telefon raqamini kiritish
raqam = input("Joylashuvni aniqlash uchun telefon raqamini kiriting: ")

# Joylashuvni aniqlash
natija = joylashuvni_aniqlash(raqam)
print("Telefon raqamingizga mos joylashuv:", natija)
