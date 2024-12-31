
import pprint
from lagent.actions.web_browser import WebBrowser

_browser = WebBrowser(searcher_type="SearXNG", topk=6)
res = _browser.search("the weather in Shanghai and what to wear")
top = _browser.select([0, 1, 2])

# pprint.pp(res)
pprint.pp(top)
