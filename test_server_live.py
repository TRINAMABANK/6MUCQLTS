import urllib.request

url = 'http://localhost:8080/index.html'
with urllib.request.urlopen(url) as response:
    content = response.read().decode('utf-8')

checks = [
    ('Pagination selector 10 selected', '<option value="10" selected>10</option>'),
    ('Pagination selector 20', '<option value="20">20</option>'),
    ('Pagination selector 50', '<option value="50">50</option>'),
    ('Pagination selector 100', '<option value="100">100</option>'),
    ('Button Trang truoc', 'id="btnPrevPage" title="Về trang trước">Trang trước</button>'),
    ('Button Trang sau', 'id="btnNextPage" title="Sang trang sau">Trang sau</button>'),
    ('Button Chon tat ca cac trang', 'Chọn tất cả các trang'),
    ('Header check select all current page', 'title="Chọn / Bỏ chọn toàn bộ dòng trên trang hiện tại"'),
    ('Default pageSize = 10', 'let pageSize = 10;'),
    ('Display stats continuous format', 'Hiển thị <b>${startNum}–${endNum}</b> trên tổng số <b>${totalItems}</b> tài sản'),
    ('Continuous STT calculation', 'const displayStt = startIndex + idx + 1;'),
]

all_passed = True
for name, snippet in checks:
    if snippet in content:
        print(f"[PASS] {name}")
    else:
        print(f"[FAIL] {name} NOT FOUND!")
        all_passed = False

if all_passed:
    print("\nSUCCESS: All live server checks passed!")
else:
    print("\nFAILURE: Some checks failed!")
