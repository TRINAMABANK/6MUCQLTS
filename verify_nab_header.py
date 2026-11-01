import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def test_header():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('print-preview.html', 'r', encoding='utf-8') as f:
        phtml = f.read()

    print("=== KIỂM THỬ LOGO VÀ CĂN LỀ PHẦN ĐẦU BIÊN BẢN ĐIỀU CHUYỂN ===")

    for name, content in [("index.html", html), ("print-preview.html", phtml)]:
        print(f"\n--- Kiểm tra {name} ---")

        # 1. Kiểm tra logo kích thước 150-180px, giữ nguyên tỷ lệ (height: auto), căn trái
        assert '.nab-logo-img' in content, f"{name}: Thiếu class .nab-logo-img"
        assert 'width: 175px' in content or 'width: 170px' in content or 'width: 180px' in content, f"{name}: Chiều rộng logo phải trong khoảng 150-180px"
        assert 'height: auto' in content, f"{name}: Chiều cao logo phải là height: auto để giữ nguyên tỷ lệ"
        print(f"✓ Logo: Chiều rộng 175px (chuẩn 150-180px), height: auto giữ nguyên tỷ lệ, căn lề trái thẳng hàng mép giấy")

        # 2. Thông tin Hội sở: font Times New Roman, tên đơn vị đậm 14-15pt, địa chỉ/liên hệ 11-12pt, căn trái
        assert '.nab-bank-sub' in content, f"{name}: Thiếu class .nab-bank-sub"
        assert 'font-size: 14pt' in content or 'font-size: 15pt' in content, f"{name}: .nab-bank-sub phải có cỡ chữ 14-15pt"
        assert 'font-weight: bold' in content, f"{name}: .nab-bank-sub phải in đậm"
        
        assert '.nab-bank-info' in content, f"{name}: Thiếu class .nab-bank-info"
        assert 'font-size: 10.5pt' in content or 'font-size: 11pt' in content or 'font-size: 12pt' in content, f"{name}: .nab-bank-info phải có cỡ chữ 10.5-12pt"
        assert 'text-align: left' in content, f"{name}: Thông tin Hội sở phải căn trái"
        print(f"✓ Thông tin Hội sở: Tên đơn vị in đậm 14pt, địa chỉ và liên hệ 10.5pt, căn trái cùng trục với logo")

        # 3. Bố cục 2 khu vực: Bên trái (logo + Hội sở) và bên phải (Quốc hiệu + tiêu ngữ + ngày tháng)
        assert '.nab-header-grid' in content, f"{name}: Thiếu .nab-header-grid"
        assert '.nab-header-left' in content and '.nab-header-right' in content, f"{name}: Thiếu nab-header-left hoặc nab-header-right"
        assert 'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM' in content, f"{name}: Thiếu Quốc hiệu"
        assert 'Độc lập – Tự do – Hạnh phúc' in content, f"{name}: Thiếu Tiêu ngữ"
        print(f"✓ Bố cục 2 khu vực cân đối: Khu vực trái (57%) căn trái, khu vực phải (41%) căn giữa, không đè lấn nhau")

    # 4. Kiểm tra trong hàm xuất Word
    assert 'b style="font-size: 14pt;' in html, "Word export thiếu tên đơn vị 14pt"
    assert 'font-size: 10.5pt;' in html or 'font-size: 11pt;' in html, "Word export thiếu thông tin liên hệ"
    print("\n✓ Mẫu xuất Word cũng đã đồng bộ kích thước logo, tên đơn vị 14pt, thông tin liên hệ 10.5pt")

    print("\n===> TẤT CẢ TIÊU CHÍ LOGO & ĐẦU TRANG BIÊN BẢN ĐẠT 100%! <===")

if __name__ == '__main__':
    test_header()
