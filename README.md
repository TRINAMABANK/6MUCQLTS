# HỆ THỐNG TRA CỨU & ĐIỀU CHUYỂN TÀI SẢN — TCLOUD SAAS ENTERPRISE (CHUẨN HÓA 19 CỘT DỮ LIỆU)

Phần mềm Quản trị Tra cứu, Điều chuyển Tài sản và Xuất Biên bản Bàn giao A4 chuẩn Doanh nghiệp / Ngân hàng (NAB Enterprise) với kiến trúc **Bố cục 2 Cột Chuyên nghiệp (2-Column Dashboard)** theo phong cách nhận diện **TCloud SaaS (Tím công nghệ & Lavender sáng)**.

---

## 1. DANH SÁCH 19 TRƯỜNG DỮ LIỆU CHUẨN (BẢO TOÀN THỐNG NHẤT 100%)

Hệ thống áp dụng nghiêm ngặt danh sách 19 trường dữ liệu chuẩn theo đúng thứ tự, không tự ý đổi tên, bỏ cột, gộp cột hoặc thay đổi thứ tự:

| STT | Tên trường chuẩn | Kiểu dữ liệu & Đặc tả nghiệp vụ |
|---:|---|---|
| **1** | **STT** | Số thứ tự tăng dần (1, 2, 3...) |
| **2** | **Mã tài sản** | Chuỗi ký tự (Text), **bảo toàn nguyên vẹn số 0 ở đầu** (ví dụ: `00109201`) |
| **3** | **Tên tài sản** | Tên thiết bị, công cụ lao động |
| **4** | **SL** | Số lượng hiện vật |
| **5** | **Quy cách** | Cấu hình kỹ thuật, model, thông số |
| **6** | **Nguyên giá** | Giá trị ban đầu, hỗ trợ phân cách hàng nghìn (VD: `25,500,000`) |
| **7** | **Số tháng PB** | Tổng số tháng phân bổ hao mòn |
| **8** | **Số tháng PB còn lại** | Thời gian phân bổ còn lại |
| **9** | **Phân bổ luỹ kế** | Giá trị đã trích khấu hao/phân bổ lũy kế |
| **10** | **Giá trị còn lại** | Giá trị sổ sách còn lại của tài sản |
| **11** | **Bộ phận quản lý** | Đơn vị / Phòng ban quản lý hiện tại |
| **12** | **Bộ phận quản lý tạm thời** | Đơn vị quản lý tạm thời hiện tại |
| **13** | **Bộ phận quản lý NEW** | Đơn vị tiếp nhận mới sau điều chuyển (Highlight xanh lá) |
| **14** | **Bộ phận quản lý tạm thời NEW**| Đơn vị tạm thời mới sau điều chuyển (Highlight xanh lá) |
| **15** | **Loại công cụ** | Phân nhóm tài sản (Thiết bị tin học, Thiết bị ngoại vi...) |
| **16** | **Ngày hạch toán** | Giữ đúng ngày tháng nguồn (định dạng `DD/MM/YYYY`) |
| **17** | **Tình trạng tài sản** | Tình trạng kỹ thuật (Bình thường, Đang sử dụng, Cần bảo dưỡng...) |
| **18** | **Tài sản thay thế** | Thông tin thiết bị thay thế (nếu có) |
| **19** | **Kiến nghị** | Ghi chú, đề xuất điều chuyển, bàn giao kèm phụ kiện |

---

## 2. QUY TRÌNH NẠP DỮ LIỆU & BẢNG XEM TRƯỚC (SECTION 3 & 4)

1. **Định dạng hỗ trợ**:
   - Tệp Excel `.xlsx`, `.xls` và tệp CSV `.csv`.
   - Khu vực upload thiết kế TCloud viền nét đứt tím nhạt `#E9DDFB`, icon tải lên `#7C2FE8`, nút chọn file gradient tím – hồng.
   - Hỗ trợ chọn file từ máy tính hoặc kéo thả (Drag & Drop).

2. **Cơ chế đọc & ánh xạ thông minh**:
   - Nhận diện cột theo tên cột (có dấu, không dấu, khoảng trắng thừa) và ánh xạ vào đúng 19 trường chuẩn.
   - Không phụ thuộc vào vị trí cột khi các cột trong file nguồn bị đảo lộn.
   - Phát hiện các cột lạ không thuộc 19 chuẩn và cảnh báo cụ thể, bỏ qua an toàn, không âm thầm gán nhầm dữ liệu.
   - Kiểm tra mã tài sản bị trống và loại trừ các dòng lỗi.
   - Phát hiện mã tài sản trùng lặp, thống kê số lần xuất hiện và bảo toàn đầy đủ bản ghi (không tự ý xóa).
   - Không tự ý biến ô trống thành số 0.

3. **Bảng xem trước & Xác nhận nạp dữ liệu**:
   - Hiển thị Thẻ phân tích tệp với 4 chỉ số: `Tổng số dòng đọc`, `Số dòng hợp lệ`, `Số dòng có lỗi`, `Số mã TS trùng lặp`.
   - Bảng xem trước hiển thị 5 dòng đầu tiên với đầy đủ 19 cột chuẩn để đối chiếu.
   - Nút **"Xác nhận nạp dữ liệu vào hệ thống"**: Dữ liệu chỉ được chính thức ghi nhận vào kho sau khi người dùng nhấn nút xác nhận này.

---

## 3. KIẾN TRÚC GIAO DIỆN BỐ CỤC 2 CỘT (2-COLUMN DASHBOARD)

### 🌟 CỘT 1 (Bên trái ~290px) — Bảng điều khiển & Các Tab chức năng:
* **Tab 1**: `1. Tra cứu & Chọn TS` (kèm badge đếm tổng tài sản).
* **Tab 2**: `2. Điều chuyển TS (NEW)` (kèm badge đếm số tài sản đã chọn).
* **Tab 3**: `3. Biên bản bàn giao A4` (lập và xuất biên bản in ấn).
* **Tab 4**: `4. Nhập / Xuất dữ liệu` (upload file, nạp dữ liệu mẫu, tải file mẫu 19 cột).
* **Footer Status**: Chấm xanh xung nhịp `🟢 Hệ thống trực tuyến` cùng tóm tắt số liệu kho.

### 🌟 CỘT 2 (Bên phải) — Thể hiện thông tin & Xử lý dữ liệu tương ứng:
* **Thanh Header động**: Hiển thị tên phân hệ, mô tả chức năng và Dải KPI thống kê nhanh (`Tổng kho`, `Đang lọc`, `Đã chọn`, `Số lượng đơn vị`).
* **Khu vực hiển thị tương ứng**:
  * **Tab 1**: Thanh tra cứu nhanh (mã đầy đủ, 4–6 số cuối, tên, quy cách, ghi chú...), bộ lọc đơn vị/tình trạng, bảng tra cứu đầy đủ 19 cột chuẩn, chức năng **Click tiêu đề cột để sắp xếp (Sort A-Z, 0-9)**, phân trang linh hoạt, nút "Xuất Excel toàn bộ kho (19 cột)".
  * **Tab 2**: Bảng làm việc điều chuyển đầy đủ 19 cột chuẩn, hỗ trợ chỉnh sửa trực tiếp từng dòng (inline edit), công cụ áp dụng hàng loạt (`Bộ phận quản lý NEW`, `Bộ phận quản lý tạm thời NEW`, `Tình trạng bàn giao`), nút "Xuất Excel danh sách điều chuyển (19 cột)", nút "Xác nhận cập nhật chính thức".
  * **Tab 3**: Form cấu hình thông tin Bên giao (Bên A), Bên nhận (Bên B), căn cứ pháp lý, tờ biên bản A4 chuẩn tỷ lệ in ấn, nút In A4, Lưu PDF, Xem trước toàn màn hình, Mở tab riêng.
  * **Tab 4**: Dropzone kéo thả file, thẻ xem trước và phân tích file, tải file mẫu 19 cột, nạp 15 tài sản mẫu chuẩn.

---

## 4. KẾT QUẢ KIỂM THỬ 12 TÌNH HUỐNG NGHIỆM THU

| STT | Tình huống kiểm thử | Kết quả thực tế | Trạng thái |
|:---:|---|---|:---:|
| 1 | Nạp file có đủ 19 cột đúng thứ tự | Nhận diện đủ 19/19 cột chuẩn, hiển thị bảng xem trước chính xác | **ĐẠT** |
| 2 | Nạp file có các cột bị đổi thứ tự | Nhận diện đúng từng cột qua tên trường, không phụ thuộc vị trí cột | **ĐẠT** |
| 3 | Nạp file thiếu cột | Phát hiện cột bắt buộc thiếu (báo lỗi); các cột chuẩn tùy chọn thiếu sẽ để trống mặc định và thông báo | **ĐẠT** |
| 4 | Nạp file có cột lạ | Liệt kê danh sách cột lạ, bỏ qua an toàn và không gán nhầm dữ liệu | **ĐẠT** |
| 5 | Nạp file có mã tài sản trùng | Phát hiện và thống kê danh sách mã trùng lặp, bảo toàn tất cả bản ghi | **ĐẠT** |
| 6 | Nạp file có mã TS bắt đầu bằng số 0 | Đọc `raw: false`, bảo toàn chuỗi `00109201` không bị mất số 0 | **ĐẠT** |
| 7 | Nạp file có ô trống & số có dấu phẩy | Đọc đúng giá trị số phân cách hàng nghìn, không tự ý gán 0 cho ô trống | **ĐẠT** |
| 8 | Nạp file có ngày hạch toán | Giữ đúng định dạng ngày tháng theo nguồn | **ĐẠT** |
| 9 | Tìm kiếm & chọn tài sản sau khi nạp | Tìm theo 4–6 số cuối, lọc bộ phận, tick chọn từng dòng hoặc toàn bộ | **ĐẠT** |
| 10 | Cập nhật 2 trường NEW | Không ghi đè bộ phận cũ khi chưa xác nhận chính thức | **ĐẠT** |
| 11 | Xuất Excel đủ 19 cột | Cả xuất điều chuyển và xuất toàn bộ kho đều tạo file `.xlsx` đủ 19 cột chuẩn, mã TS giữ số 0 | **ĐẠT** |
| 12 | In và lưu PDF | Xem trước toàn màn hình và in A4 chuẩn văn bản hành chính không bị ảnh hưởng | **ĐẠT** |

---

## 5. ĐỊA CHỈ TRUY CẬP LOCALHOST

Máy chủ đang hoạt động tại:
- **Giao diện Dashboard chính**: [http://localhost:8080](http://localhost:8080)
- **Trang in Biên bản A4 độc lập**: [http://localhost:8080/print-preview.html](http://localhost:8080/print-preview.html)

*(Nhấn `Ctrl + F5` hoặc `Cmd + Shift + R` trên trình duyệt để xóa cache và tải bản cập nhật mới nhất).*
