from transformers import AutoTokenizer, pipeline
import torch
# import 01-streamlit as st
from utils import read_json


# @st.cache(allow_output_mutation=True)
def get_pipeline():
    device: int = 0 if torch.cuda.is_available() else -1

    model_path: str = '/Users/yangjaeug/Desktop/GitHub/Product-Serving/assets/comments_task/model.pt'
    config_path: str = '/Users/yangjaeug/Desktop/GitHub/Product-Serving/practice/03-streamlit-fastapi/app/config.json'

    model = torch.load(model_path, map_location=torch.device('cpu'))
    model_config = read_json(config_path)

    tokenizer = AutoTokenizer.from_pretrained('beomi/KcELECTRA-base')

    pipe = pipeline(
        task="text-classification",
        config=model_config,
        model=model.model,
        tokenizer=tokenizer,
        device=device
    )
    
    return pipe

def inference(comments, pipe):
    results = []
    
    for comment in comments:
        try:
            output = pipe(comment)
        except:
            continue
    
        if output[0]['label'] == 'none':
            continue
    
        else:
            results.append(
                {
                    'comment': comment,
                    'label': output[0]['label'],
                    'score': output[0]['score']
                }
            )
    
    return results