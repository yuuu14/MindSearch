import pprint
from langchain_community.utilities import SearxSearchWrapper


search = SearxSearchWrapper(searx_host="http://10.50.60.21:8888")

results = search.results(
    query="上海的天气",
    num_results=10,
)
pprint.pp(results)
# results = search.results(
#     "Large Language Model prompt",
#     num_results=5,
#     categories="science",
#     time_range="year",
# )
# pprint.pp(results)

# arxiv_results = search.results(
#     "Large Language Model prompt", num_results=5, engines=["arxiv"]
# )
# pprint.pp(arxiv_results)


# git_results = search.results(
#     "large language model", num_results=20, engines=["github", "gitlab"]
# )
# pprint.pp(git_results)

# snippet title link engines category

## 
## https://python.langchain.com/docs/integrations/tools/searx_search/