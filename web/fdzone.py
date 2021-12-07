import func
import os
def main(url):
    soup = func.get_url(url)
    folder = soup.find('td', class_='subjecttable').find('span', class_='bold')
    func.make_folder(folder.text)
    os.system('rm -r imglink.txt')
    func.write_source_url(url)
    images = soup.find_all('img', class_='post-image')
    for image_count, image_link in enumerate(images, 1):
        open('imglink.txt', 'a+').write(image_link['src'] + '\n' + f'  out={image_count}.jpg\n')
