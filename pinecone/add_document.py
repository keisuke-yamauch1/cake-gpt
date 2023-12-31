import json
import logging
import os

import pinecone
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone

load_dotenv()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def initialize_vectorstore():
    pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment=os.environ["PINECONE_ENV"],
    )

    index_name = os.environ["PINECONE_INDEX"]

    if index_name in pinecone.list_indexes():
        pinecone.delete_index(index_name)

    pinecone.create_index(name=index_name, metric="cosine", dimension=1536)

    embeddings = OpenAIEmbeddings()
    return Pinecone.from_existing_index(index_name, embeddings)


def save_to_pinecone(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    vectorstore = initialize_vectorstore()
    try:
        vectorstore.add_documents(docs)
    except Exception as e:
        logger.error(f"Failed to add documents to Pinecone: {e}")
        return


if __name__ == "__main__":
    save_to_pinecone("data/sample.json")