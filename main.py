import re, os, subprocess

def regex(url):
    os.chdir('./download')
    re_buondua = re.search(r'buondua.com', url)
    re_telegraph = re.search(r'telegra.ph', url)
    re_everia = re.search(r'everia.club', url)
    re_173mt = re.search(r'173mt.com', url)
    re_hitxhot = re.search(r'(.+hitxhot\.com/gallerys/.+\.html)', url)
    re_jkforum = re.search(r'.+www\.jkforum\.net/thread.+\.html', url)

    if re_buondua:
        from web import buondua
        buondua.main(url)
    if re_telegraph:
        from web import telegraph
        telegraph.main(url)
    if re_everia:
        from web import everia
        everia.main(url)
    if re_173mt:
        from web import satutujuhtigaMT
        satutujuhtigaMT.main(url)
    if re_hitxhot:
        from web import hitxhot
        hitxhot.main(re_hitxhot.group(0))
    if re_jkforum:
        from web import jkforum
        jkforum.main(re_jkforum.group(0))

def main():
    url = input('Input URL: ')
    # url = 'https://www.jkforum.net/thread-12134822-1-1.html?number=6'
    regex(url)
    cwd = os.getcwd() # Current Working Directory
    aria2c(cwd)

def aria2c(cwd):
  subprocess.run(['aria2c', '--continue=true', '-j', '5', '-s', '5', '-i', 'imglink.txt'])
  subprocess.run(['rm', '-r', 'imglink.txt'])
  subprocess.run(['clear'])
  os.chdir(cwd)
  print('Download Successfully')

if __name__ == "__main__":
    main()
