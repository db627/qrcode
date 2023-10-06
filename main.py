import qrcode
import os.path
from config import Config

def create_qr_code_image(data: str):
    """Generate QR Code"""

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill='black', back_color='white')



def main():
    full_path = os.getcwd()

    directory_path_and_file_name = os.path.join(full_path, Config.QR_CODE_IMAGE_DIRECTORY, Config.QR_CODE_DEFAULT_FILE_NAME)

    qr_image = create_qr_code_image(Config.QR_CODE_DEFAULT_URL)
    for i in range(0, 1):
        while True:
            try:
                qr_image.save(directory_path_and_file_name)
            except FileNotFoundError:
                qr_image_directory = Config.QR_CODE_IMAGE_DIRECTORY
                new_directory_path = os.path.join(full_path, qr_image_directory)
                os.mkdir(new_directory_path)
                continue
            break


if __name__ == "__main__":
    main()