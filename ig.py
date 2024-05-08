import requests
from bs4 import BeautifulSoup

def get_video_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    video_url = soup.find("video").get("src")
    return video_url

def download_video(url, file_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers, stream=True)
    with open(file_name, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

if __name__ == "__main__":
    url = input("Masukkan URL video Instagram: ")
    video_url = get_video_url(url)
    print("URL video:", video_url)
    file_name = input("Masukkan nama file untuk video yang diunduh: ")
    download_video(video_url, file_name)
    print("Video berhasil diunduh!")

    # https://www.instagram.com/reels/C0MkIRlo6EG/?hl=en