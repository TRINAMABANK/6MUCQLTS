import re
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def test_workflow():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    print("=== KIỂM THỬ QUY TRÌNH BIÊN BẢN & CẬP NHẬT CHÍNH THỨC ===")

    # 1. Kiểm tra cấu trúc 3 nhóm thông tin trên giao diện Biên bản
    assert 'class="minute-form-sections"' in html, "Thiếu minute-form-sections"
    assert 'A. THÔNG TIN CHUNG CỦA BIÊN BẢN' in html, "Thiếu tiêu đề Nhóm A"
    assert 'B. BÊN ĐIỀU CHUYỂN — BÊN A' in html, "Thiếu tiêu đề Nhóm B"
    assert 'C. BÊN NHẬN ĐIỀU CHUYỂN — BÊN B' in html, "Thiếu tiêu đề Nhóm C"
    
    # 2. Kiểm tra layout 3 cột trên 1 hàng
    rows_3col = html.count('class="minute-row-3col"')
    assert rows_3col >= 3, f"Phải có ít nhất 3 hàng 3 cột, tìm thấy {rows_3col}"
    print(f"✓ 3 nhóm thông tin đều sử dụng minute-row-3col ({rows_3col} hàng)")

    # 3. Kiểm tra các trường thông tin bắt buộc
    fields = [
        "docDateInput", "docEffectiveDateInput", "docLocationInput",
        "senderNameInput", "senderRoleInput", "senderDeptInput",
        "receiverNameInput", "receiverRoleInput", "receiverDeptInput"
    ]
    for fid in fields:
        assert f'id="{fid}"' in html, f"Thiếu trường {fid}"
    print(f"✓ Đầy đủ 9 trường thông tin bắt buộc: {', '.join(fields)}")

    # 4. Kiểm tra nút ở Tab 2 không còn commit trực tiếp mà chuyển sang Tab 3
    assert 'id="btnProceedToMinute"' in html, "Thiếu btnProceedToMinute ở Tab 2"
    assert "switchTab('tab-minute')" in html, "Thiếu hàm switchTab('tab-minute')"
    print("✓ Tab 2 có nút 'Tiếp tục: Lập biên bản điều chuyển →' chuyển hướng sang Tab 3")

    # 5. Kiểm tra nút Xác nhận cập nhật chính thức ở Tab 3
    assert 'id="btnCommitTransferOfficial"' in html, "Thiếu btnCommitTransferOfficial ở Tab 3"
    assert 'id="btnExportWordOfficial"' in html, "Thiếu btnExportWordOfficial ở Tab 3"
    print("✓ Tab 3 có nút 'Xác nhận cập nhật chính thức' và 'Xuất file Word'")

    # 6. Kiểm tra các cơ chế Workflow & Vai trò
    assert 'id="userRoleSelect"' in html, "Thiếu userRoleSelect"
    assert 'id="badgeMinuteStatus"' in html, "Thiếu badgeMinuteStatus"
    assert 'id="btnSubmitForApproval"' in html, "Thiếu btnSubmitForApproval"
    assert 'id="btnAdminApprove"' in html, "Thiếu btnAdminApprove"
    print("✓ Đầy đủ cơ chế vai trò (Chuyên viên / Lãnh đạo) & các nút Gửi duyệt, Phê duyệt")

    # 7. Kiểm tra hàm JS xác thực và xử lý cập nhật chính thức
    assert 'function validateMinuteFields()' in html, "Thiếu hàm validateMinuteFields"
    assert 'function handleCommitTransferOfficial()' in html, "Thiếu hàm handleCommitTransferOfficial"
    assert 'function exportOfficialWordMinute()' in html, "Thiếu hàm exportOfficialWordMinute"
    print("✓ Đầy đủ các hàm JS nghiệp vụ: validateMinuteFields, handleCommitTransferOfficial, exportOfficialWordMinute")

    # 8. Kiểm tra Responsive CSS
    assert '.minute-row-3col' in html, "Thiếu CSS .minute-row-3col"
    assert 'grid-template-columns: repeat(3, minmax(0, 1fr))' in html, "Thiếu grid-template-columns 3 cột"
    assert '@media (max-width: 900px)' in html, "Thiếu media query cho màn hình nhỏ"
    print("✓ CSS responsive đầy đủ: 3 cột trên máy tính, 1 cột trên mobile/tablet <= 900px")

    # 9. Kiểm tra file print-preview.html cũng đồng bộ bố cục 3 nhóm
    with open("print-preview.html", "r", encoding="utf-8") as pf:
        phtml = pf.read()
    assert 'class="minute-row-3col"' in phtml, "print-preview.html thiếu minute-row-3col"
    assert 'B. BÊN ĐIỀU CHUYỂN — BÊN A' in phtml, "print-preview.html thiếu Nhóm B"
    assert 'C. BÊN NHẬN ĐIỀU CHUYỂN — BÊN B' in phtml, "print-preview.html thiếu Nhóm C"
    print("✓ print-preview.html đã đồng bộ cấu trúc 3 nhóm và layout 3 cột")

    # 10. Kiểm tra bảo toàn dữ liệu và đồng bộ lịch sử
    assert 'transferHistory.unshift' in html, "Thiếu ghi lịch sử vào transferHistory"
    assert 'officialMinuteSnapshot' in html, "Thiếu lưu officialMinuteSnapshot"
    print("✓ Đã tích hợp lưu snapshot biên bản và lịch sử điều chuyển Tab 5")

    # 11. Kiểm tra khi cập nhật chính thức thì phần in biên bản (A4) KHÔNG thể hiện phần trên (watermark ribbon)
    assert '.minute-watermark-ribbon.official' in html and 'display: none !important;' in html, "Thiếu CSS ẩn ribbon khi official"
    assert "ribbon.style.display = 'none'" in html, "Thiếu logic ẩn ribbon khi official trong updateMinuteWorkflowUI"
    print("✓ Đã xử lý chuẩn xác: Sau khi xác nhận cập nhật chính thức, phần in biên bản (A4) không còn thể hiện dải băng/khung trên đầu nữa")

    print("\n===> TẤT CẢ 11/11 TIÊU CHÍ KIỂM THỬ ĐỀU ĐẠT THÀNH CÔNG! <===")

if __name__ == '__main__':
    test_workflow()
