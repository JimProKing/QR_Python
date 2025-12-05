from pathlib import Path
from step_1_1 import OUT_DIR
import qrcode

data = [
    "BEGIN:VCARD",
    "VERSION:3.0",
    "N:Lee;Young Chan;;;",
    "FN:Young Chan Lee",
    "TEL;TYPE=CELL:+82 10-8706-2516",
    "EMAIL:caramel2516@naver.com",
    # 새 집 주소
    "ADR;TYPE=HOME:;;김해시 대동면 동남로585번길 9, 2층집;김해시;;;대한민국",
    # 한 줄로 예쁘게 보이게 LABEL 추가 (아이폰·안드로이드 추천)
    "LABEL;TYPE=HOME:김해시 대동면 동남로585번길 9\\n2층집",
    "END:VCARD"
]

vcf = "\n".join(data) + "\n"

# vCard 파일 저장
vcf_path = OUT_DIR / f"{Path(__file__).stem}.vcf"
with open(vcf_path, "w", encoding="utf-8") as fp:
    fp.write(vcf)

print(f"vCard 저장 완료 → {vcf_path}")

# QR 코드 생성 & 저장
img = qrcode.make(vcf)
img.show()

qr_path = OUT_DIR / f"{Path(__file__).stem}_qr.png"
img.save(qr_path)
print(f"QR 코드 저장 완료 → {qr_path}")