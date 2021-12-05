#HitxHot Downloader
import os
import func
image_count = 0
def main(url):
  try: os.remove('imglink.txt')
  except:pass
  init(url)

def init(url):
  soup = func.get_url(url)
  folder = soup.title.text[12:-11]
  func.make_folder(folder)
  func.write_source_url(url)
  # print(f'Scraping: {page}/{last_page}', end = '\r')
  images = soup.find('div', class_ = "contentme").find_all('img')
  global image_count
  for image in images:
    image_count += 1
    link = image['src']
    open('imglink.txt', 'a+').write(link + '\n' + '  out=' + str(image_count) + '.jpg\n')
  try:
      next_page = soup.find(string='Next >').parent['href']
      url2 = url[:19]
      os.chdir('..')
      main(url2 + next_page)
  except:pass
