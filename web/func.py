import requests
import os
from bs4 import BeautifulSoup

def write_source_url(url):
  with open("source.txt", "w")as f:f.write(url)

def get_url(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.content, "html.parser", from_encoding = 'utf-8')
  return soup

def make_folder(folder):
  try:
    os.mkdir(os.path.join(os.getcwd(), folder))
    print(f'Folder Created: {folder}')
  except:pass
  os.chdir(os.path.join(os.getcwd(), folder))