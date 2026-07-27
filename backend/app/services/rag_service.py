from app.services.retriever_service import get_retriever
from app.services.llm_service import get_llm

from app.prompts.rag_prompts import rag_prompt



def format_documents(docs):

    context = ""

    for doc in docs:

        context += (
            f"\n\nSource: {doc.metadata.get('filename')}"
            f"\nPage: {doc.metadata.get('page')}"
            f"\n\n{doc.page_content}"
        )

    return context



def ask_question(question: str):


    retriever = get_retriever(
        k=5
    )


    docs = retriever.invoke(
        question
    )



    context = format_documents(
        docs
    )



    prompt = rag_prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )



    llm = get_llm()

    response = llm.invoke(
        prompt
    )


    return {
        "answer": response.content,
        "sources": [
            doc.metadata
            for doc in docs
        ]
    }