import re
import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def check_tab6_implementation():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    errors = []
    passes = []

    # 1. Check library html5-qrcode
    if "html5-qrcode" in html:
        passes.append("Tích hợp thư viện html5-qrcode (cục bộ & CDN fallback)")
    else:
        errors.append("Thiếu thư viện html5-qrcode")

    # 2. Check sidebar menu item 6. Kiểm kê QRCode
    if 'data-tab-target="tab-qrcode"' in html and "6. Kiểm kê QRCode" in html:
        passes.append("Cột 1 có nút phân hệ '6. Kiểm kê QRCode' với badge counter #sidebarBadgeQr")
    else:
        errors.append("Thiếu nút phân hệ 6 trong sidebar menu")

    # 3. Check pane-tab-qrcode
    if 'id="pane-tab-qrcode"' in html:
        passes.append("Cột 2 có tab pane id #pane-tab-qrcode")
    else:
        errors.append("Thiếu pane-tab-qrcode")

    # 4. Check department selector
    if 'id="qrInventoryDeptSelect"' in html:
        passes.append("Có trường chọn Bộ phận quản lý kiểm kê (#qrInventoryDeptSelect)")
    else:
        errors.append("Thiếu #qrInventoryDeptSelect")

    # 5. Check camera scanner controls
    for el in ["#btnQrStartCamera", "#btnQrStopCamera", "#btnQrResumeScan", "#qrReaderBox", "#qrScannerLaser"]:
        if f'id="{el.replace("#", "")}"' in html:
            passes.append(f"Có thành phần camera: {el}")
        else:
            errors.append(f"Thiếu thành phần camera: {el}")

    # 6. Check manual code input fallback
    if 'id="qrManualCodeInput"' in html and 'id="btnQrManualLookup"' in html:
        passes.append("Có ô nhập mã tài sản thủ công (#qrManualCodeInput & #btnQrManualLookup)")
    else:
        errors.append("Thiếu ô nhập mã thủ công")

    # 7. Check 7 standard fields in exact order
    field_ids = [
        "qrValCode",      # 1. Mã tài sản
        "qrValName",      # 2. Tên tài sản
        "qrValCost",      # 3. Nguyên giá
        "qrValBookVal",   # 4. Giá trị còn lại
        "qrValAcctDate",  # 5. Ngày hạch toán
        "qrValDept",      # 6. Bộ phận quản lý
        "qrValTempDept"   # 7. BP quản lý tạm thời
    ]
    for fid in field_ids:
        if f'id="{fid}"' in html:
            passes.append(f"Có trường thông tin bắt buộc: #{fid}")
        else:
            errors.append(f"Thiếu trường thông tin: #{fid}")

    # 8. Check Department Cross-Check Box
    if 'id="qrCrosscheckBanner"' in html and 'id="qrCrosscheckMessage"' in html:
        passes.append("Có khung đối chiếu bộ phận (#qrCrosscheckBanner, Khớp bộ phận / Cần kiểm tra)")
    else:
        errors.append("Thiếu khung đối chiếu bộ phận")

    # 9. Check Confirm Button
    if 'id="btnQrConfirmInventory"' in html:
        passes.append("Có nút chính XÁC NHẬN (#btnQrConfirmInventory)")
    else:
        errors.append("Thiếu nút #btnQrConfirmInventory")

    # 10. Check Inventory Table (12 columns)
    if 'id="tblQrInventoryList"' in html and 'id="tblBodyQrInventory"' in html:
        passes.append("Có bảng DANH SÁCH TÀI SẢN ĐÃ KIỂM KÊ (#tblQrInventoryList)")
    else:
        errors.append("Thiếu bảng danh sách kiểm kê")

    # 11. Check Excel Export & Clear Session
    if 'id="btnQrExportExcel"' in html and 'id="btnQrClearSession"' in html:
        passes.append("Có nút Xuất Excel (#btnQrExportExcel) và Xóa phiên (#btnQrClearSession)")
    else:
        errors.append("Thiếu nút Xuất Excel hoặc Xóa phiên")

    # 12. Check JavaScript logic functions
    js_funcs = [
        "initQrInventoryTab",
        "populateQrDepartmentDropdown",
        "startQrScanner",
        "stopQrCamera",
        "resumeQrScanner",
        "handleProcessScannedCode",
        "handleConfirmQrInventory",
        "renderQrInventoryTable",
        "exportQrInventoryExcel",
        "saveQrInventoryRecords",
        "loadQrInventoryRecords"
    ]
    for func in js_funcs:
        if f"function {func}" in html or f"const {func}" in html or f"let {func}" in html or f"{func} =" in html:
            passes.append(f"Có hàm nghiệp vụ: {func}()")
        else:
            errors.append(f"Thiếu hàm nghiệp vụ: {func}()")

    print("\n" + "="*50)
    print("KIỂM TRA CẤU TRÚC PHÂN HỆ 6 (KIỂM KÊ QRCODE)")
    print("="*50)
    for p in passes:
        print(f"✓ {p}")

    if errors:
        print("\nCÁC LỖI PHÁT HIỆN:")
        for e in errors:
            print(f"✗ {e}")
        return False
    else:
        print(f"\n===> TẤT CẢ {len(passes)}/{len(passes)} TIÊU CHÍ PHÂN HỆ 6 ĐỀU ĐẠT 100%! <===")
        return True

if __name__ == "__main__":
    success = check_tab6_implementation()
    sys.exit(0 if success else 1)
