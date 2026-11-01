import openpyxl
import re
import unicodedata
import sys

sys.stdout.reconfigure(encoding='utf-8')

def norm(text):
    if not text:
        return ""
    text = str(text).lower()
    text = unicodedata.normalize('NFD', text)
    text = re.sub(r'[\u0300-\u036f]', '', text)
    text = text.replace('đ', 'd').strip()
    return text

def map_column_header(h):
    h_clean = str(h or "").strip()
    if not h_clean:
        return None
    h_norm = norm(h_clean)

    if re.search(r'^(stt|so thu tu|no\.?|stt\.|#)$', h_norm): return 'stt'
    if re.search(r'^(ma tai san|ma ts|so the|asset code|code|ma)$', h_norm): return 'code'
    if re.search(r'^(ten tai san|ten ts|asset name|ten|noi dung|noi dung tai san)$', h_norm): return 'name'
    if re.search(r'^(sl|so luong|quantity|qty)$', h_norm): return 'qty'
    if re.search(r'^(quy cach|thong so|model|cau hinh|specification)$', h_norm): return 'spec'
    if re.search(r'^(nguyen gia|gia mua|don gia|cost|original cost)$', h_norm): return 'cost'
    if re.search(r'^(so thang pb|thang pb|thoi gian pb|depreciation months)$', h_norm) and not re.search(r'con lai', h_norm): return 'dep_months'
    if re.search(r'^(so thang pb con lai|thang pb con lai|thang con lai|pb con lai|remaining months)$', h_norm): return 'rem_months'
    if re.search(r'^(phan bo luy ke|luy ke pb|luy ke|da phan bo|accumulated depreciation)$', h_norm): return 'acc_dep'
    if re.search(r'^(gia tri con lai|gtcl|book value|remaining value)$', h_norm): return 'book_val'
    if re.search(r'^(bo phan quan ly new|bp quan ly new|bp new|bo phan new|don vi new|bo phan quan ly moi|bp moi|don vi moi)$', h_norm) and not re.search(r'tam', h_norm): return 'new_dept'
    if re.search(r'^(bo phan quan ly tam thoi new|bp tam new|tam thoi new|tam new|tam thoi moi|bp quan ly tam new)$', h_norm): return 'new_temp'
    if re.search(r'^(bo phan quan ly tam thoi|bp quan ly tam|bp tam|tam thoi|bo phan tam)$', h_norm) and not re.search(r'new|moi', h_norm): return 'temp'
    if re.search(r'^(bo phan quan ly|bp quan ly|phong ban|don vi quan ly|don vi)$', h_norm) and not re.search(r'tam|new|moi', h_norm): return 'dept'
    if re.search(r'^(loai cong cu|loai tai san|loai ts|nhom tai san|category|phan loai)$', h_norm): return 'category'
    if re.search(r'^(ngay hach toan|ngay mua|ngay vao so|ngay su dung|accounting date|date)$', h_norm): return 'acct_date'
    if re.search(r'^(tinh trang tai san|tinh trang|trang thai|condition|status)$', h_norm): return 'status'
    if re.search(r'^(tai san thay the|ts thay the|thay the|replacement)$', h_norm): return 'replace_asset'
    if re.search(r'^(kien nghi|ghi chu|note|remark|de xuat)$', h_norm): return 'note'

    return None

test_cases = [
    'test_files/1_Chuan_19_Cot.xlsx',
    'test_files/2_Dao_Thu_Tu_Cot.xlsx',
    'test_files/3_Thieu_Cot_Tuy_Chon.xlsx',
    'test_files/4_Co_Cot_La.xlsx',
    'test_files/5_Ma_Trung_Lap.xlsx'
]

for filepath in test_cases:
    wb = openpyxl.load_workbook(filepath, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    headers = rows[0]
    col_map = {}
    unknown = []
    for idx, h in enumerate(headers):
        k = map_column_header(h)
        if k:
            col_map[k] = idx
        else:
            unknown.append(h)
    
    data_rows = rows[1:]
    code_counts = {}
    codes = []
    for r in data_rows:
        code_val = str(r[col_map['code']]).strip() if 'code' in col_map and r[col_map['code']] is not None else ""
        if code_val:
            codes.append(code_val)
            code_counts[code_val] = code_counts.get(code_val, 0) + 1
            
    duplicates = [c for c, cnt in code_counts.items() if cnt > 1]
    
    print(f"=== File: {filepath} ===")
    print(f" - Matched columns count: {len(col_map)}/19")
    print(f" - Unknown columns: {unknown}")
    print(f" - Rows parsed: {len(data_rows)}")
    print(f" - Duplicates: {duplicates}")
    print(f" - Code sample with leading zero check: {codes[0]} (starts with 0: {codes[0].startswith('0')})")
    assert 'code' in col_map, f"Must find 'code' column in {filepath}"
    assert codes[0] == '00109201' or codes[0] == '00109520' or codes[0] == '00109611', f"Leading zeros must be preserved!"
    print(" -> PASSED\n")

print("ALL 5 AUTOMATED VERIFICATION CHECKS PASSED PERFECTLY!")
