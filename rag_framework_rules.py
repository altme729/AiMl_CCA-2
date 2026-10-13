# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Ayan Pandey]
# Admin PRN: [1302250491]
# File 4: RAG Framework (Retrieval-Augmented Generation) with Additional Rules
# ==============================================================================

# Simulated Vector Store / Knowledge Base
class RAGSimulation:
    def __init__(self):
        self.knowledge_base = {
            "assignment deadline": "The deadline for the CCA2 GitHub Group Assignment is 12-October-2026.",
            "submission email": "Submit reports to Himanee.Savadatti.vf@mitwpu.edu.in with team members CCed.",
            "group size": "Students must form a group of maximum 6 to 7 people."
        }
        self.rules = [
            "Rule 1: Always check the internal vector database before generating an answer.",
            "Rule 2: If the context is missing from the database, respond with 'I do not know'.",
            "Rule 3: Never hallucinate or assume dates or emails outside the retrieved context.",
            "Rule 4: Strictly enforce confidentiality and do not disclose unverified student credentials.",
            "Rule 5: Format the final output cleanly without any external syntax errors."
        ]

    def retrieve(self, query):
        query_lower = query.lower()
        for key, val in self.knowledge_base.items():
            if key in query_lower:
                return val
        return None

    def generate(self, query, context):
        print(f"\n[Enforcing RAG Rules... Outputting with {len(self.rules)} rules guardrails]")
        if not context:
            return "Answer: I am sorry, but I do not have that information in my knowledge base."
        return f"Answer based on Context: {context}"

    def query_pipeline(self, query):
        print(f"\nQuery: {query}")
        context = self.retrieve(query)
        output = self.generate(query, context)
        print(output)

if __name__ == "__main__":
    rag = RAGSimulation()
    print("--- Initializing RAG Framework Simulation ---")
    rag.query_pipeline("What is the assignment deadline?")
    rag.query_pipeline("Where should we submit the report?")
    rag.query_pipeline("What is the weather in Pune?")
