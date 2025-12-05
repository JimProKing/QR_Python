from pathlib import Path
import qrcode
from qrcode.image.styledpil import StyledPilImage
from step_1_1 import IN_DIR
from step_2_2 import OUT_2_2_VCF

# 1. vCard 데이터 읽기
with open(OUT_2_2_VCF, encoding="utf-8") as fp:
    vcf = fp.read()

# 2. QRCode 객체 생성할 때 반드시 ERROR_CORRECT_H 설정!
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,   # 이 줄이 핵심!!!
    box_size=10,
    border=4,
)

qr.add_data(vcf)
qr.make(fit=True)   # 자동으로 최적 버전 선택

# 3. 가운데에 로고 넣기 (StyledPilImage 사용)
img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path=IN_DIR / "me.jpeg",   # 이게 오타였음! → embedded_image_path
    # 아래 옵션들은 취향대로 조절
    # eye_color="black",
    # color_mask=qrcode.image.styles.colormasks.SolidFillColorMask(back_color=(255,255,255), front_color=(0,0,0)),
)

img.show()          # 화면에 바로 띄우기
img.save(IN_DIR.parent / "QR_with_logo.png")  # 저장도 해놓자