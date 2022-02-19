import func
import os
import requests
def main(url):
    try: os.remove('imglink.txt')
    except:pass
    soup = func.get_url(url)
    down_btn1 = soup.find('a', class_='download_post')['href']
    soup = func.get_url(down_btn1)
    down_btn2 = soup.find('span', class_='download_post')

    dirs = down_btn2['dir']
    post_id = down_btn2['post_id']
    post_name = down_btn2['post_name']
    func.make_folder(post_name)
    func.write_source_url(url)

    params = (
        ('dir', dirs),
        ('post_id', post_id),
        ('post_name', post_name),
    )
    down_lnk = requests.get('https://asiantolick.com/ajax/download_post.php', params=params).content.decode('UTF-8')
    open('imglink.txt', 'w').write(down_lnk)

# main('https://asiantolick.com/post-1840/-%E5%8D%BF%E5%8D%BF%E5%8F%A3%E7%BD%A9%E5%A8%98-sexy-body-32p')