import threading
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"\nDownloaded {filename}")

urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg"
]

threads = []
for i, url in enumerate(urls):
    filename = f"image_{i+1}.jpg"
    thread = threading.Thread(target=download_file, args=(url, filename))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("All downloads completed")
