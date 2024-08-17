from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.document_loaders import PyPDFLoader

# 接続文字列の定義
CONNECTION_STRING = "postgresql+psycopg2://postgres:postgres@localhost/pgvector_db"

# Embeddingsの定義
embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1")

# PostgreSQLの定義
db = PGVector(connection_string=CONNECTION_STRING, embedding_function=embeddings)

# PDFファイルをDBに追加
loader = PyPDFLoader(r"../data/データサイエンティスト.pdf")
pages = loader.load_and_split()
db.add_documents(documents=pages)
