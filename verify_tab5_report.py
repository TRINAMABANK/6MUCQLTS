import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("==================================================")
print("KIỂM THỬ TOÀN DIỆN TAB 5: BÁO CÁO SỰ ĐIỀU CHUYỂN")
print("==================================================")

tests = [
    # 1. Tên chính xác và điều hướng Sidebar
    ("Tab 5 có tên chính xác: 5. Báo cáo sự điều chuyển",
     '5. Báo cáo sự điều chuyển' in html and 'data-tab-target="tab-report"' in html),

    ("Tab pane id là pane-tab-report",
     'id="pane-tab-report"' in html),

    ("Tab metadata có đúng tiêu đề và mô tả",
     "'tab-report': {" in html and "title: '5. BÁO CÁO SỰ ĐIỀU CHUYỂN'" in html),

    # 2. Bố cục Khu vực A: Bộ lọc và tra cứu
    ("Bộ lọc có Mã tài sản (rptFilterAssetCode)", 'id="rptFilterAssetCode"' in html),
    ("Bộ lọc có Bộ phận quản lý cũ (rptFilterOldDept)", 'id="rptFilterOldDept"' in html),
    ("Bộ lọc có Bộ phận quản lý mới (rptFilterNewDept)", 'id="rptFilterNewDept"' in html),
    ("Bộ lọc có Từ ngày - Đến ngày", 'id="rptFilterStartDate"' in html and 'id="rptFilterEndDate"' in html),
    ("Bộ lọc có Nhân viên thực hiện", 'id="rptFilterCreator"' in html),
    ("Bộ lọc có Trạng thái (Đang làm, Chờ duyệt, Đã duyệt, Từ chối, Đã hoàn tất)",
     '<option value="Đang làm">' in html and
     '<option value="Chờ duyệt">' in html and
     '<option value="Đã duyệt">' in html and
     '<option value="Từ chối/Yêu cầu chỉnh sửa">' in html and
     '<option value="Đã hoàn tất">' in html),
    ("Nút Tìm kiếm (btnRptSearch) và Xóa bộ lọc (btnRptReset)",
     'id="btnRptSearch"' in html and 'id="btnRptReset"' in html),

    # 3. Ba phạm vi báo cáo
    ("Phạm vi: Một mã tài sản (btnScopeAsset)", 'id="btnScopeAsset"' in html),
    ("Phạm vi: Một phòng ban (btnScopeDept)", 'id="btnScopeDept"' in html),
    ("Phạm vi: Tất cả phòng ban (btnScopeAll)", 'id="btnScopeAll"' in html),

    # 4. Chức năng 1: Tra cứu theo mã tài sản
    ("Hiển thị Mã tài sản & Tên tài sản", 'id="rptAssetCodeDisplay"' in html and 'id="rptAssetNameDisplay"' in html),
    ("Hiển thị Số lần điều chuyển đã thực hiện", 'id="rptAssetTransferCount"' in html),
    ("Hiển thị Bộ phận quản lý hiện tại", 'id="rptAssetCurrentDept"' in html),
    ("Hiển thị Ngày điều chuyển gần nhất", 'id="rptAssetLatestDate"' in html),
    ("Hiển thị Trạng thái điều chuyển gần nhất", 'id="rptAssetLatestStatus"' in html),
    ("Bảng lịch sử 11 cột chuẩn",
     'th style="width: 48px; text-align: center;">STT</th>' in html and
     'Ngày điều chuyển' in html and
     'Mã phiếu' in html and
     'Bộ phận quản lý cũ' in html and
     'Bộ phận quản lý mới' in html and
     'Bộ phận quản lý tạm thời cũ' in html and
     'Bộ phận quản lý tạm thời mới' in html and
     'Nhân viên thực hiện' in html and
     'Người duyệt' in html and
     'Trạng thái' in html and
     'Ghi chú' in html),
    ("Xuất báo cáo Word theo mã tài sản (exportWordAssetReport)",
     'exportWordAssetReport' in html and 'Bao_cao_lich_su_dieu_chuyen_' in html),

    # 5. Chức năng 2: Báo cáo theo phòng ban
    ("Chỉ tiêu: Tên phòng ban", 'id="kpiDeptName"' in html),
    ("Chỉ tiêu: Số mã TS và Tổng SL chuyển đi", 'id="kpiDeptOutCodes"' in html and 'id="kpiDeptOutQty"' in html),
    ("Chỉ tiêu: Số mã TS và Tổng SL chuyển đến", 'id="kpiDeptInCodes"' in html and 'id="kpiDeptInQty"' in html),
    ("Chỉ tiêu: Số phiếu liên quan", 'id="kpiDeptTickets"' in html),
    ("Chỉ tiêu: Phiếu đã duyệt / Hoàn tất", 'id="kpiDeptApproved"' in html),
    ("Chỉ tiêu: Phiếu chờ duyệt", 'id="kpiDeptPending"' in html),
    ("Chỉ tiêu: Phiếu đang làm", 'id="kpiDeptDraft"' in html),
    ("Chỉ tiêu: Phiếu bị từ chối/yêu cầu sửa", 'id="kpiDeptRejected"' in html),
    ("Chỉ tiêu: Tài sản hiện đang quản lý", 'id="kpiDeptCurrentAssets"' in html),
    ("Bảng chi tiết diễn biến phòng ban (tblDeptDetail)", 'id="tblDeptDetail"' in html),

    # 6. Chức năng 3: Báo cáo tất cả phòng ban
    ("Thẻ tổng quan toàn hệ thống (mã TS, tổng SL, số phiếu, số lần ĐC hợp lệ...)",
     'id="kpiAllUniqueCodes"' in html and
     'id="kpiAllTotalQty"' in html and
     'id="kpiAllTotalTickets"' in html and
     'id="kpiAllValidTransfers"' in html),
    ("Bảng tổng hợp theo phòng ban (tblSummaryByDept)", 'id="tblSummaryByDept"' in html),
    ("Cho phép bấm vào từng phòng ban để xem chi tiết", 'selectDeptFromSummary' in html),
    ("Bảng chi tiết toàn bộ diễn biến điều chuyển (tblAllDetail)", 'id="tblAllDetail"' in html),

    # 7. Nguyên tắc tính số liệu
    ("Quy tắc đếm số lần: chỉ tính Đã duyệt hoặc Đã hoàn tất",
     "e.status === 'Đã duyệt' || e.status === 'Đã hoàn tất'" in html),
    ("Không tính phiếu nháp (Đang làm), chờ duyệt, từ chối vào số lần đã thực hiện",
     "validCompleted = assetEvents.filter" in html),
    ("Phân biệt điều chuyển đi và điều chuyển đến",
     "e.oldDept === targetDept" in html and "e.newDept === targetDept" in html),
    ("Phân biệt quản lý chính thức và quản lý tạm thời",
     "oldTempDept" in html and "newTempDept" in html),

    # 8. Xuất báo cáo và tương tác
    ("Xuất Excel đầy đủ dữ liệu (exportExcelReport)", 'exportExcelReport' in html),
    ("In báo cáo (btnRptPrint)", 'id="btnRptPrint"' in html),
    ("Làm mới dữ liệu (btnRptRefresh)", 'id="btnRptRefresh"' in html),
    ("Modal lập phiếu điều chuyển mới (modalNewTicket)", 'id="modalNewTicket"' in html),
    ("Tích hợp Tab 2 khi Commit chuyển dữ liệu vào Tab 5",
     "addTransferHistoryRecord" in html and "ticketCode" in html),
    ("Bảo toàn Times New Roman cho báo cáo xuất Word",
     "Times New Roman" in html and "BÁO CÁO LỊCH SỬ ĐIỀU CHUYỂN TÀI SẢN" in html),
]

all_passed = True
for name, passed in tests:
    status = "[PASS]" if passed else "[FAIL]"
    print(f"{status} {name}")
    if not passed:
        all_passed = False

if all_passed:
    print("\n>>> TẤT CẢ CÁC TIÊU CHÍ NGHIỆM THU TAB 5 ĐẠT 100%! <<<")
else:
    print("\n>>> CÓ LỖI: MỘT SỐ TIÊU CHÍ CHƯA ĐẠT! <<<")
    sys.exit(1)
