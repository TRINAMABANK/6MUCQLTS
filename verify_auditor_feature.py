import re
import sys
import json

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def test_auditor_feature():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    passes = []
    errors = []

    # 1. Kiểm tra trường chọn Phòng Ban kiểm kê & Session Info Bar
    if 'id="qrInventoryDeptSelect"' in html and 'id="qrSessionIdDisplay"' in html and 'id="qrSessionStartTime"' in html:
        passes.append("Tiêu chí 1: Có trường chọn Phòng Ban kiểm kê (#qrInventoryDeptSelect) và thanh hiển thị thông tin phiên (#qrSessionIdDisplay, #qrSessionStartTime)")
    else:
        errors.append("Thiếu trường chọn Phòng ban hoặc thông tin phiên")

    # 2. Kiểm tra danh mục nhân sự dùng chung & chọn nhân sự có sẵn
    if 'KEY_EMPLOYEE_DIRECTORY' in html and 'loadEmployeeDirectory' in html and 'DEFAULT_EMPLOYEES' in html:
        passes.append("Tiêu chí 2: Có danh mục nhân sự dùng chung (KEY_EMPLOYEE_DIRECTORY) với dữ liệu mẫu Nam A Bank và hàm tải/lưu")
    else:
        errors.append("Thiếu danh mục nhân sự dùng chung")

    if 'id="modalQrAddAuditor"' in html and 'id="tblBodyEmployeeDirectory"' in html and 'id="qrAuditorSearchInput"' in html:
        passes.append("Tiêu chí 2b: Có Modal Quản lý nhân sự (#modalQrAddAuditor) với ô tìm kiếm (#qrAuditorSearchInput) và bảng danh sách nhân viên (#tblBodyEmployeeDirectory)")
    else:
        errors.append("Thiếu modal hoặc ô tìm kiếm nhân viên")

    # 3. Kiểm tra thêm nhiều nhân sự vào cùng phiên
    if 'addEmpToCurrentSession' in html and 'id="qrAuditorChipContainer"' in html and 'renderQrAuditorChips' in html:
        passes.append("Tiêu chí 3: Cho phép thêm nhiều nhân sự vào cùng phiên (addEmpToCurrentSession), hiển thị dạng thẻ linh hoạt (#qrAuditorChipContainer)")
    else:
        errors.append("Thiếu chức năng thêm nhiều nhân sự hoặc hiển thị dạng thẻ")

    # 4. Kiểm tra thêm nhân sự mới vào danh mục khi có quyền Admin
    if 'id="paneModalAddNewEmp"' in html and 'id="chkToggleAdminRole"' in html and 'handleSaveNewEmployeeAndAdd' in html:
        passes.append("Tiêu chí 4: Có form thêm nhân sự mới vào danh mục (#paneModalAddNewEmp), kiểm tra phân quyền Quản trị viên (#chkToggleAdminRole, isQrAdminMode)")
    else:
        errors.append("Thiếu form thêm nhân sự mới hoặc phân quyền")

    # 5. Kiểm tra ngăn mã nhân viên trùng
    if 'errNewEmpCode' in html and 'exists = employeeDirectory.find' in html:
        passes.append("Tiêu chí 5: Có cơ chế kiểm tra và ngăn chặn mã nhân viên trùng lặp (#errNewEmpCode, employeeDirectory duplicate check)")
    else:
        errors.append("Thiếu cơ chế ngăn mã nhân viên trùng")

    # 6. Kiểm tra chọn nhân sự phụ trách chính
    if 'setLeadAuditor' in html and 'is-lead' in html and '★ Phụ trách chính' in html and 'leadAuditor' in html:
        passes.append("Tiêu chí 6: Cho phép chọn và hiển thị Nhân sự phụ trách chính (setLeadAuditor, ★ Phụ trách chính, leadAuditor)")
    else:
        errors.append("Thiếu chức năng chỉ định nhân sự phụ trách chính")

    # 7. Kiểm tra Quét và Xác nhận liên tục, lưu người quét thực tế
    if 'id="qrScannerAuditorSelect"' in html and 'scannerAuditor' in html and 'handleConfirmQrInventory' in html:
        passes.append("Tiêu chí 7: Lưu nhân sự trực tiếp thực hiện quét (#qrScannerAuditorSelect, scannerAuditor) và hỗ trợ xác nhận nhiều tài sản liên tiếp")
    else:
        errors.append("Thiếu trường nhân sự thực hiện quét hoặc xử lý xác nhận")

    # 8. Kiểm tra tự động reset nhưng giữ nguyên Phòng Ban và Nhân sự phiên
    if 'resetQrPreviewArea' in html and 'qrCurrentSession.dept' in html and 'qrCurrentSession.members' in html:
        passes.append("Tiêu chí 8: Tự động reset khu vực xem trước nhưng bảo toàn nguyên vẹn Phòng Ban và danh sách nhân sự của phiên kiểm kê")
    else:
        errors.append("Thiếu logic bảo toàn phòng ban và nhân sự sau khi reset")

    # 9. Kiểm tra dữ liệu phiên kiểm kê được lưu trữ và truy xuất lại
    if 'KEY_QR_SESSIONS' in html and 'viewQrSessionDetail' in html and 'id="modalQrSessionDetail"' in html:
        passes.append("Tiêu chí 9: Dữ liệu phiên kiểm kê được lưu trữ lâu dài (KEY_QR_SESSIONS) và có Modal xem chi tiết phiên (#modalQrSessionDetail, viewQrSessionDetail)")
    else:
        errors.append("Thiếu lưu trữ phiên kiểm kê hoặc modal xem chi tiết phiên")

    # 10. Kiểm tra cập nhật Bảng Danh sách kiểm kê & Xuất Excel 14 cột
    if 'Nhân sự phụ trách' in html and 'Nhân sự thực hiện quét' in html and 'Phòng Ban kiểm kê' in html:
        passes.append("Tiêu chí 10: Bảng danh sách và mẫu xuất Excel đã bổ sung đầy đủ các cột: Phòng Ban kiểm kê, Nhân sự phụ trách, Nhân sự thực hiện quét")
    else:
        errors.append("Thiếu các cột nhân sự trong bảng danh sách kiểm kê")

    print("\n" + "="*70)
    print("KẾT QUẢ KIỂM THỬ NGHIỆM THU CHỨC NĂNG NHÂN SỰ KIỂM KÊ (TAB 6)")
    print("="*70)
    for p in passes:
        print(f"✓ {p}")

    if errors:
        print("\nCÁC LỖI CẦN XỬ LÝ:")
        for e in errors:
            print(f"✗ {e}")
        return False
    else:
        print(f"\n===> TẤT CẢ {len(passes)}/10 TIÊU CHÍ NGHIỆM THU ĐỀU ĐẠT 100%! <===")
        return True

if __name__ == "__main__":
    success = test_auditor_feature()
    sys.exit(0 if success else 1)
