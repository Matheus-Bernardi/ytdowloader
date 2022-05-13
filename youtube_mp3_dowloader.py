from youtube_dl import YoutubeDL

def main():

  with open('urls.txt', 'r') as file:
    urls = file.readlines()

  for video in urls:
    video_info = YoutubeDL().extract_info(
      url=video, download=False
    )

    file_name: str = video_info.get('title', 'defaultTitle').replace('/', '')
    url: str = video_info.get('webpage_url')

    options = {
      'format': 'bestaudio/best',
      'keepvideo': False,
      'outtmpl': f"{file_name}.mp3",
    }

    with YoutubeDL(options) as ydl:
      ydl.download([url])

    print("Download complete... ")

if __name__ == '__main__':
  main()
