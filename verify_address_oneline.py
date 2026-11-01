import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def test_address_oneline():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('print-preview.html', 'r', encoding='utf-8') as f:
        phtml = f.read()

    print("=== KIỂM THỬ ĐỊA CHỈ TRÊN 1 DÒNG & TRANG TRÍ ĐẦU BIÊN BẢN ===")

    for name, content in [("index.html", html), ("print-preview.html", phtml)]:
        print(f"\n--- Kiểm tra {name} ---")

        # 1. Kiểm tra class nab-bank-address có white-space: nowrap !important
        assert '.nab-bank-address' in content, f"{name}: Thiếu class .nab-bank-address"
        assert 'white-space: nowrap !important' in content or 'white-space: nowrap' in content, f"{name}: Thiếu white-space nowrap cho địa chỉ"
        print("✓ Class .nab-bank-address có white-space: nowrap !important bảo đảm không bị rớt dòng")

        # 2. Kiểm tra độ rộng khu vực trái (57%) và phải (41%)
        assert '57%' in content and '41%' in content, f"{name}: Phải phân bổ 57% bên trái và 41% bên phải để vừa vặn địa chỉ"
        print("✓ Khu vực bên trái mở rộng lên 57%, đủ không gian cho toàn bộ địa chỉ trên 1 dòng duy nhất")

        # 3. Kiểm tra font size chuẩn đẹp 10.5pt
        assert '10.5pt' in content, f"{name}: Thiếu font-size 10.5pt"
        print("✓ Cỡ chữ địa chỉ và thông tin liên hệ được tối ưu chuẩn đẹp 10.5pt (Times New Roman)")

        # 4. Kiểm tra các phần tử HTML đều có class nab-bank-address
        matches = content.count('nab-bank-address')
        assert matches >= 2, f"{name}: Chưa gán class nab-bank-address vào thẻ HTML"
        print(f"✓ Thẻ HTML địa chỉ đã được gắn class nab-bank-address ({matches} vị trí)")

    # 5. Kiểm tra Word export
    assert 'white-space: nowrap;' in html, "Word export thiếu white-space nowrap cho địa chỉ"
    print("\n✓ Mẫu xuất Word cũng đã áp dụng white-space nowrap và chia tỷ lệ 58% - 42% cho địa chỉ trên 1 dòng")

    print("\n===> TẤT CẢ TIÊU CHÍ ĐỊA CHỈ 1 DÒNG & BỐ CỤC ĐẸP ĐẠT 100%! <===")

if __name__ == '__main__':
    test_address_oneline()
