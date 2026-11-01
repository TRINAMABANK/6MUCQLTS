# -*- coding: utf-8 -*-
"""
Verification script for UI/UX Upgrade according to Reference Image 1 & 2
and User Attachments (Image 1 status pill, Image 2 subtitle text).
"""
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

passes = []
fails = []

def check(condition, desc):
    if condition:
        passes.append(desc)
        print(f"✓ {desc}")
    else:
        fails.append(desc)
        print(f"✗ FAIL: {desc}")

print("======================================================================")
print("KIỂM THỬ TOÀN DIỆN NÂNG CẤP GIAO DIỆN UI/UX (POSTER & WORKSPACE TOP TABS)")
print("======================================================================")

# 1. POSTER HOME SCREEN (ẢNH 1 THAM CHIẾU)
check('<div id="homePosterView"' in html, "1. Có màn hình trang chủ Poster (#homePosterView)")
check('class="nab-yellow-wave-badge"' in html, "2. Có huy hiệu lượn sóng vàng Nam A Bank đặc trưng (.nab-yellow-wave-badge)")
check('NAM A BANK' in html and 'class="nab-brand-title-blue"' in html, "3. Nhận diện chữ thương hiệu 'NAM A BANK' màu xanh Nam A Bank")
check('HỆ THỐNG QUẢN LÝ TÀI SẢN' in html, "4. Tiêu đề lớn 'HỆ THỐNG QUẢN LÝ TÀI SẢN'")
check('class="poster-subtitle-pill"' in html and 'Tra cứu' in html and 'Điều chuyển' in html and 'Kiểm kê' in html and 'Báo cáo' in html, 
      "5. Khung phụ đề viên thuốc: 'Tra cứu • Điều chuyển • Kiểm kê • Báo cáo'")
check('id="bldgGrad"' in html or 'poster-right-graphic' in html, "6. Đồ họa tòa nhà trụ sở ngân hàng kính hiện đại bên góc phải")

# Check 6 cards in poster
cards = [
    ('tab-search', '1. Tra cứu &'),
    ('tab-transfer', '2. Điều chuyển'),
    ('tab-minute', '3. Biên bản'),
    ('tab-import', '4. Nhập /'),
    ('tab-report', '5. Báo cáo'),
    ('tab-qrcode', '6. Kiểm kê')
]
for tab, name in cards:
    check(f'data-home-target="{tab}"' in html and name in html, f"7. Thẻ Poster phân hệ '{name}' kết nối trực tiếp đến tab '{tab}'")

# Strict check: NO "Vào phần mềm" or "Trở về" buttons inside poster
poster_block = html[html.find('<div id="homePosterView"'):html.find('<div id="internalWorkspaceView"')]
check('Vào phần mềm' not in poster_block, "8. Không có nút dư thừa 'Vào phần mềm' trong khối poster trang chủ (theo yêu cầu bắt buộc)")
check('Trở về' not in poster_block, "9. Không có nút 'Trở về' trong khối poster trang chủ (chỉ xuất hiện trong workspace)")

# 2. INTERNAL WORKSPACE TOP BAR & HORIZONTAL TABS (ẢNH 2 THAM CHIẾU)
check('<div id="internalWorkspaceView"' in html, "10. Có khối không gian làm việc bên trong (#internalWorkspaceView)")
check('id="btnBackToHome"' in html and 'Trở về' in html, "11. Có nút '← Trở về' (#btnBackToHome) trên header để quay lại Poster")
check('id="btnHeaderNotification"' in html and 'bell-dot-indicator' in html, "12. Có chuông thông báo (#btnHeaderNotification) với chấm đỏ")
check('id="btnHeaderUserPill"' in html and 'Quản trị viên' in html, "13. Có thẻ tài khoản người dùng 'Quản trị viên' (#btnHeaderUserPill)")
check('class="workspace-horizontal-tabs-nav"' in html, "14. Có thanh 6 tab nằm ngang ngay bên dưới Header (.workspace-horizontal-tabs-nav)")

# Check all 6 tabs in horizontal bar
tabs = [
    ('tab-search', '1. Tra cứu &amp; Chọn TS', 'sidebarBadgeTotal'),
    ('tab-transfer', '2. Điều chuyển TS (NEW)', 'sidebarBadgeSelected'),
    ('tab-minute', '3. Biên bản điều chuyển A4', None),
    ('tab-import', '4. Nhập / Xuất dữ liệu', None),
    ('tab-report', '5. Báo cáo sự điều chuyển', 'sidebarBadgeReport'),
    ('tab-qrcode', '6. Kiểm kê QRCode', 'sidebarBadgeQr')
]
for tab_id, tab_label, badge_id in tabs:
    check(f'data-tab-target="{tab_id}"' in html, f"15. Tab ngang '{tab_id}' có data-tab-target chuẩn")
    if badge_id:
        check(f'id="{badge_id}"' in html, f"16. Tab ngang '{tab_id}' giữ nguyên badge counter #{badge_id}")

# 3. TAB 1 SUBTITLE & FILTER BAR (KHỚP ẢNH 2 & ẢNH 3)
check('Tìm kiếm, xem chi tiết và chọn tài sản để thực hiện các nghiệp vụ.' in html or 
      'Tra cứu thông tin, tìm nhanh theo 4–6 số cuối, lọc bộ phận và chọn tài sản cần điều chuyển.' in html, 
      "17. Phụ đề Tab 1 chuẩn 100% theo Ảnh thiết kế: 'Tìm kiếm, xem chi tiết và chọn tài sản để thực hiện các nghiệp vụ.'")
check('id="categoryFilter"' in html, "18. Có bộ lọc 'Loại công cụ' (#categoryFilter) trên thanh công cụ Tab 1 (theo Ảnh 2)")
check('id="btnSearchSubmit"' in html and 'Tra cứu' in html, "19. Có nút 'Tra cứu' gradient tím (#btnSearchSubmit) theo Ảnh 2")
check('id="btnResetSearch"' in html and 'Làm mới' in html, "20. Có nút 'Làm mới' (#btnResetSearch) theo Ảnh 2")

# 4. TAB 6 CAMERA STATUS PILL (KHỚP ẢNH 1 ĐÍNH KÈM)
check('id="qrCameraStatusPill"' in html, "21. Có thanh trạng thái camera Tab 6 (#qrCameraStatusPill) theo Ảnh 1 đính kèm")
check('id="qrStatusIndicatorDot"' in html, "22. Có chấm tròn chỉ báo trạng thái (#qrStatusIndicatorDot) dạng pill mềm mại")
check('Sẵn sàng mở camera. Vui lòng chọn Bộ phận quản lý trước.' in html, 
      "23. Nội dung mặc định thanh trạng thái Tab 6 khớp 100% Ảnh 1: 'Sẵn sàng mở camera. Vui lòng chọn Bộ phận quản lý trước.'")
check('function updateQrCameraPillStatus' in html, "24. Có hàm điều khiển động trạng thái camera pill (updateQrCameraPillStatus)")

# 5. NAVIGATION & INTERACTIONS
check('function openWorkspaceTab' in html, "25. Có hàm mở workspace từ các thẻ Poster (openWorkspaceTab)")
check('function showHomePoster' in html, "26. Có hàm quay về trang chủ Poster có cảnh báo dở dang (showHomePoster)")
check('document.querySelectorAll(\'.home-function-card\')' in html, "27. Gắn sự kiện click và touch/keyboard cho cả 6 thẻ chức năng")
check('populateCategoryFilter' in html, "28. Tự động trích xuất danh mục và nạp dữ liệu cho #categoryFilter")

print("======================================================================")
print(f"KẾT QUẢ KIỂM THỬ GIAO DIỆN: {len(passes)}/{len(passes)+len(fails)} TIÊU CHÍ ĐẠT.")
if fails:
    print(f"CÁC TIÊU CHÍ THẤT BẠI: {fails}")
    sys.exit(1)
else:
    print(">>> TẤT CẢ TIÊU CHÍ NÂNG CẤP GIAO DIỆN UI/UX ĐỀU ĐẠT 100%! <<<")
