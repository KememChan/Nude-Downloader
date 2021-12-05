import func
import os
page = 1
image_count = 0

def main(url):
    try: os.remove('imglink.txt')
    except:pass
    init(url)

def init(url):
    global page, image_count
    url2 = url[:17]
    soup = func.get_url(url)
    folder = soup.title
    if folder is not None:
        func.make_folder(folder.text[:-17])
    func.write_source_url(url)
    last_page = soup.find('div', class_='article-paging').find_all('span')[-1].text
    images = soup.find_all('img', 'lazyload', alt=True)
    for image in images:
        image_link = image['data-src']
        image_count += 1
        open('imglink.txt', 'a+').write(image_link + '\n' + '  out=' + str(image_count) + '.jpg\n')
    while page < int(last_page):
        page += 1
        selected_page_url = soup.find(string=str(page)).parent.parent['href']
        url3 = url2 + selected_page_url
        os.chdir('..')
        main(url3)
# https://173mt.com/cn/42658_2.html
