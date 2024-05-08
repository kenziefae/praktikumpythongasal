import instaloader
loader = instaloader.Instaloader()

def download_post(urL):
    try:

        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])

        loader.download_post(post, target="testcoki")
        print("Postingan berhasil diunduh!")
    except Exception as e:
        print("terjadi kesalahan",str(e))


url = input ("enter your url: ")        
url = str(url)
download_post(url)