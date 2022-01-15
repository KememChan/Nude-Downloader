import requests
import os
from bs4 import BeautifulSoup

def write_source_url(url):
  with open("source.txt", "w")as f:f.write(url)

def get_url(url):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
  }
  r = requests.get(url, headers=headers)
  soup = BeautifulSoup(r.content, "html.parser", from_encoding = 'utf-8')
  return soup

def make_folder(folder):
  try:
    os.mkdir(os.path.join(os.getcwd(), folder))
    print(f'Folder Created: {folder}')
  except:pass
  os.chdir(os.path.join(os.getcwd(), folder))