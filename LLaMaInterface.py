# Jun
# Local version of LLaMaInterface

from llama_cpp import Llama
import time

'''
Arguments: String with header file
Returns: List with different cell headers separated
'''
def separateCellHeaders(row):
    '''
    param row: string only contains the header
    Prompt when we used LLaMa online:
    Separate these into different titles for columns:

    RDHS Dengue Fever Dysentery Encephaliti Enteric Fever Food Poi- Leptospirosis Typhus Viral Hep- Human Chickenpox Meningitis Leishmania- WRCD
    '''
    pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as Assistant."
    prompt = "Seperate these into different titles for columns using commas: " + row
    
    LLM = Llama(model_path="./llama-2-7b-chat.Q5_K_M.gguf", n_ctx=2048)
    # WARNING! ggml is no longer compatable with llama_cpp, so use gguf models

    output = LLM(f"{prompt}", max_tokens=0)

    return output["choices"][0]["text"]

now = time.time()

test_out = separateCellHeaders("RDHS Dengue Fever Dysentery Encephaliti Enteric Fever Food Poi- Leptospirosis Typhus Viral Hep- Human Chickenpox Meningitis Leishmania- WRCD")

print(test_out)

finished = time.time()
print(finished - now, "seconds elapsed.")