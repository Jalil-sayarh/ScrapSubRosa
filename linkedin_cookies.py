import browser_cookie3
import requests

# Extract cookies from the browser
cookiejar_simple = browser_cookie3.firefox(domain_name='www.linkedin.com')

# Convert cookies to a format usable by Requests while avoiding duplicates
cookiejar = requests.cookies.RequestsCookieJar()

# Keep track of added cookies to avoid duplicates
added_cookies = set()

for cookie in cookiejar_simple:
    # Create a unique identifier for each cookie (name + domain + path)
    cookie_identifier = (cookie.name, cookie.domain, cookie.path)
    
    if cookie_identifier not in added_cookies:
        cookiejar.set_cookie(cookie)
        added_cookies.add(cookie_identifier)
        
from requests.cookies import RequestsCookieJar

# Create a RequestsCookieJar instance
abdeljalilsayarhgmailcom = RequestsCookieJar()

# Add cookies to the jar
abdeljalilsayarhgmailcom.set("li_alerts", "e30=", domain="www.linkedin.com")
abdeljalilsayarhgmailcom.set("li_rm", "AQG3_nKHho4ubwAAAZOwaoivj1979hl4v0UD7HPGXY_K4tZSqjrcghalMlEgHuqncZYq108xtuo3k27WBscd5UW89TCsn3-GmoAh8kc6W8CwCj239m9_jv4Z", domain=".www.linkedin.com")
abdeljalilsayarhgmailcom.set("li_at", "AQEDASa4zgsDnJO7AAABk7Bru4oAAAGT1Hg_ik0AH8wea1TatSSjWEa4vh3bWTxmeaJByFf0LbLQUM2yIJAX_SFumle4GxSNvak8-qZg-wYOpVjIsr8AGaUyO5v4e3BvWcvNoqTc2zZu-26V1f9-5NlU", domain=".www.linkedin.com")
abdeljalilsayarhgmailcom.set("JSESSIONID", "ajax:3105849245320411360", domain=".www.linkedin.com")
abdeljalilsayarhgmailcom.set("timezone", "Europe/Paris", domain=".www.linkedin.com")
abdeljalilsayarhgmailcom.set("li_theme", "light", domain=".www.linkedin.com")
abdeljalilsayarhgmailcom.set("li_theme_set", "app", domain=".www.linkedin.com")
abdeljalilsayarhgmailcom.set("bscookie", "v=1&20241210115304eb556749-52af-4c24-85ba-d068e8fb8510AQFDh5DxW1hc5k52Ct2rpJP8zqhXDJK-", domain=".www.linkedin.com")

# Cookies are now stored in the 'abdeljalilsayarhgmailcom' variable

from requests.cookies import RequestsCookieJar

# Create a new RequestsCookieJar instance for the new account
frstscoutgmailcom = RequestsCookieJar()

# Add cookies to the jar
frstscoutgmailcom.set("li_g_recent_logout", "v=1&true", domain="www.linkedin.com")
frstscoutgmailcom.set("g_state", '{"i_p":1734007696516,"i_l":1}', domain="www.linkedin.com")
frstscoutgmailcom.set("fcookie", "AQEAu0D2FuwKJQAAAZO6f8hEY6gaoCB5JXc690kcREdHlH9k9_weCHBJ24Hz9gxkkh-ADIxKCB4zZaMuStAATwaqw9SNeGxGgKmwLLxAKvr6iP9ooRctr_uYB2mNFQnL2p2NbCXp3sLGsEL5Zlk_3X0u6Kf7HCwNWE8xci4tx7-jbDh5cwE2vC-MaLoYdrimOgVKxmELHgT9i4dXItpRLbiayjrM0TxKAaw1NUsg8su5NiqAHqRIKF9r0UsZKmE5p0hBvON0mjUr+aNRt6S9fRnZP2T35pgwqOKnKwy4FRkqXow4Q1qKhaOg8Un+Mn0xmBty5DgJDQ==", domain="www.linkedin.com")
frstscoutgmailcom.set("fid", "AQGI-7oA6DcjewAAAZO6mFr8VGdxin6Vw24g83H0SEmVVc1MK7syq4AZ3SiiG1WXuYw8ZH0n3diZ4A", domain="www.linkedin.com")
frstscoutgmailcom.set("li_alerts", "e30=", domain="www.linkedin.com")
frstscoutgmailcom.set("chp_token", "AgGqNEuQiQMxtgAAAZO6f0O829UUNubbGcaWSFeMQtMiBfIytCkSw7w1ql4zMZuCr_cwrDOTIPsXCMrBW4DNrtKY185Je14hGUcdKg", domain=".www.linkedin.com")
frstscoutgmailcom.set("li_at", "AQEDAVW2LDUEyCBGAAABk7qhetYAAAGT3q3-1lYAziOQACRBVxctxTYBqJ9QRNYRzrtnsfpfENtRNPt5OqGNZ9EcDD3gAAsFzbJEUi1BOwogvb8Xgi3EDYCG2nEQOvK2_diS8r1kgDZLZjKbpGCJdDve", domain=".www.linkedin.com")
frstscoutgmailcom.set("li_rm", "AQEd3OgQzGg8jAAAAZO6oXvflineh9g_qPGz6B30udzqM6HIgOohMza2xU4GNglVF6IyLzDSCZUiuvaOtBZzPQ-7MfLp51-fjuV48gd8fU3xURRnrcTGyqLyuJf97sUXF0oY3aVxG2gaKfzSDjVwycb2Ds6unZ1RQyeiK_kJcv82T8ncK5yrxPsE9yWMuRhoV-30YyWx5Sa-KmuYXgb5GDVPfzNBRXvMBZpbT86D0rNrXaqot4HIEOk_N_20K4TsMY32OIP8MMmlZyNgkGgPuEg8NbyjHXk2IP4sMR598puNcNGJBqSpsdweXgj6TxlufQzgWLCzwv02hthl1Bk", domain=".www.linkedin.com")
frstscoutgmailcom.set("bscookie", "v=1&20241210115304eb556749-52af-4c24-85ba-d068e8fb8510AQFDh5DxW1hc5k52Ct2rpJP8zqhXDJK-", domain=".www.linkedin.com")
frstscoutgmailcom.set("timezone", "Europe/Paris", domain=".www.linkedin.com")
frstscoutgmailcom.set("li_theme", "light", domain=".www.linkedin.com")
frstscoutgmailcom.set("li_theme_set", "app", domain=".www.linkedin.com")
frstscoutgmailcom.set("JSESSIONID", "ajax:1633448646683150934", domain=".www.linkedin.com")

# Cookies for the new account are now stored in 'frstscoutgmailcom'

accounts_cookies = {
    "abdeljalil.sayarh@gmail.com": abdeljalilsayarhgmailcom,
    "frstscout@gmail.com": frstscoutgmailcom
}
