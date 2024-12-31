import lmdeploy
from lmdeploy import TurbomindEngineConfig

backend_config = TurbomindEngineConfig(cache_max_entry_count=0.0001)

pipe = lmdeploy.pipeline(
    model_path="/home/yu/.cache/modelscope/hub/internlm/internlm2_5-7b-chat",
    backend_config=backend_config
)

response = pipe(["Hi, pls intro yourself", "Shanghai is"])
print(response)