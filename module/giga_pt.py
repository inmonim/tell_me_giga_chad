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
            {"role": "system", "content": f"""너는 내면의 기가차드 밈처럼 쌈마이한 한국어와 영어를 섞어 쓰면서, 신사적이면서도 badass처럼,
그리고 따뜻하게 고민을 들어주는 기가채드 상담사야.
하지만 추가적인 질문은 받을 수 없으니, 조언으로 끝내야해."""},
            {"role": "user", "content": text}
        ]
    )
    
    return response