DATA_DICT = {
    "personal_info": {
        "full_name": "",
        "gender": "",
        "address": "",
        "mother_maiden_name": "",
        "ssn": "",
        "geo_coordinates": "",
        "birthday": "",
        "age": "",
        "tropical_zodiac_sign": "",
    },
    "phone": {
        "phone_number": "",
        "country_code": ""
    },
    "online_info": {
        "email_address": "",
        "username": "",
        "password": "",
        "website": "",
        "browser_user_agent": "",
        "mail_receiving_url": ""
    },
    "financial_info": {
        "card_company": "",
        "card_number": "",
        "card_expiration_date": "",
        "card_verification_value": "",
    },
    "employment": {
        "company": "",
        "occupation": ""
    },
    "physical_characteristics": {
        "height": "",
        "weight": "",
        "blood_type": ""
    },
    "tracking_numbers": {
        "ups_tracking_number": "",
        "western_union_mtcn": "",
        "money_gram_mtcn": ""
    },
    "additional_info": {
        "favorite_color": "",
        "vehicle": "",
    }
}

NAME_SET = {
    'american': 'us',
    'arabic': 'ar',
    'australian': 'au',
    'brazil': 'br',
    'chechen_latin': 'celat',
    'chinese': 'ch',
    'chinese_traditional': 'zhtw',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'dk',
    'dutch': 'nl',
    'england_wales': 'en',
    'eritrean': 'er',
    'finnish': 'fi',
    'french': 'fr',
    'german': 'gr',
    'greenland': 'gl',
    'hispanic': 'sp',
    'hobbit': 'hobbit',
    'hungarian': 'hu',
    'icelandic': 'is',
    'igbo': 'ig',
    'italian': 'it',
    'japanese': 'jpja',
    'japanese_anglicized': 'jp',
    'klingon': 'tlh',
    'ninja': 'ninja',
    'norwegian': 'no',
    'persian': 'fa',
    'polish': 'pl',
    'russian': 'ru',
    'russian_cyrillic': 'rucyr',
    'scottish': 'gd',
    'slovenian': 'sl',
    'swedish': 'sw',
    'thai': 'th',
    'vietnamese': 'vn'
 }

COUNTRY_SET = {
    'australia': 'au',
    'austria': 'as',
    'belgium': 'bg',
    'brazil': 'br',
    'canada': 'ca',
    'cyprus_anglicized': 'cyen',
    'cyprus_greek': 'cygk',
    'czech_republic': 'cz',
    'denmark': 'dk',
    'estonia': 'ee',
    'finland': 'fi',
    'france': 'fr',
    'germany': 'gr',
    'greenland': 'gl',
    'hungary': 'hu',
    'iceland': 'is',
    'italy': 'it',
    'netherlands': 'nl',
    'new_zealand': 'nz',
    'norway': 'no',
    'poland': 'pl',
    'portugal': 'pt',
    'slovenia': 'sl',
    'south_africa': 'za',
    'spain': 'sp',
    'sweden': 'sw',
    'switzerland': 'sz',
    'tunisia': 'tn',
    'united_kingdom': 'uk',
    'united_states': 'us',
    'uruguay': 'uy'
}

FEED = {
    "Mother's maiden name": ["personal_info", "mother_maiden_name"],
    "Geo coordinates": ["personal_info", "geo_coordinates"],
    "Phone": ["phone", "phone_number"],
    "Country code": ["phone", "country_code"],
    "Birthday": ["personal_info", "birthday"],
    "Age": ["personal_info", "age"],
    "Tropical zodiac": ["personal_info", "tropical_zodiac_sign"],
    "Username": ["online_info", "username"],
    "Password": ["online_info", "password"],
    "Website": ["online_info", "website"],
    "Browser user agent": ["online_info", "browser_user_agent"],
    "Visa": ["financial_info", "card_number"],
    "MasterCard": ["financial_info", "card_number"],
    "Expires": ["financial_info", "card_expiration_date"],
    "CVV2": ["financial_info", "card_verification_value"],
    "CVC2": ["financial_info", "card_verification_value"],
    "Company": ["employment", "company"],
    "Occupation": ["employment", "occupation"],
    "Height": ["physical_characteristics", "height"],
    "Weight": ["physical_characteristics", "weight"],
    "Blood type": ["physical_characteristics", "blood_type"],
    "UPS tracking number": ["tracking_numbers", "ups_tracking_number"],
    "Western Union MTCN": ["tracking_numbers", "western_union_mtcn"],
    "MoneyGram MTCN": ["tracking_numbers", "money_gram_mtcn"],
    "Favorite color": ["additional_info", "favorite_color"],
    "Vehicle": ["additional_info", "vehicle"]
}

DEFAULTS = {
    "name": "us",
    "country": "us",
    "gender": "50",
    "age": ("19", "85")
}
