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