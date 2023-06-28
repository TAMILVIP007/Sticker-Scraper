import cloudscraper
from flask import Flask, request, jsonify
import re
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time
scraper = cloudscraper.create_scraper()

app = Flask(__name__)

mainurl = 'https://combot.org/telegram/stickers?q='


@app.route("/")
def index():
    return "Hemlo!"


@app.route('/stickers')
def search_stickers():
    query = request.args.get('q')
    all_links = {}
    start = time.time()
    try:
        r = scraper.get(mainurl + query)
        if r.status_code != 200:
            return jsonify({"total": 0, "result": [], "time_taken": time.time() - start})
        page_links = re.findall(r'(/telegram/stickers\?page=\d+)', r.text)
        def scrape_page(page_link):
            page_response = scraper.get(f"https://combot.org{page_link}")
            if page_response.status_code == 200:
                soup = BeautifulSoup(page_response.text, 'html.parser')
                links = soup.find_all("a", {"class": "sticker-pack__btn"})
                titles = soup.find_all("div", "sticker-pack__title")
                for link, title in zip(links, titles):
                    sticker_name = title.text
                    sticker_link = link['href']
                    if sticker_name not in all_links:
                        all_links[sticker_name] = sticker_link
        with ThreadPoolExecutor() as executor:
            executor.map(scrape_page, page_links)
        unique_stickers = [{"title": name, "link": link}
                           for name, link in all_links.items()]
        response = {
            "total": len(unique_stickers),
            "result": unique_stickers,
            "time_taken": time.time() - start
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"total": 0, "result": [], "time_taken": time.time() - start})


if __name__ == '__main__':
    app.run()
