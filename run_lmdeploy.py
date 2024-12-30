import lmdeploy
pipe = lmdeploy.pipeline("Shanghai_AI_Laboratory/internlm2_5-7b-chat")
response = pipe(["Hi, pls intro yourself", "Shanghai is"])
print(response)