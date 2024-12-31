
from mindsearch.agent.graph import SearcherAgent, ExecutionAction
from lagent.actions import WebBrowser
from datetime import datetime
from mindsearch.agent.models import azure
from copy import deepcopy
from lagent.agents.stream import get_plugin_prompt
from lagent.utils import create_object
from lagent.prompts import InterpreterParser, PluginParser
from mindsearch.agent.mindsearch_prompt import (
    FINAL_RESPONSE_CN,
    FINAL_RESPONSE_EN,
    GRAPH_PROMPT_CN,
    GRAPH_PROMPT_EN,
    searcher_context_template_cn,
    searcher_context_template_en,
    searcher_input_template_cn,
    searcher_input_template_en,
    searcher_system_prompt_cn,
    searcher_system_prompt_en,
    graph_fewshot_example_cn,
    graph_fewshot_example_en,
    fewshot_example_cn,
    fewshot_example_en,
)

from lagent.utils import GeneratorWithReturn

lang = "en"
date = datetime.now().strftime("The current date is %Y-%m-%d.")

llm_cfg = deepcopy(azure)
if llm_cfg is None:
    raise NotImplementedError
llm = create_object(llm_cfg)


plugins = [WebBrowser(searcher_type="SearXNG", topk=6)]

searcher_cfg=dict(
    llm=llm,
    plugins=plugins,
    template=date,
    output_format=PluginParser(
        template=(
            searcher_system_prompt_cn + fewshot_example_cn if lang == "cn" 
            else searcher_system_prompt_en + fewshot_example_en
        ),
        tool_info=get_plugin_prompt(plugins),
    ),
    user_input_template=searcher_input_template_cn if lang == "cn" 
        else searcher_input_template_en,
    user_context_template=searcher_context_template_cn if lang == "cn" 
        else searcher_context_template_en,
)

searcher_agent = SearcherAgent(**searcher_cfg)
action = ExecutionAction()


gen = GeneratorWithReturn(
    searcher_agent(
        question="the weather in Shanghai",
        topic="the weather in Shanghai and what to wear",
    )
)
for _ in gen:
    pass

print(gen.ret)
