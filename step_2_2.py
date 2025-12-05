from pathlib import Path
import qrcode
from step_1_1 import OUT_DIR

OUT_2_2_VCF = OUT_DIR / f"{Path(__file__).stem}.vcf"
OUT_2_2_PNG = OUT_DIR / f"{Path(__file__).stem}.png"

if __name__ == "__main__":
    data = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        "N:이;영찬;;;",
        "FN:이영찬",
        "TEL;type=CELL:+82 10-8706-2516",
        "END:VCARD",
    ]
    vcf = "\n".join(data)

    with open(OUT_2_2_VCF, "w", encoding="utf-8") as fp:
        fp.write(vcf)

    # 이 방식이 제일 깔끔하고 에러 안 남!
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # 또는 H
        box_size=10,
        border=4,
    )
    qr.add_data(vcf)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(OUT_2_2_PNG)