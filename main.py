from tasnim import get_tasnim
from shahrkhabar import get_shahrkhabar
import pandas as pd
import json
try:
    with open("scraper_v5/sources.json", encoding="utf-8") as f:
        sources = json.load(f)
    my_list = []
    for item in sources["tasnim"]:
        my_list.extend(get_tasnim(item["url"], item["category"]))
    for item in sources["shahrkhabar"]:
        my_list.extend(get_shahrkhabar(item["url"], item["category"]))
    df = pd.DataFrame(my_list)
    df.to_csv("scraper_v5/titles.csv", index=False, encoding="utf-8-sig")
except Exception as e:
    print(f"Error fetching : {e}")