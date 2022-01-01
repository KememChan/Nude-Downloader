# JKForum.nwt Downloader
import func
import re
def main(url):
    soup = func.get_url(url)
    folder = soup.find('h1')
    if folder is not None:
        func.make_folder(folder.text)
    func.write_source_url(url)
    image_count = None
    thread = soup.find(class_="thread-cont")
    for image_count, image_link in enumerate(thread.find_all(src=re.compile(r'.+mymypic.+')), 1):
       open('imglink.txt', 'a+').write(image_link['src'] + '\n' + '  out=' + str(image_count) + '.jpg\n')