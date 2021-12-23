import requests
import os, re
from bs4 import BeautifulSoup

def write_source_url(url):
  with open("source.txt", "w")as f:f.write(url)

def get_url(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.content, "html.parser", from_encoding = 'utf-8')
  return soup

def make_folder(folder):
  folder = re.sub('[p#%&\\<>*?/$!\'":@+`|=]', '', folder)
  try:
    os.mkdir(folder)
    print(f'Folder Created: {folder}')
  except:pass
  os.chdir(folder)