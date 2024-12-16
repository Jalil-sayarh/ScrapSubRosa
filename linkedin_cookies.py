from requests.cookies import RequestsCookieJar

# JSON string of cookies
cookies_jalil =[
{
    "domain": ".linkedin.com",
    "expirationDate": 1734344443,
    "hostOnly": False,
    "httpOnly": True,
    "name": "__cf_bm",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "l7SMpapLhG.L6NOMgxG5ZVQRJ33RXZsKyen0MXtpn8c-1734342645-1.0.1.1-sIngfq9Abz39e4nYN3i_0LFuqmSdOjvgI8zOAYVG3Z9hBqZoqXFzPqASXNZZvg4bxvfOxIIkuPjCrwvS04Jbxw",
    "id": 1
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1735646485,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_gcl_au",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1.1.866595068.1727870485.399077303.1731666806.1731666806",
    "id": 2
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1735646603,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_guid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "8446126d-ed9a-43fc-b078-04e76ce2da33",
    "id": 3
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1736934644,
    "hostOnly": False,
    "httpOnly": False,
    "name": "aam_uuid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "17983546297555526760035632484875148218",
    "id": 4
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1749894644,
    "hostOnly": False,
    "httpOnly": False,
    "name": "AMCV_14215E3D5995C57C0A495C55%40AdobeOrg",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "-637568504%7CMCIDTS%7C20074%7CMCMID%7C17457487507274261590050024149271210097%7CMCAAMLH-1734947444%7C6%7CMCAAMB-1734947444%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1734349844s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C465922018",
    "id": 5
},
{
    "domain": ".linkedin.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "1",
    "id": 6
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1736695415,
    "hostOnly": False,
    "httpOnly": False,
    "name": "AnalyticsSyncHistory",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "AQKEesS5TLmVawAAAZPAnkFbiSIOYixn8R3EWAJuclnFYKuyfiwRdPMInrBfceX4xWJcBF0V05Ig7lgMg-cNsg",
    "id": 7
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1765878662,
    "hostOnly": False,
    "httpOnly": False,
    "name": "bcookie",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "\"v=2&2001cb8e-42a2-4074-8430-6ea2a4858f66\"",
    "id": 8
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1759250706,
    "hostOnly": False,
    "httpOnly": True,
    "name": "dfpfpt",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "c9c4b87b14ba4d5dbdfb969c5419de64",
    "id": 9
},
{
    "domain": ".linkedin.com",
    "hostOnly": False,
    "httpOnly": True,
    "name": "fptctx2",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": True,
    "storeId": "0",
    "value": "taBcrIH61PuCVH7eNCyH0MJojnuUODHcZ6x9WoxhgCn%252f8PUCZxAEbxqPOnsw5wnJm9614FowAsFz%252feYHi%252bv3ATWUlklOTKXAN923czCzP%252b7k%252fxkj1LeRm%252bUVOyHDwD%252bH58WRBF0VmK%252fj8SBqBqJBVUkhHa98vDtwxnfkRP9nVaaFZ%252fDIrWBo9Zr%252bZdtkradr5wUgiO1thHjnEbpKcKK2pZFeVD0TCCJHl%252f0HHteTjeFdGHT%252frhCBxx5KAlojj62DuGYOY2HEDbZh5%252bnQ668KUop02upv1hjMrETxHT89OiPdkJ3eyNp%252fhRwFgdmnDLwQDq4XPxRRjtqJd9dnEgvPDVpauTyHsiQYUme6lmQydsE%253d",
    "id": 10
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1745068565,
    "hostOnly": False,
    "httpOnly": False,
    "name": "gpv_pn",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "www.linkedin.com%2Fin%2Fam%25Cid-redacted%25Aid-redactedlie-courant-id-redacted%2F",
    "id": 11
},
{
    "domain": ".linkedin.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "lang",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": True,
    "storeId": "0",
    "value": "\"v=2&lang=en-us\"",
    "id": 12
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1743266696,
    "hostOnly": False,
    "httpOnly": False,
    "name": "li_gc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "MTsyMTsxNzI3NzE0Njk4OzI7MDIxJWLl78i2qmo27JmiYtmDhOrMMH053S/JGqYeZbmqTgw=",
    "id": 13
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1749894462,
    "hostOnly": False,
    "httpOnly": False,
    "name": "li_mc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "MTsyMTsxNzM0MzQyNDY0OzI7MDIxcy+zswGIc0169G5W1vBQT0Ko/+AVj8jYOaSEBddeTqk=",
    "id": 14
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1742118662,
    "hostOnly": False,
    "httpOnly": False,
    "name": "li_sugr",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "7cf97e63-1970-4a1d-87be-70a095946a1f",
    "id": 15
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1765586243,
    "hostOnly": False,
    "httpOnly": False,
    "name": "liap",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "True",
    "id": 16
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1734367657,
    "hostOnly": False,
    "httpOnly": False,
    "name": "lidc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "\"b=TB79:s=T:r=T:a=T:p=T:g=3720:u=711:x=1:i=1734342664:t=1734367659:v=2:sig=AQEi2o5TVRxHUJ55qX65mRQLoXpn1D9Y\"",
    "id": 17
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1736695416,
    "hostOnly": False,
    "httpOnly": False,
    "name": "lms_ads",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "AQFgvtewHwgUbwAAAZPAnkPNiE7zT3wyO8jQ-fkvbPk2zNcQPUFN-oVdyV3oU4_OBk2fAEVl6-bkNBrGLWPkXIYWEdc7uejY",
    "id": 18
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1736695416,
    "hostOnly": False,
    "httpOnly": False,
    "name": "lms_analytics",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "AQFgvtewHwgUbwAAAZPAnkPNiE7zT3wyO8jQ-fkvbPk2zNcQPUFN-oVdyV3oU4_OBk2fAEVl6-bkNBrGLWPkXIYWEdc7uejY",
    "id": 19
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1745068548,
    "hostOnly": False,
    "httpOnly": False,
    "name": "s_ips",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "665.4444427490234",
    "id": 20
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1745068565,
    "hostOnly": False,
    "httpOnly": False,
    "name": "s_tp",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "2443",
    "id": 21
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1745068565,
    "hostOnly": False,
    "httpOnly": False,
    "name": "s_tslv",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1729516565595",
    "id": 22
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1736934660,
    "hostOnly": False,
    "httpOnly": False,
    "name": "UserMatchHistory",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "AQITxoVD7zxh8QAAAZPO4MG7H5cQhPE8n9u8kx7KeTSgH4h708ENob2HdPr0lXftosE1YrK-fTBNHYQiOSMXcF4-UFBKOdPGRveHm45BrxsRRMKZo5J2U50BAZfRRMDutBMbFbWe9ZJus85TVcJA9ywkwG3aG8kupCR5myd7bb0SqmAOSSTnf8Yxqihp7-Tsri-laRemcu6QuyQSvuwhOfyKxAn1ySOCePbzPWTN10Pw0gxahsAbERXxOBIINz8fqvJrYbbSIdJ62p-zb5thHkUcxYAViXaM9WSYLyyftXs2aauXeql-YbcDYely-_qYpnXZbAahyDEMiiMIQFIk6x4HY29XsiC94LyZwtgaIXHG3eFvHQ",
    "id": 23
},
{
    "domain": ".linkedin.com",
    "expirationDate": 1762430465,
    "hostOnly": False,
    "httpOnly": False,
    "name": "visit",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "v=1&M",
    "id": 24
},
{
    "domain": ".www.linkedin.com",
    "expirationDate": 1765639416,
    "hostOnly": False,
    "httpOnly": True,
    "name": "bscookie",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "\"v=1&2024093016445293a6f471-a352-4813-8783-ca29f7a21a14AQFgQZmou81_hM102gaXN4aq8C9G-t5p\"",
    "id": 25
},
{
    "domain": ".www.linkedin.com",
    "expirationDate": 1765586243,
    "hostOnly": False,
    "httpOnly": False,
    "name": "JSESSIONID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "\"ajax:7580219957469720317\"",
    "id": 26
},
{
    "domain": ".www.linkedin.com",
    "expirationDate": 1765586243,
    "hostOnly": False,
    "httpOnly": True,
    "name": "li_at",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "AQEDASa4zgsBBoZ1AAABkk0c9BUAAAGT4X9rVk0ABIrFec5SZz8iYbh01szWoDn5aelYnjpvBRjCcn1cuWAW9OoMlnO6s4a8sUIWzCrpf3GzIJm8z_QPtbt5E1TITEVahpsEoWHi5bIJEDN1G6DUzsUw",
    "id": 27
},
{
    "domain": ".www.linkedin.com",
    "expirationDate": 1759406461,
    "hostOnly": False,
    "httpOnly": True,
    "name": "li_rm",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "AQF8vBFwCsRt6wAAAZJNGuzCd6TW5YLgQJI5aagt2_UEEBZs1xD7JRYiwDcq84GjjxctHKgqFNCneV7K6hLLfPabhQOk18Ye9Z0MJBFHvKl4Q2BGQlOLGlTD",
    "id": 28
},
{
    "domain": ".www.linkedin.com",
    "expirationDate": 1749891053,
    "hostOnly": False,
    "httpOnly": False,
    "name": "li_theme",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "light",
    "id": 29
},
{
    "domain": ".www.linkedin.com",
    "expirationDate": 1749891053,
    "hostOnly": False,
    "httpOnly": False,
    "name": "li_theme_set",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "app",
    "id": 30
},
{
    "domain": ".www.linkedin.com",
    "expirationDate": 1735552252,
    "hostOnly": False,
    "httpOnly": False,
    "name": "timezone",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "Europe/Paris",
    "id": 31
},
{
    "domain": "www.linkedin.com",
    "expirationDate": 1743422469,
    "hostOnly": True,
    "httpOnly": False,
    "name": "g_state",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "{\"i_l\":1,\"i_p\":1727877669867}",
    "id": 32
},
{
    "domain": "www.linkedin.com",
    "expirationDate": 1759406479,
    "hostOnly": True,
    "httpOnly": False,
    "name": "li_alerts",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "e30=",
    "id": 33
}
]

cookie_jars = RequestsCookieJar()

# Populate the cookie jar
for cookie in cookies_jalil:
    cookie_jars.set(
        name=cookie["name"],
        value=cookie["value"],
        domain=cookie["domain"],
        path=cookie["path"],
        secure=cookie.get("secure", False),
        rest={"HttpOnly": cookie.get("httpOnly", False)}
    )

accounts_cookies = {
    "abdeljalil.sayarh@gmail.com": cookie_jars
 }
