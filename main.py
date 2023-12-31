import logging
import os

from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain

from langchain.chat_models import ChatOpenAI

from my_pinecone.init import initialize_vectorstore

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

    condense_question_llm = ChatOpenAI(
        model_name=os.environ["OPENAI_API_MODEL"],
        temperature=os.environ["OPENAI_API_TEMPERATURE"],
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        condense_question_llm=condense_question_llm,
    )

    # ユーザーからの入力を受け取る
    question = input("質問を入力してください: ")

    chat_history = ""

    # 辞書形式で質問とチャットの履歴を渡す
    response = qa_chain.run({'question': question, 'chat_history': chat_history})
    print(response)



