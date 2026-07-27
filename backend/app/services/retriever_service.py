from langchain_core.documents import Document

from app.vectorstore.chroma import get_vectorstore


def retrieve_with_scores(query: str,k: int = 5):
    vectorstore = get_vectorstore()

    return vectorstore.similarity_search_with_score(
        query,
        k=k
    )

def get_retriever(k: int = 5):

    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": 50,
            "lambda_mult": 0.7
        }
    )

    return retriever