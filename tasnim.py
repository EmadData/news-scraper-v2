import requests
from bs4 import BeautifulSoup
def get_tasnim(url, category):
    my_list = []
    seen = set()
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.find_all("div", class_="col-8 text-container vcenter")
        for i in text:
            h2_tag = i.find("h2")
            h4_tag = i.find("h4")

            if h2_tag is None or h4_tag is None:
                continue

            title_tag = h2_tag.text.strip()
            title_sub = h4_tag.text.strip()

            if len(title_sub) < 3 or len(title_tag) < 3:
                continue
            if title_sub in seen or title_tag in seen:
                continue
            seen.add(title_sub)
            seen.add(title_tag)
            my_list.append({
                "دسته": category,
                "خبر":title_tag,
                "خبر کامل":title_sub,
                "طول خبر":len(title_sub),
                "منبع": "تسنیم"
            })
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return my_list