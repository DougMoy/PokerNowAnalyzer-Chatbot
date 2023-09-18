import os
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY

loader = PyPDFLoader("FinalSource.pdf")
pages = loader.load_and_split()


chunks = pages

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(chunks, embeddings)

chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")


def cleanPlayerStats(playerStats, playerName):
    filtered_stats = {}
    relevant_stats = [
        'PFR', 'VPIP', '3BET%', 'FOLD TO 3BET AFTER RAISING%',
        'FLOP CBET%', 'FOLD TO FLOP CBET%', 'AF', 'WTSD',
        'W$SD', 'WWSF'
    ]

    for stat in relevant_stats:
        if stat in playerStats:
            filtered_stats[stat] = playerStats[stat]
    query = ("Generate a strategy for me to play against this player in 5-7 sentences, make sure to not just list statistics but give a strategy for " + playerName +
             "Given their stats and include their full name in your response:" + str(filtered_stats))
    return askQuestion(query)


def askQuestion(query):
    docs = db.similarity_search(query)

    return (chain.run(input_documents=docs, question=query))
