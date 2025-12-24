import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_shahrkhabar(url, category):
    try:
        my_list = []
        seen = set()
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find_all("h2")
        for i in title:
            if i is None:
                continue
            h2 = i.text.strip()
            if h2 in seen:
                continue
            if len(h2) < 3:
                continue
            seen.add(h2)
            my_list.append({
                "دسته":category,
                "خبر":h2,
                "خبر کامل":None,
                "طول خبر":len(h2),
                "منبع":"خبر فوری"
            })
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return my_list