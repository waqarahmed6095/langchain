import os

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()


if __name__ == "__main__":
    print("Ingesting ...")
    loader = TextLoader("mediumblog1.txt", encoding="utf-8")
    documents = loader.load()
    print("splitting ...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    print(f"Ingested {len(texts)} chunks ...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    print("Ingesting to Pinecone ...")
    PineconeVectorStore.from_documents(
        texts, embeddings, index_name=os.getenv("INDEX_NAME")
    )

    print("Finished ...")
