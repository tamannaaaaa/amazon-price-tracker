from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = "pythondeveloper23072001@gmail.com"
MY_PASSWORD = "python@23"

product_url = "https://www.amazon.com/dp/B0053WRWX8/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0?th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 "
                  "Safari/537.36 ",
    "Accept-Language": "en-US,en;q=0.9"

}

response = requests.get(url=product_url, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")
price = soup.find(name="span", class_="a-offscreen").getText()
price_actual = price.split("$")[1]
price_ruppee = float(price_actual)
print(price_ruppee)

if price_ruppee > 100:
    content = f"The price for thr product is upto your expectations: {price_ruppee}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:\n\n{content}")
