from webpage_cache import WebPage
import time

webpage = WebPage("https://huysfoundation.org/")

now = time.perf_counter()
content1 = webpage.content

content = []
fetch = []
for i in range(5):
    now = time.perf_counter()
    content.append(webpage.content)
    fetch.append(time.perf_counter() - now),
    print(f"Request {i}: {fetch[i]: .10f}")

for j in range(len(content) - 1):
    assert content[j] == content[j+1]