import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def test_file_contains(filepath, requirements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n==========================================")
    print(f"VERIFYING FILE: {filepath}")
    print(f"==========================================")

    all_passed = True
    for desc, expected in requirements:
        if isinstance(expected, str):
            found = expected in content
        else:
            found = bool(expected.search(content))
        
        status = "[PASS]" if found else "[FAIL]"
        print(f"{status} {desc}")
        if not found:
            all_passed = False

    return all_passed

nab_requirements_index = [
    ("NAB Bank Logo Image", '<img src="logo-namabank.png" alt="NAM A BANK" class="nab-logo-img">'),
    ("NAB Bank Title", "NAM A BANK"),
    ("NAB Hoi So", "NAM A BANK – HỘI SỞ"),
    ("NAB Address", "201-203 Cách Mạng Tháng Tám, Phường Bàn Cờ, TP. HCM"),
    ("NAB Phone/Fax", "08 3929 6699 - "),
    ("NAB Hotline/Web", "1900 6679 - "),
    ("National Motto", "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM"),
    ("National Motto on 1 Line (white-space: nowrap)", "white-space: nowrap;"),
    ("Independence/Freedom", "Độc lập – Tự do – Hạnh phúc"),
    ("Doc Title Exact", "BIÊN BẢN ĐIỀU CHUYỂN TÀI SẢN CỐ ĐỊNH/ CÔNG CỤ LAO ĐỘNG"),
    ("Section I Title", "I. THÀNH PHẦN THAM DỰ"),
    ("Section I Intro", "Chúng tôi gồm có :"),
    ("Party 1 Exact", "1. BÊN ĐIỀU CHUYỂN TSCĐ/ CCLĐ :"),
    ("Party 2 Exact", "2. BÊN NHẬN ĐIỀU CHUYỂN TSCĐ/ CCLĐ :"),
    ("Section II Title", "II. NỘI DUNG"),
    ("Section II Intro", "Các bên cùng tiến hành điều chuyển TSCĐ/ CCLĐ với nội dung chi tiết như sau :"),
    ("6 Columns Table Header (STT, Mã, Tên, SL, Tình trạng, Ghi chú)", re.compile(r'<th[^>]*>STT</th>.*<th[^>]*>Mã tài sản</th>.*<th[^>]*>Tên tài sản</th>.*<th[^>]*>SL</th>.*<th[^>]*>Tình trạng</th>.*<th[^>]*>Ghi chú</th>', re.DOTALL)),
    ("Closing clause 1", "số TSCĐ/ CCLĐ trên sẽ do Bên nhận điều chuyển chịu trách nhiệm quản lý, sử dụng."),
    ("Closing clause 2", "Biên bản này được lập thành 02 (hai) bản, mỗi bên giữ một bản có giá trị như nhau. /."),
    ("Signature Sender Rep", "BÊN ĐIỀU CHUYỂN"),
    ("Signature Receiver Rep", "BÊN NHẬN ĐIỀU CHUYỂN"),
    ("Signature Admin Approval", "XÁC NHẬN CỦA PHÒNG HCQT"),
    ("Form code in footer", "Biểu mẫu: BM-HCQT.ĐCTS.02"),
    ("Input docDateInput", 'id="docDateInput"'),
    ("Input docEffectiveDateInput", 'id="docEffectiveDateInput"'),
    ("Input docLocationInput", 'id="docLocationInput"'),
    ("Input senderNameInput", 'id="senderNameInput"'),
    ("Input senderRoleInput", 'id="senderRoleInput"'),
    ("Input senderDeptInput", 'id="senderDeptInput"'),
    ("Input receiverNameInput", 'id="receiverNameInput"'),
    ("Input receiverRoleInput", 'id="receiverRoleInput"'),
    ("Input receiverDeptInput", 'id="receiverDeptInput"'),
    ("Multi source dept warning banner", 'id="multiSourceDeptWarning"'),
    ("Auto department population logic", 'autoPopulateDepts'),
]

nab_requirements_preview = [
    ("NAB Bank Logo Image", '<img src="logo-namabank.png" alt="NAM A BANK" class="nab-logo-img">'),
    ("NAB Bank Title", "NAM A BANK"),
    ("NAB Hoi So", "NAM A BANK – HỘI SỞ"),
    ("NAB Address", "201-203 Cách Mạng Tháng Tám, Phường Bàn Cờ, TP. HCM"),
    ("NAB Phone/Fax", "08 3929 6699 - "),
    ("NAB Hotline/Web", "1900 6679 - "),
    ("National Motto", "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM"),
    ("National Motto on 1 Line (white-space: nowrap)", "white-space: nowrap;"),
    ("Independence/Freedom", "Độc lập – Tự do – Hạnh phúc"),
    ("Doc Title Exact", "BIÊN BẢN ĐIỀU CHUYỂN TÀI SẢN CỐ ĐỊNH/ CÔNG CỤ LAO ĐỘNG"),
    ("Section I Title", "I. THÀNH PHẦN THAM DỰ"),
    ("Section I Intro", "Chúng tôi gồm có :"),
    ("Party 1 Exact", "1. BÊN ĐIỀU CHUYỂN TSCĐ/ CCLĐ :"),
    ("Party 2 Exact", "2. BÊN NHẬN ĐIỀU CHUYỂN TSCĐ/ CCLĐ :"),
    ("Section II Title", "II. NỘI DUNG"),
    ("Section II Intro", "Các bên cùng tiến hành điều chuyển TSCĐ/ CCLĐ với nội dung chi tiết như sau :"),
    ("6 Columns Table Header (STT, Mã, Tên, SL, Tình trạng, Ghi chú)", re.compile(r'<th[^>]*>STT</th>.*<th[^>]*>Mã tài sản</th>.*<th[^>]*>Tên tài sản</th>.*<th[^>]*>SL</th>.*<th[^>]*>Tình trạng</th>.*<th[^>]*>Ghi chú</th>', re.DOTALL)),
    ("Closing clause 1", "số TSCĐ/ CCLĐ trên sẽ do Bên nhận điều chuyển chịu trách nhiệm quản lý, sử dụng."),
    ("Closing clause 2", "Biên bản này được lập thành 02 (hai) bản, mỗi bên giữ một bản có giá trị như nhau. /."),
    ("Signature Sender Rep", "BÊN ĐIỀU CHUYỂN"),
    ("Signature Receiver Rep", "BÊN NHẬN ĐIỀU CHUYỂN"),
    ("Signature Admin Approval", "XÁC NHẬN CỦA PHÒNG HCQT"),
    ("Form code in footer", "Biểu mẫu: BM-HCQT.ĐCTS.02"),
    ("Live binding inputs", "renderDocument"),
]

ok1 = test_file_contains('index.html', nab_requirements_index)
ok2 = test_file_contains('print-preview.html', nab_requirements_preview)

if ok1 and ok2:
    print("\n>>> ALL NAM A BANK TRANSFER MINUTES TEMPLATE CHECKS PASSED 100%! <<<")
else:
    print("\n>>> ERROR: SOME TEMPLATE CHECKS FAILED! <<<")
    sys.exit(1)
