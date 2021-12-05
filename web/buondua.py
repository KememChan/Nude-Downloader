import func
import os

page = 1
total_images = 0

def main(url):
    try: os.remove('imglink.txt')
    except:pass
    init(url)

def init(url):
    global page, total_images
    soup = func.get_url(url)
    folder = soup.title.text
    func.make_folder(folder)
    func.write_source_url(url)
    last_page = soup.find("div", class_="pagination-list").find_all("a")[-1]["href"][-1]
    while page <= int(last_page):
      print(f'Scraping The Web: {page}/{last_page}', end='\r')
      url2 = url + "?page=" + str(page)
      soup = func.get_url(url2)
      images = soup.find("div", class_="article-fulltext").find_all("img")
      for image in images:
          total_images += 1
          link = image["data-src"]
          with open('imglink.txt', 'a+') as f:
              f.write(link + '\n' + '  out=' + str(total_images) + '.jpg\n')
      page += 1
    print(f'Succesfully Scraping {total_images} Images')
