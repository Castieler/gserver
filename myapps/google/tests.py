from django.test import TestCase

# Create your tests here.
import requests
from lxml import etree
url = 'https://www.google.com.hk/search?safe=strict&hl=zh-CN&q={0}'
res = requests.get(url.format('python'))
html = etree.HTML(res.text)
cate_list = html.xpath("//div[@class='g']")
