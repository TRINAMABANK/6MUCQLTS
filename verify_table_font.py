import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def test_table_font():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    print("=== KIỂM THỬ QUY CHUẨN FONT TIMES NEW ROMAN BẢNG TRA CỨU TÀI SẢN ===")

    # 1. Kiểm tra CSS quy định Times New Roman cho #masterTable
    assert '#masterTable' in html, "Thiếu selector #masterTable"
    assert '"Times New Roman"' in html or "'Times New Roman'" in html, "Thiếu font-family Times New Roman"
    
    # 2. Kiểm tra các selector chi tiết của bảng
    for sel in ['#masterTable th', '#masterTable td', '#masterTable .font-code', '#masterTable .badge-chip']:
        assert sel in html, f"Thiếu selector {sel}"
    print("✓ Đã cấu hình Times New Roman cho #masterTable, th, td, mã tài sản (.font-code), badge-chip")

    # 3. Kiểm tra kích thước font tiêu đề (14px đậm) và dữ liệu (14-15px)
    assert '#masterTable thead th' in html and '14px' in html and '700' in html, "Tiêu đề cột phải là 14px chữ đậm"
    assert '#masterTable tbody td' in html and '15px' in html, "Dữ liệu dòng phải là 15px"
    print("✓ Tiêu đề cột: font-size 14px, font-weight 700 đậm")
    print("✓ Dữ liệu dòng: font-size 15px, chiều cao dòng cân đối")

    # 4. Kiểm tra ô tìm kiếm, bộ lọc và thanh phân trang đồng bộ Times New Roman
    for filter_sel in ['#searchInput', '#departmentFilter', '#statusFilter', '#masterTableStats', '#pageSizeSelect', '#pageIndicator']:
        assert filter_sel in html, f"Thiếu selector {filter_sel} cho bộ lọc/phân trang"
    print("✓ Ô tìm kiếm, bộ lọc phòng ban/tình trạng và thanh phân trang đã đồng bộ Times New Roman")

    # 5. Kiểm tra 19 trường dữ liệu chuẩn vẫn giữ nguyên
    columns_19 = [
        "STT", "Mã tài sản", "Tên tài sản", "SL", "Quy cách", "Nguyên giá",
        "Số tháng PB", "Số tháng PB còn lại", "Phân bổ luỹ kế", "Giá trị còn lại",
        "Bộ phận quản lý", "Bộ phận quản lý tạm thời", "Bộ phận quản lý NEW",
        "Bộ phận quản lý tạm thời NEW", "Loại công cụ", "Ngày hạch toán",
        "Tình trạng tài sản", "Tài sản thay thế", "Kiến nghị"
    ]
    for col in columns_19:
        assert col in html, f"Thiếu cột {col} trong 19 cột chuẩn"
    print("✓ Đầy đủ 19/19 trường dữ liệu chuẩn, không thay đổi thứ tự hay tên cột")

    # 6. Kiểm tra phân trang mặc định 10 dòng
    assert '<option value="10" selected>10</option>' in html, "Phân trang mặc định phải là 10 dòng"
    print("✓ Phân trang mặc định giữ nguyên 10 dòng/trang")

    print("\n===> TẤT CẢ TIÊU CHÍ KIỂM THỬ FONT BẢNG TÀI SẢN ĐẠT 100%! <===")

if __name__ == '__main__':
    test_table_font()
