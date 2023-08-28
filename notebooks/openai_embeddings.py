from config import key, location, endpoint

import openai
openai.api_type = "azure"
openai.api_key = key
openai.api_base = endpoint
deployment_id_ada='embedding-ada'
openai.api_key = key
openai.api_version = "2022-12-01"

def get_embeddings_azure_openai(sentence01):
    response_sentence01 = openai.Embedding.create(
    input=sentence01,
    engine=deployment_id_ada
)
    embeddings_sentence01 = response_sentence01['data'][0]['embedding']
    return embeddings_sentence01