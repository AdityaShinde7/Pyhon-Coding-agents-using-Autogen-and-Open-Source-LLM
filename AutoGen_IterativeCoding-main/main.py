from IterativeTools import IterativeCoding

# llm model 
llm_model = 'gpt-3.5-turbo'#'gpt-3.5-turbo' 'gpt-4-0613'

config_list = [
    {
        'model': llm_model,
        'api_key': 'YOUR API KEY HERE',   
        'api_type': 'open_ai',
        'api_base': 'http://localhost:1234/v1',
        'api_key': 'NULL'
    }  # OpenAI API endpoint for gpt-3.5-turbo
 
]

llm_config = {"config_list": config_list, "seed": 42}

gpt_config = {
    "seed": 42,  # change the seed for different trials
    "temperature": 0,
    "config_list": config_list,
    "request_timeout": 120,
}

p = IterativeCoding(gpt_config)
p.setProjectDir("IterCode_Projects/")
p.run()