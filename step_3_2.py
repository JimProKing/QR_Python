from pathlib import Path
from PIL import Image
from step_1_1 import IN_DIR, OUT_DIR
from step_2_2 import OUT_2_2_PNG

OUT_3_2 = OUT_DIR / f"{Path(__file__).stem}.png"

if __name__ == "__main__":
    # 1. 기존 QR 코드 열기
    qr = Image.open(OUT_2_2_PNG).convert("RGBA")
    width_qr, height_qr = qr.size
    
    # 2. 로고 이미지 열기 (너는 me.jpeg 쓰고 싶겠지?)
    icon = Image.open(IN_DIR / "me.jpeg").convert("RGBA")
    
    # 3. 로고 크기 조절 (QR 크기의 20%)
    width_icon = int(width_qr * 0.2)
    height_icon = int(height_qr * 0.2)
    icon_resized = icon.resize((width_icon, height_icon), Image.Resampling.LANCZOS)
    
    # 4. 우측 하단 위치 계산 (pad = 여백)
    pad = 50
    icon_x = width_qr - width_icon - pad
    icon_y = height_qr - height_icon - pad
    
    # 5. 로고 붙이기 (mask로 투명도 처리)
    qr.paste(icon_resized, box=(icon_x, icon_y), mask=icon_resized)
    
    # 6. 저장 & 화면에 띄우기
    qr.save(OUT_3_2)
    qr.show()
    print(f"완료! 저장: {OUT_3_2}")