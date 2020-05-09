from .data_dicts import DATA_DICT, NAME_SET, COUNTRY_SET, DEFAULTS, FEED
from bs4 import BeautifulSoup
import requests

def preprocessCodeString(string):
    return "_".join(string.lower().replace("/", "_").replace("(", "").replace(")", "").split())

def beautifyText(text):
    return " ".join([a for a in text.replace("\n", "").split() if not a == ""])

def get(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    try:
        r = requests.get(url, headers = headers)
        if r.status_code == 200:
            return r.text
        else:
            print("Response Code: ", r.status_code)
            return ""
    except requests.exceptions.RequestException as err:
        print(err)
        return ""

def generate_url(name_set, country, gender, age):
    country = preprocessCodeString(country)
    name_set = preprocessCodeString(name_set)
    if country in COUNTRY_SET:
        country = COUNTRY_SET[country]
    else:
        print("Country either not set or is invalid. Resorting to default.")
        country = DEFAULTS["country"]
    if name_set in NAME_SET:
        name_set = NAME_SET[name_set]
    else:
        print("Name Set either not set or is invalid. Resorting to default.")
        name_set = DEFAULTS["name"]
    gender = gender.lower()
    if gender == "male":
        gender = "100"
    elif gender == "female":
        gender = "0"
    else:
        print("Choose either of Male or Female as gender. Resorting to default.")
        gender = DEFAULTS["gender"]
    status = False
    if type(age) in [int, str] and age != "":
        age = str(int(float(age)))
        min_age = age
        max_age = age
        status = True
    elif type(age) in [list, tuple]:
        if len(age) >= 2:
            try:
                min_age = str(int(float(age[0])))
                max_age = str(int(float(age[1])))
                status = True
            except:
                pass
    if status is False:
        print("Invalid age parameter provided. Resorting to default")
        min_age = DEFAULTS["age"][0]
        max_age = DEFAULTS["age"][1]

    return f'https://www.fakenamegenerator.com/advanced.php?t=country&n%5B%5D={name_set}&c%5B%5D={country}&gen={gender}&age-min={min_age}&age-max={max_age}'

def generate_fake_id(name_set = "", country = "", gender = "", age = ""):
    url = generate_url(name_set, country, gender, age)
    print("URL:", url)
    new = dict(DATA_DICT)
    soup = BeautifulSoup(get(url), "html.parser")
    a = soup.find(lambda tag: tag.name == "img" and tag.get('alt') in ["Female", "Male"])
    if a:
        new["personal_info"]["gender"] = a.get("alt", "")
    soup = soup.find('div', {'class': 'info'})
    if soup:
        a = soup.find('div', {'class': 'address'})
        if a:
            adr = a.find('h3')
            if adr:
                new["personal_info"]["full_name"] = adr.text
            adr = a.find("div", {'class': "adr"})
            if adr:
                new["personal_info"]["address"] = beautifyText(BeautifulSoup(str(adr).replace("<br/>", "; "), "html.parser").text)
        a = soup.find("dt", text = "SSN")
        if a:
            a = a.findNext("dd")
            if a:
                new["personal_info"]["ssn"] = a.text.split()[0]
        a = soup.find("dt", text = "Email Address")
        if a:
            a = a.findNext("dd")
            if a:
                new["online_info"]["email_address"] = a.text.split()[0]
                a = a.find('a')
                if a:
                    new["online_info"]["mail_receiving_url"] = a.get("href", "")
        a = soup.find(lambda tag: tag.name == "dt" and tag.text in ["Visa", "MasterCard"])
        if a:
            new["financial_info"]["card_company"] = a.text
        for x, y in FEED.items():
            a = soup.find("dt", text = x)
            if a:
                a = a.findNext("dd")
                if a:
                    new[y[0]][y[1]] = a.text
    return new
