import re, os, subprocess, sys

def main():
    # python main.py <downloadDir> <url>
    downloadDir = sys.argv[1]
    url = sys.argv[2]

    if os.path.isdir(downloadDir) is not True:
        os.mkdir(downloadDir)

    cwd = os.getcwd() # Current Working Directory
    regex(url, downloadDir)
    if os.path.isfile('imglink.txt'):
        aria2c(cwd)

def aria2c(cwd):
  subprocess.run(['aria2c', '--continue=true', '-j', '5', '-s', '5', '-i', 'imglink.txt'])
  subprocess.run(['rm', '-rf', 'imglink.txt'])
  subprocess.run(['clear'])
  os.chdir(cwd)
  print('Download Successfully')

def regex(url, downloadDir):
    os.chdir(downloadDir)
    re_buondua = re.search(r'buondua.com', url)
    re_fdzone = re.search(r'fdzone.org', url)
    re_telegraph = re.search(r'telegra.ph', url)
    re_everia = re.search(r'everia.club', url)
    re_173mt = re.search(r'173mt.com', url)
    re_hitxhot = re.search(r'(.+hitxhot\.com/gallerys/.+\.html)', url)
    re_jkforum = re.search(r'jkforum.net', url)
    re_asiantolick = re.search(r'.+asiantolick.com/post-.+', url)

    if re_asiantolick:
        from web import AsianToLick
        AsianToLick.main(url)
    if re_buondua:
        from web import buondua
        buondua.main(url)
    if re_fdzone:
        from web import fdzone
        fdzone.main(url)
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
        jkforum.main(url)

if __name__ == "__main__":
    main()
