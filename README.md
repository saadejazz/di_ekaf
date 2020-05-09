# Fake ID Generator  
Scrapes data from [Fake Name Generator](https://www.fakenamegenerator.com) corresponding to given attributes.

## Getting Started  
* Pull the repository  
    ```bash
    mkdir di_ekaf
    cd di_ekaf
    git init
    git add .
    git remote add origin https://www.github.com/saadejazz/di_ekaf
    git pull origin master
    cd ..
    ```
* Install python dependencies  
    ```bash
    python -m pip install bs4 requests
    ```

## Code 
To generate a fake id, the following four attributes may be given:  
1. name_set -- corresponds to the locality/root of random name generated. Examples include "Arabic", "American", "Persian", etc.  
2. country -- corresponds to the location of the id which includes addresses, geo-coordinates, and phone number. Examples include "United Kingdom", "Germany", "Tunisia", etc.  
3. gender -- provide either "Male" or "Female". Default randomly selects between the two.  
4. age -- provided either an age number (in str format) or a tuple of ages: (min, max).  

**Note:** You can view all possible (and default) values of the above-mentioned attributes in di_ekaf/data_dicts.py 

```python
from di_ekaf.fake import generate_fake_id

result = generate_fake_id(name_set = "Russian", country = "Denmark", gender = "Female", age = "27")

# alternate option
# result = generate_fake_id(name_set = "Russian", country = "Denmark", gender = "", age = ("15", "27"))

print(result)

```

## Example Output  

```python
{
    'personal_info': {'full_name': 'Zarina Lazareva',
    'gender': 'Female',
    'address': 'Stokløkken 46; 3480 Fredensborg',
    'mother_maiden_name': '',
    'ssn': '',
    'geo_coordinates': '56.059172, 12.307519',
    'birthday': 'July 14, 1978',
    'age': '41 years old',
    'tropical_zodiac_sign': 'Cancer'},
    'phone': {'phone_number': '26-16-73-36', 'country_code': '45'},
    'online_info': {'email_address': 'ZarinaLazareva@rhyta.com',
    'username': 'Eareeter',
    'password': 'eiS4ahv6bux',
    'website': 'CenturyBowl.dk',
    'browser_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.132',
    'mail_receiving_url': 'http://www.fakemailgenerator.com/#/rhyta.com/zarinalazareva/'},
    'financial_info': {'card_company': 'Visa',
    'card_number': '4539 8232 2906 3653',
    'card_expiration_date': '3/2021',
    'card_verification_value': '168'},
    'employment': {'company': 'Chase Pitkin', 'occupation': 'HIV/AIDS nurse'},
    'physical_characteristics': {'height': '5\' 3" (161 centimeters)',
    'weight': '212.7 pounds (96.7 kilograms)',
    'blood_type': 'O+'},
    'tracking_numbers': {'ups_tracking_number': '1Z 208 913 64 9499 928 0',
    'western_union_mtcn': '4629504633',
    'money_gram_mtcn': '80730039'},
    'additional_info': {'favorite_color': 'Red', 'vehicle': '1992 Ford Mustang'}
}
```