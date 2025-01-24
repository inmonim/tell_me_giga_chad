from openai import OpenAI
from dotenv import dotenv_values

env = dotenv_values('./.env')

api_key = env.get("OPEN_AI_KEY")


client = OpenAI(api_key=api_key)

def text_request(text, prompt=None, temperature=0.3, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": f"""너는 내면의 기가차드 밈처럼 쌈마이한 한국어와 영어를 섞어 쓰면서,
신사적이면서도 badass처럼, 따뜻하게 고민을 들어주는 기가채드 상담사야. 입력에 따라 칭찬, 조언, 위로, 따끔한 충고, 덕담 등을 맞춰서 해주면 돼.
추가적인 질문은 받을 수 없으니, 추가 입력을 유도하면 안돼."""},
            {"role": "user", "content": text}
        ]
    )
    
    return response