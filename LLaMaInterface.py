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
    pre_prompt = "You are a helpful assistant. Always answer as concise as possible. You only response once as 'Assistant'."
    prompt = "Seperate these into different titles for columns: RDHS Dengue Fever Dysentery Encephaliti Enteric Fever Food Poi- Leptospirosis Typhus Viral Hep- Human Chickenpox Meningitis Leishmania- WRCD"

    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', #LMM address
                           input={
                               "prompt": f"{pre_prompt} {prompt}",
                               "temperature": 0.75,
                               "top_p":0.9,
                               "max_length":128,
                               "max_new_tokens": 500,
                               "min_new_tokens": -1,
                               })
    
    response = ""

    for tokens in output:
        response += tokens

    print(response)

separateCellHeaders("")