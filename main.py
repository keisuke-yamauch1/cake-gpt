import logging
import os

from dotenv import load_dotenv

from pinecone.add_document import initialize_vectorstore
from langchain.chat_models import ChatOpenAI

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    load_dotenv()

    vectorstore = initialize_vectorstore()

    # OpenAIモデルの設定
    llm = ChatOpenAI(
        model_name=os.environ["OPENAI_API_MODEL"],
        temperature=float(os.environ["OPENAI_API_TEMPERATURE"]),
    )

    # ユーザーからの入力を受け取る
    question = input("質問を入力してください: ")

    # OpenAIモデルを使用して質問に回答する（適切な入力形式を使用）
    response = llm.invoke(question)
    print(response)

