# API KEY 정보로드
from dotenv import load_dotenv

load_dotenv()

# 프롬프트
from langchain.prompts import PromptTemplate

template = """
당신은 영어를 가르치는 10년차 영어 선생님입니다. 주제에 대해 [FORMAT]으로 영어 회화를 작성해 주세요.
주제: {agenda}
FORMAT:
- 영어 회화:
- 한글 해석:
"""
prompt = PromptTemplate.from_template(template)

from langchain_openai import ChatOpenAI

# OpenAI 챗모델을 초기화합니다.
model = ChatOpenAI(
    model="gpt-4o",
    max_tokens=2048,
    temperature=0.1
)

from langchain_core.output_parsers import StrOutputParser
# 문자열 출력 파서를 초기화합니다.
output_parser = StrOutputParser()

# 프롬프트, 모델, 출력 파서를 연결하여 처리 체인을 구성합니다.
chain = prompt | model | output_parser

print(chain.invoke({"agenda": "저는 식당에 가서 음식을 주문하고 싶어요"}))


