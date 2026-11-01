import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
import os

os.makedirs('test_files', exist_ok=True)

headers_19 = [
    'STT',
    'Mã tài sản',
    'Tên tài sản',
    'SL',
    'Quy cách',
    'Nguyên giá',
    'Số tháng PB',
    'Số tháng PB còn lại',
    'Phân bổ luỹ kế',
    'Giá trị còn lại',
    'Bộ phận quản lý',
    'Bộ phận quản lý tạm thời',
    'Bộ phận quản lý NEW',
    'Bộ phận quản lý tạm thời NEW',
    'Loại công cụ',
    'Ngày hạch toán',
    'Tình trạng tài sản',
    'Tài sản thay thế',
    'Kiến nghị'
]

# 1. File chuẩn 19 cột đúng thứ tự
wb1 = openpyxl.Workbook()
ws1 = wb1.active
ws1.title = "DanhMuc19Cot"
ws1.append(headers_19)
rows_1 = [
    ['1', '00109201', 'Máy vi tính xách tay Dell Latitude 5430', '1', 'i7-1265U / 16GB / 512GB', '25,500,000', '36', '14', '15,583,333', '9,916,667', 'Khối CNTT & Chuyển đổi số', '', '', '', 'Thiết bị tin học', '15/01/2023', 'Bình thường', '', 'Kèm sạc Zin 65W'],
    ['2', '00109315', 'Màn hình Dell UltraSharp U2422H', '2', '24 inch IPS Type-C', '13,600,000', '36', '20', '6,044,444', '7,555,556', 'Phòng Kế toán & Tài chính', '', '', '', 'Thiết bị ngoại vi', '10/05/2023', 'Đang sử dụng', '', 'Mới 98%'],
    ['3', '00109404', 'Máy đếm tiền Glory GFS-120', '1', 'Chống tiền giả CIS', '32,000,000', '60', '28', '17,066,667', '14,933,333', 'Phòng Giao dịch Bến Thành', 'Chi nhánh Chợ Lớn', '', '', 'Thiết bị ngân quỹ', '01/03/2022', 'Bình thường', '', 'Kiểm định định kỳ']
]
for r in rows_1:
    ws1.append(r)
# Set cell format of Col B to text
for row in ws1.iter_rows(min_row=2, min_col=2, max_col=2):
    for cell in row:
        cell.number_format = '@'
wb1.save('test_files/1_Chuan_19_Cot.xlsx')

# 2. File 19 cột bị đảo lộn thứ tự cột
shuffled_headers = [
    'Mã tài sản', 'Bộ phận quản lý NEW', 'Tên tài sản', 'STT', 'SL', 'Nguyên giá',
    'Bộ phận quản lý', 'Quy cách', 'Số tháng PB còn lại', 'Số tháng PB',
    'Giá trị còn lại', 'Phân bổ luỹ kế', 'Bộ phận quản lý tạm thời',
    'Bộ phận quản lý tạm thời NEW', 'Ngày hạch toán', 'Loại công cụ',
    'Tình trạng tài sản', 'Kiến nghị', 'Tài sản thay thế'
]
wb2 = openpyxl.Workbook()
ws2 = wb2.active
ws2.title = "DaoThuTu"
ws2.append(shuffled_headers)
ws2.append([
    '00109201', 'Khối Vận hành', 'Máy vi tính Dell Latitude 5430', '1', '1', '25500000',
    'Khối CNTT', 'Core i7', '14', '36', '9916667', '15583333', '',
    '', '15/01/2023', 'Tin học', 'Bình thường', 'Bàn giao kèm sạc', ''
])
for row in ws2.iter_rows(min_row=2, min_col=1, max_col=1):
    for cell in row:
        cell.number_format = '@'
wb2.save('test_files/2_Dao_Thu_Tu_Cot.xlsx')

# 3. File thiếu cột tùy chọn (Thiếu 'Tài sản thay thế' và 'Kiến nghị')
missing_headers = [h for h in headers_19 if h not in ['Tài sản thay thế', 'Kiến nghị']]
wb3 = openpyxl.Workbook()
ws3 = wb3.active
ws3.append(missing_headers)
ws3.append(['1', '00109520', 'Máy quét Canon DR-C225W', '1', 'Quét 2 mặt Wi-Fi', '11500000', '36', '18', '5750000', '5750000', 'Khối Nhân sự', '', '', '', 'Thiết bị văn phòng', '20/04/2023', 'Bình thường'])
for row in ws3.iter_rows(min_row=2, min_col=2, max_col=2):
    for cell in row:
        cell.number_format = '@'
wb3.save('test_files/3_Thieu_Cot_Tuy_Chon.xlsx')

# 4. File có cột lạ không thuộc 19 chuẩn
extra_headers = headers_19[:5] + ['Mã vạch Barcode', 'Người đang giữ thiết bị'] + headers_19[5:]
wb4 = openpyxl.Workbook()
ws4 = wb4.active
ws4.append(extra_headers)
ws4.append([
    '1', '00109611', 'Máy chủ Dell PowerEdge R650xs', '1', 'Xeon 64GB',
    'BC-998877', 'Nguyễn Văn Kỹ Thuật',
    '128000000', '60', '38', '46933333', '81066667', 'Trung tâm DC', '', '', '', 'Máy chủ', '05/01/2023', 'Đang sử dụng', '', 'Server 1U'
])
for row in ws4.iter_rows(min_row=2, min_col=2, max_col=2):
    for cell in row:
        cell.number_format = '@'
wb4.save('test_files/4_Co_Cot_La.xlsx')

# 5. File có mã tài sản trùng lặp
wb5 = openpyxl.Workbook()
ws5 = wb5.active
ws5.append(headers_19)
ws5.append(['1', '00109201', 'Laptop Dell (Bản ghi 1)', '1', 'i7', '25500000', '36', '14', '15583333', '9916667', 'Khối CNTT', '', '', '', 'Tin học', '15/01/2023', 'Bình thường', '', ''])
ws5.append(['2', '00109201', 'Laptop Dell (Bản ghi 2 - trùng mã)', '1', 'i7', '25500000', '36', '14', '15583333', '9916667', 'Khối CNTT', '', '', '', 'Tin học', '15/01/2023', 'Bình thường', '', ''])
ws5.append(['3', '00109903', 'Ghế xoay giám đốc', '2', 'Da thật', '14200000', '36', '22', '5522222', '8677778', 'Ban TGĐ', '', '', '', 'Nội thất', '15/09/2023', 'Bình thường', '', ''])
for row in ws5.iter_rows(min_row=2, min_col=2, max_col=2):
    for cell in row:
        cell.number_format = '@'
wb5.save('test_files/5_Ma_Trung_Lap.xlsx')

print("All 5 test files created successfully in test_files/")
