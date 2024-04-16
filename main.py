from typing import NamedTuple
from urllib.parse import urljoin, quote

import pandas as pd
import requests
from bs4 import BeautifulSoup

from config import Config
from google_api import write_to_google_sheets


class PersonInfo(NamedTuple):
    name: str
    role: str
    img_src: str
    linkedin: str
    twitter: str
    personal: str


def scrapping():
    response = requests.get(Config.BASE_URL)
    soup = BeautifulSoup(response.text, 'lxml')

    people_info = []
    all_persons = soup.find_all("div", class_="speakers-list_item-wrapper")

    for person in all_persons:
        name = person.find("h3", class_="speakers-list_item-heading").text
        role = person.find("div", class_="").text
        relative_img_src = person.find("img").get("src")
        img_src = urljoin(Config.BASE_URL, quote(relative_img_src))
        linkedin = "No LinkedIn link"
        twitter = "No Twitter link"
        personal = "No Personal link"

        for link in person.find("div", class_="w-layout-grid speakers-list_social-list").find_all("a"):
            href = link['href']
            if "linkedin.com" in href:
                linkedin = href
            elif "twitter.com" in href:
                twitter = href
            elif "index.html#" != href:
                personal = href

        people_info.append(PersonInfo(
            name=name,
            role=role,
            img_src=img_src,
            linkedin=linkedin,
            twitter=twitter,
            personal=personal,
        ))
    df = pd.DataFrame(people_info)
    df.to_json('people_data.json', orient='records', indent=4)
    df.to_csv('people_data.csv')
    write_to_google_sheets(Config.SPREADSHEET_ID, PersonInfo._fields, people_info)


if __name__ == '__main__':
    scrapping()
