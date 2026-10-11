import requests
import time
from fake_useragent import UserAgent

url = 'https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&p%5B%5D=facets.ideal_for%255B%255D%3DMen&param=3523&offer=nb%3Amp%3A0757c88528%2Cnb%3Amp%3A07dc5a6d17%2Cnb%3Amp%3A08hcvv3723&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNoaXJ0cyx0ZWVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D'
# url = 'https://pages.daraz.com.bd/wow/gcp/route/daraz/mm/upr/router?hybrid=1&data_prefetch=true&prefetch_replace=1&at_iframe=1&wh_pid=%2Flazada%2Fchannel%2Fbd%2Fflashsale%2F8r7TbxhpSH&hide_h5_title=true&lzd_navbar_hidden=true&disable_pull_refresh=true&skuIds=543053403%2C1594777184%2C222336602%2C1586896739%2C256722371%2C387252151%2C1587536317&spm=a2a0e.tm80335411.FlashSale.d_shopMore'
# url = 'https://computermania.com.bd/product-category/cm-offers/'

s = requests.Session()
headers = {
    'User-Agent' : UserAgent().random,
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com'
}
time.sleep(2)
r = s.get(url)  
print(r.text)

with open('E:/Code/Python-Automation-60Days/day06/collected.html', 'w', encoding='utf-8') as f:
    f.write(r.text)