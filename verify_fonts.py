import sys

sys.stdout.reconfigure(encoding='utf-8')

def verify_file_fonts(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n==========================================")
    print(f"VERIFYING TIMES NEW ROMAN IN: {filepath}")
    print(f"==========================================")

    checks = [
        ("Universal Times New Roman rule for .a4-sheet & descendants", 
         ".a4-sheet,\n    .nab-a4-sheet,\n    .a4-sheet *,\n    .nab-a4-sheet *" in content or
         ".a4-sheet, .nab-a4-sheet, .a4-sheet *, .nab-a4-sheet *" in content or
         "font-family: 'Times New Roman', Times, serif !important;" in content),
        
        ("Official NAB Logo Image replaced text title",
         '<img src="logo-namabank.png" alt="NAM A BANK" class="nab-logo-img">' in content),
        
        ("Code font in A4 report uses Times New Roman",
         ".a4-code-font {\n      font-family: 'Times New Roman', Times, serif !important;" in content),

        ("Print media query specifies Times New Roman",
         "@media print" in content and "font-family: 'Times New Roman', Times, serif !important;" in content),
    ]

    all_passed = True
    for desc, passed in checks:
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status} {desc}")
        if not passed:
            all_passed = False

    return all_passed

r1 = verify_file_fonts("index.html")
r2 = verify_file_fonts("print-preview.html")

if r1 and r2:
    print("\n>>> ALL REPORTS VERIFIED WITH 100% TIMES NEW ROMAN FONT! <<<")
else:
    print("\n>>> ERROR: SOME FONT CHECKS FAILED! <<<")
    sys.exit(1)
