# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Shlok Shirke]
# Admin PRN: [1302250028]
# File 4: RAG Framework (Retrieval-Augmented Generation) with Additional Rules
# ==============================================================================

# Simulated Vector Store / Knowledge Base
class FinancialRAGSystem:

  def __init__(self):
    # Knowledge base / Vector database mock documents with added compliance rules
    self.knowledge_base = {
        "Rule_101": (
            "RBI Guidelines: All digital lending apps must provide a clear Key"
            " Fact Statement (KFS) to borrowers before executing loan"
            " agreements."
        ),
        "Rule_102": (
            "Data Privacy: Financial institutions must encrypt customer"
            " transaction logs using AES-256 standards at rest and in transit."
        ),
        "Rule_103": (
            "AML Compliance: Any cash deposit or digital transfer exceeding"
            " INR 10,00,000 must trigger an automatic Suspicious Transaction"
            " Report (STR)."
        ),
        "Rule_104": (
            "Consumer Protection: E-commerce and fintech platforms must process"
            " customer refunds within 5-7 working days of cancellation."
        ),
    }

  def retrieve_documents(self, query):
    """Retrieval step: Fetch relevant rules based on keyword matching."""
    relevant_docs = []
    query_terms = query.lower().split()
    for rule_id, content in self.knowledge_base.items():
      if any(term in content.lower() for term in query_terms):
        relevant_docs.append((rule_id, content))
    return relevant_docs

  def generate_response(self, query):
    """Generation step: Combine retrieved rules to formulate an answer."""
    retrieved = self.retrieve_documents(query)

    print(f"Query: '{query}'")
    print(f"Retrieved {len(retrieved)} relevant regulatory rule(s).\n")

    if not retrieved:
      return (
          "Generated Response: No specific regulatory rule found matching"
          " your query."
      )

    context_str = "\n".join([f"- [{rid}]: {doc}" for rid, doc in retrieved])
    response = (
        f"Generated Response based on RAG Retrieval:\n"
        f"Based on current compliance standards, here are the applicable"
        f" directives:\n{context_str}"
    )
    return response


if __name__ == "__main__":
  rag = FinancialRAGSystem()

  # Test query triggering compliance rules
  sample_query = "What are the data privacy and digital lending loan agreement rules?"
  print(rag.generate_response(sample_query))
