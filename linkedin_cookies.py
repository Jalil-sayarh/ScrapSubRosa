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
cookies = RequestsCookieJar()

# Add cookies to the jar
cookies.set("li_alerts", "e30=", domain="www.linkedin.com")
cookies.set("li_rm", "AQG3_nKHho4ubwAAAZOwaoivj1979hl4v0UD7HPGXY_K4tZSqjrcghalMlEgHuqncZYq108xtuo3k27WBscd5UW89TCsn3-GmoAh8kc6W8CwCj239m9_jv4Z", domain=".www.linkedin.com")
cookies.set("li_at", "AQEDASa4zgsDnJO7AAABk7Bru4oAAAGT1Hg_ik0AH8wea1TatSSjWEa4vh3bWTxmeaJByFf0LbLQUM2yIJAX_SFumle4GxSNvak8-qZg-wYOpVjIsr8AGaUyO5v4e3BvWcvNoqTc2zZu-26V1f9-5NlU", domain=".www.linkedin.com")
cookies.set("JSESSIONID", "ajax:3105849245320411360", domain=".www.linkedin.com")
cookies.set("timezone", "Europe/Paris", domain=".www.linkedin.com")
cookies.set("li_theme", "light", domain=".www.linkedin.com")
cookies.set("li_theme_set", "app", domain=".www.linkedin.com")
cookies.set("bscookie", "v=1&20241210115304eb556749-52af-4c24-85ba-d068e8fb8510AQFDh5DxW1hc5k52Ct2rpJP8zqhXDJK-", domain=".www.linkedin.com")

# Cookies are now stored in the 'cookies' variable
