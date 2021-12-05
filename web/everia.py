import func
import os
def main(url):
    try: os.remove('imglink.txt')
    except:pass
    soup = func.get_url(url)
    folder = soup.find("h1", class_="entry-title").text
    func.make_folder(folder)
    func.write_source_url(url)
    images = soup.find("div", class_="entry-content").find_all("img")
    image_count = 0
    for image in images:
      image_count += 1
      image_link = image["src"]
      open('imglink.txt', 'a+').write(image_link + '\n' + '  out=' + str(image_count) + '.jpg\n')
    print(f'Scraped {image_count} Total Images')
