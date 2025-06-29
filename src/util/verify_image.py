from fastapi import UploadFile
from PIL import Image


def verify_image(file: UploadFile):
    # try:
    # Membuka file dengan Pillow (PIL) untuk memverifikasi apakah itu gambar
    #     image = Image.open(file.file)
    #     image.verify()  # Verifikasi apakah file tersebut adalah gambar yang valid
    #     return True
    # except Exception:
    #     return False

    allowed_extensions = ["jpg", "jpeg", "png", "gif"]
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in allowed_extensions:
        return False
    return True