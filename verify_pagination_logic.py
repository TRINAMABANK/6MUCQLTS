import sys

sys.stdout.reconfigure(encoding='utf-8')

class PaginationModel:
    def __init__(self, data=None, page_size=10):
        self.data = data or []
        self.page_size = page_size
        self.current_page = 1
        self.selected_assets = {}

    def get_total_items(self):
        return len(self.data)

    def get_total_pages(self):
        total = self.get_total_items()
        return max(1, (total + self.page_size - 1) // self.page_size)

    def clamp_page(self):
        total_pages = self.get_total_pages()
        if self.current_page > total_pages:
            self.current_page = total_pages
        if self.current_page < 1:
            self.current_page = 1

    def get_page_items(self):
        self.clamp_page()
        total_items = self.get_total_items()
        start_index = (self.current_page - 1) * self.page_size
        end_index = min(start_index + self.page_size, total_items)
        return self.data[start_index:end_index], start_index, end_index

    def get_stats_text(self):
        total_items = self.get_total_items()
        if total_items == 0:
            return "Hiển thị 0 trên tổng số 0 tài sản"
        _, start_index, end_index = self.get_page_items()
        return f"Hiển thị {start_index + 1}–{end_index} trên tổng số {total_items} tài sản"

    def get_page_indicator(self):
        total_items = self.get_total_items()
        if total_items == 0:
            return "Trang 0 / 0"
        total_pages = self.get_total_pages()
        return f"Trang {self.current_page} / {total_pages}"

    def is_prev_disabled(self):
        total_pages = self.get_total_pages()
        return self.current_page <= 1 or total_pages <= 1

    def is_next_disabled(self):
        total_pages = self.get_total_pages()
        return self.current_page >= total_pages or total_pages <= 1

    def next_page(self):
        total_pages = self.get_total_pages()
        if self.current_page < total_pages:
            self.current_page += 1

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1

    def set_page_size(self, new_size):
        self.page_size = new_size
        self.current_page = 1

# Sample 15 items mimicking NAB Master data
sample_15 = [
    {"id": i, "code": f"00109{200+i}", "name": f"Tài sản NAB {i+1}", "stt": str(i+1)}
    for i in range(15)
]

print("=== TEST 1: Default 10 rows/page on 15 items ===")
model = PaginationModel(sample_15, page_size=10)
assert model.page_size == 10
assert model.get_total_pages() == 2
items, start_idx, end_idx = model.get_page_items()
assert len(items) == 10, f"Expected 10 items, got {len(items)}"
stts_page1 = [start_idx + idx + 1 for idx in range(len(items))]
assert stts_page1 == list(range(1, 11)), f"STT Page 1 wrong: {stts_page1}"
assert model.get_stats_text() == "Hiển thị 1–10 trên tổng số 15 tài sản"
assert model.get_page_indicator() == "Trang 1 / 2"
assert model.is_prev_disabled() is True
assert model.is_next_disabled() is False
print(" -> Page 1 verified successfully!")

print("\n=== TEST 2: Navigate to Page 2 ===")
model.next_page()
assert model.current_page == 2
items2, start_idx2, end_idx2 = model.get_page_items()
assert len(items2) == 5, f"Expected 5 items on page 2, got {len(items2)}"
stts_page2 = [start_idx2 + idx + 1 for idx in range(len(items2))]
assert stts_page2 == list(range(11, 16)), f"STT Page 2 wrong: {stts_page2}"
assert items2[0]["code"] == "00109210", "Asset code must be preserved"
assert model.get_stats_text() == "Hiển thị 11–15 trên tổng số 15 tài sản"
assert model.get_page_indicator() == "Trang 2 / 2"
assert model.is_prev_disabled() is False
assert model.is_next_disabled() is True
print(" -> Page 2 verified successfully!")

print("\n=== TEST 3: Switch page size to 20 ===")
model.set_page_size(20)
assert model.current_page == 1
assert model.get_total_pages() == 1
items_all, _, _ = model.get_page_items()
assert len(items_all) == 15
assert model.get_stats_text() == "Hiển thị 1–15 trên tổng số 15 tài sản"
assert model.get_page_indicator() == "Trang 1 / 1"
assert model.is_prev_disabled() is True
assert model.is_next_disabled() is True
print(" -> Page size 20 verified successfully!")

print("\n=== TEST 4: Empty Dataset (0 items) ===")
empty_model = PaginationModel([], page_size=10)
assert empty_model.get_total_items() == 0
assert empty_model.get_stats_text() == "Hiển thị 0 trên tổng số 0 tài sản"
assert empty_model.get_page_indicator() == "Trang 0 / 0"
assert empty_model.is_prev_disabled() is True
assert empty_model.is_next_disabled() is True
print(" -> Empty dataset verified successfully!")

print("\n=== TEST 5: Dataset with <= 10 items (8 items) ===")
small_model = PaginationModel(sample_15[:8], page_size=10)
assert small_model.get_total_items() == 8
assert small_model.get_total_pages() == 1
assert small_model.get_stats_text() == "Hiển thị 1–8 trên tổng số 8 tài sản"
assert small_model.get_page_indicator() == "Trang 1 / 1"
assert small_model.is_prev_disabled() is True
assert small_model.is_next_disabled() is True
print(" -> Small dataset (<=10) verified successfully!")

print("\n=== TEST 6: Multi-page selection preservation ===")
model10 = PaginationModel(sample_15, page_size=10)
# Select item 3 on page 1 (id 2)
model10.selected_assets[2] = {"code": sample_15[2]["code"], "newDept": "Khối CNTT"}
# Go to page 2 and select item 12 (id 11)
model10.next_page()
model10.selected_assets[11] = {"code": sample_15[11]["code"], "newDept": "Ban Giám Đốc"}
# Return to page 1
model10.prev_page()
assert len(model10.selected_assets) == 2, "Both selections must be preserved across page switches"
assert 2 in model10.selected_assets and 11 in model10.selected_assets
print(" -> Multi-page selection retention verified successfully!")

print("\n=== TEST 7: Auto-clamping to latest valid page ===")
model_clamp = PaginationModel(sample_15, page_size=10)
model_clamp.next_page() # On page 2
assert model_clamp.current_page == 2
# Filter reduces dataset to 5 items (so total_pages becomes 1)
model_clamp.data = sample_15[:5]
model_clamp.clamp_page()
assert model_clamp.current_page == 1, f"Expected clamped to page 1, got {model_clamp.current_page}"
assert model_clamp.get_stats_text() == "Hiển thị 1–5 trên tổng số 5 tài sản"
print(" -> Auto-clamping verified successfully!")

print("\nALL PAGINATION LOGIC TESTS PASSED PERFECTLY!")
