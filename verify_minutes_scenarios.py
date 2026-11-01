import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

def format_date_vietnamese(location, date_str):
    if not date_str:
        loc = location or '....'
        return f"{loc}, ngày ... tháng ... năm 20 ..."
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return f"{location}, ngày {dt.day} tháng {dt.month} năm {dt.year}"

def format_effective_date(date_str):
    if not date_str:
        return "ngày … tháng … năm 20…"
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return f"ngày {dt.day} tháng {dt.month} năm {dt.year}"

def format_representative_field(val, default_dots):
    if val and val.strip():
        return f"<b>{val.strip()}</b>"
    return default_dots

def format_role_field(val, default_dots):
    if val and val.strip():
        return f"<span>{val.strip()}</span>"
    return default_dots

def generate_table_rows(items):
    rows = []
    for idx, item in enumerate(items):
        stt = idx + 1
        code = str(item.get('code', ''))
        name = str(item.get('name', ''))
        qty = str(item.get('qty', '1'))
        status = str(item.get('status', 'Bình thường'))
        note = str(item.get('note', ''))
        rows.append({
            'stt': stt,
            'code': code,
            'name': name,
            'qty': qty,
            'status': status,
            'note': note
        })
    return rows

print("=== SCENARIO 1: Single asset, leading zeros, long name ===")
items_1 = [{
    'code': '00109201',
    'name': 'Máy vi tính xách tay Dell Latitude 5430 Core i7-1265U vPro 16GB RAM 512GB SSD PCIe NVMe Full HD IPS',
    'qty': '1',
    'status': 'Bình thường',
    'note': 'Kèm sạc Zin Type-C 65W và chuột quang không dây Dell'
}]
t_rows = generate_table_rows(items_1)
assert len(t_rows) == 1
assert t_rows[0]['code'] == '00109201', "Leading zero must be strictly preserved"
assert t_rows[0]['stt'] == 1
print(f" -> Code: {t_rows[0]['code']}, Name length: {len(t_rows[0]['name'])}, Status: {t_rows[0]['status']}")
print(" -> Passed Scenario 1!")

print("\n=== SCENARIO 2: Empty representative and role values ===")
s_name = ""
s_role = ""
rendered_name = format_representative_field(s_name, "..............................................................")
rendered_role = format_role_field(s_role, "..........................................")
assert rendered_name == ".............................................................."
assert rendered_role == ".........................................."
print(f" -> Rendered empty rep: {rendered_name}")
print(f" -> Rendered empty role: {rendered_role}")
print(" -> Passed Scenario 2!")

print("\n=== SCENARIO 3: Populated representative and role values ===")
s_name_filled = "Nguyễn Văn Hùng"
s_role_filled = "Trưởng phòng Quản trị Thiết bị"
rendered_name_f = format_representative_field(s_name_filled, "..............................................................")
rendered_role_f = format_role_field(s_role_filled, "..........................................")
assert rendered_name_f == "<b>Nguyễn Văn Hùng</b>"
assert rendered_role_f == "<span>Trưởng phòng Quản trị Thiết bị</span>"
print(f" -> Rendered filled rep: {rendered_name_f}")
print(f" -> Rendered filled role: {rendered_role_f}")
print(" -> Passed Scenario 3!")

print("\n=== SCENARIO 4: Date formatting with location and effective date ===")
d_str = format_date_vietnamese("TP. Hồ Chí Minh", "2026-10-25")
eff_str = format_effective_date("2026-10-28")
assert d_str == "TP. Hồ Chí Minh, ngày 25 tháng 10 năm 2026"
assert eff_str == "ngày 28 tháng 10 năm 2026"

d_empty = format_date_vietnamese("TP. Hồ Chí Minh", "")
eff_empty = format_effective_date("")
assert d_empty == "TP. Hồ Chí Minh, ngày ... tháng ... năm 20 ..."
assert eff_empty == "ngày … tháng … năm 20…"
print(f" -> Date filled: {d_str}")
print(f" -> Effective date filled: {eff_str}")
print(f" -> Date empty: {d_empty}")
print(f" -> Effective date empty: {eff_empty}")
print(" -> Passed Scenario 4!")

print("\n=== SCENARIO 5: Multi-department detection & warning ===")
sample_multi = [
    {'code': '00109201', 'dept': 'Khối CNTT & Chuyển đổi số', 'new_dept': 'Khối Vận hành'},
    {'code': '00109315', 'dept': 'Phòng Kế toán & Tài chính', 'new_dept': 'Khối Vận hành'},
]
source_depts = list(set([x['dept'] for x in sample_multi]))
target_depts = list(set([x['new_dept'] for x in sample_multi]))
assert len(source_depts) == 2
has_warning = len(source_depts) > 1
assert has_warning is True
print(f" -> Source depts detected: {source_depts}")
print(f" -> Multi source warning triggered: {has_warning}")
print(f" -> Target depts detected: {target_depts}")
print(" -> Passed Scenario 5!")

print("\n=== SCENARIO 6: Full 15 items batch ===")
items_15 = [
    {
        'code': f"00109{200+i}",
        'name': f"Tài sản Nam A Bank {i+1}",
        'qty': '1',
        'status': 'Bình thường',
        'note': f"Ghi chú bàn giao {i+1}"
    }
    for i in range(15)
]
t_rows_15 = generate_table_rows(items_15)
assert len(t_rows_15) == 15
assert t_rows_15[0]['code'] == '00109200'
assert t_rows_15[14]['stt'] == 15
assert t_rows_15[14]['code'] == '00109214'
print(f" -> Generated {len(t_rows_15)} table rows with 6 columns successfully!")
print(" -> Passed Scenario 6!")

print("\nALL BUSINESS SCENARIOS VERIFIED SUCCESSFULLY!")
