# 1.文档加载与分块
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
loader = PyPDFLoader("ai_course_notes.pdf")
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
splits = text_splitter.split_documents(docs)

# 2.向量库构建
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings
embedding = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-base-zh-v1.5")
vector_db = Chroma.from_documents(documents=splits, embedding=embedding, persist_directory="./chroma_db")
retriever = vector_db.as_retriever(search_kwargs={"k":3})

# 3.RAG问答链路
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(openai_api_key="YOUR_KEY", temperature=0, model_name="gpt-3.5-turbo")
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
