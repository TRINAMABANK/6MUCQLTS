import subprocess
import os

path = os.path.abspath('header_test.png')
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    f'--screenshot={path}',
    '--window-size=1500,950',
    'http://localhost:8080/index.html'
]
res = subprocess.run(cmd, capture_output=True, text=True)
print('Screenshot saved:', os.path.exists(path), 'size:', os.path.getsize(path) if os.path.exists(path) else 0)
