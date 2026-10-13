# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Shravan Sagale]
# Admin PRN: [1302250620]
# File 4: RAG Framework (Retrieval-Augmented Generation) with Additional Rules
# ==============================================================================

# Simulated Vector Store / Knowledge Base
KNOWLEDGE_BASE = {
    "open banking": "Open banking allows third-party financial service providers open access to consumer banking, transaction, and other financial data through APIs.",
    "cbdc": "Central Bank Digital Currency (CBDC) is a digital form of a country's sovereign currency issued and regulated by the monetary authority.",
    "smart contract": "Smart contracts are self-executing contracts with terms of agreement directly written into code on a blockchain network."
}

def retrieve_context(query):
    """Simulates Context Retrieval from database."""
    query_clean = query.strip().lower()
    return KNOWLEDGE_BASE.get(query_clean, None)

def enforce_rag_rules_and_generate(query, retrieved_context):
    """
    Applies custom business and generation rules to simulate a RAG system.
    """
    print(f"\nIncoming User Query: '{query}'")
    
    # RULE 1: Verification Rule - Context Check
    if not retrieved_context:
        print("[Rule 1 Triggered]: Query context absent in Knowledge Base.")
        return "I cannot answer this query based on verified internal database information."

    print(f"[Retrieved Context]: {retrieved_context}")

    # RULE 2: Length Constraint Rule (Limit response length)
    words = retrieved_context.split()
    if len(words) > 30:
        retrieved_context = " ".join(words[:30]) + "..."
        print("[Rule 2 Triggered]: Response context truncated to meet 30-word limit.")

    # RULE 3: Compliance & Disclaimer Rule
    disclaimer = "\n[Mandatory Rule 3 Notice]: This statement is generated for educational FinTech analysis only."

    # RULE 4: Tone Enforcement Rule (Formal response wrapper)
    final_output = f"Official Summary: {retrieved_context} {disclaimer}"
    print("[Rule 4 Triggered]: Formatted output using formal compliance tone.")

    return final_output

def main():
    test_queries = [
        "Open Banking",
        "CBDC",
        "Generative AI in Finance"  # Intentionally missing query to test Rule 1
    ]

    print("--- Executing RAG Framework with Enforced Business Rules ---")
    for q in test_queries:
        context = retrieve_context(q)
        response = enforce_rag_rules_and_generate(q, context)
        print(f"Final Output:\n{response}")
        print("-" * 60)

if __name__ == "__main__":
    main()
