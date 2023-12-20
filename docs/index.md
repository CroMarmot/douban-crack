# Home

## Quick Start

```sh
# Install lib
pip3 install douban-crack
# Download
```

```python
import requests
from douban_crack import crack_html
r = requests.get("https://search.douban.com/book/subject_search?search_text=黑天鹅&cat=1001")
assert r.status_code == 200
print(crack_html(r.text))
```
