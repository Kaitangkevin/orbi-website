"""Export the static website with GitHub Pages' deployment base path."""
from pathlib import Path
import os, re, shutil
root = Path(__file__).resolve().parent.parent
base = os.environ.get('PAGES_BASE_PATH', '/orbi-website').rstrip('/')
if base and (not base.startswith('/') or '..' in base):
    raise ValueError('Invalid Pages base path')
output = root / '_site'
if output.exists():
    shutil.rmtree(output)
shutil.copytree(root / 'dist', output)
pattern = re.compile(r'''(["'`])/(?!/)([^"'`\s<>]*)''')
for path in output.rglob('*'):
    if path.suffix in {'.html', '.js', '.css'}:
        text = path.read_text()
        path.write_text(pattern.sub(lambda m: m[1] + base + '/' + m[2], text))
(output / '.nojekyll').touch()
print('Website prepared for', base or '/')
