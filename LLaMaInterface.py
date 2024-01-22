# Jun
# I'll look for another way to use LLM instead of this, but just for testing.

import os
import replicate

os.environ["REPLICATE_API_TOKEN"] = "r8_"
# "r8_8fIrIK5FiWIN4c2tlL6KQSgp5NaeD6k3ZGyYB" <-- don't use it for now

'''
Arguments: String with header file
Returns: List with different cell headers separated
'''
def separateCellHeaders(row):
    '''Prompt when we used LLaMa online:
    Separate these into different titles for columns:

    RDHS Dengue Fever Dysentery Encephaliti Enteric Fever Food Poi- Leptospirosis Typhus Viral Hep- Human Chickenpox Meningitis Leishmania- WRCD
    '''
    pre_prompt = "You are a helpful, respectful and honest assistant. Always answer as concise as possible. You don't include any other words than asked information. You only response once as 'Assistant'."
    prompt = "Separate these into different titles for columns (some are seperated by blank and some are not): RDHS Dengue Fever Dysentery Encephaliti Enteric Fever Food Poi- Leptospirosis Typhus Viral Hep- Human Chickenpox Meningitis Leishmania- WRCD"

    output = replicate.run('',#LMM address
                           input={
                               "prompt": f"{pre_prompt} {prompt} Assistant: ",
                               "temperature": 0.5,
                               "top_p":0.9,
                               "max_length":256,
                               "repetition_penalty":1,
                               "max_new_tokens": 500,
                               "min_new_tokens": -1
                               })
    
    print(output)
    print("Testing Cases?")

separateCellHeaders("")