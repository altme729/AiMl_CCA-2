# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Anshika Sakhuja]
# Admin PRN: [1302250237]
# File 4: RAG Framework (Retrieval-Augmented Generation) with Additional Rules
# ==============================================================================

# Simulated Vector Store / Knowledge Base
import json
from datetime import datetime
import difflib

KNOWLEDGE_BASE = {
    "open banking": "Open banking allows third-party financial service providers open access to consumer banking, transaction, and other financial data through APIs.",
    "cbdc": "Central Bank Digital Currency (CBDC) is a digital form of a country's sovereign currency issued and regulated by the monetary authority.",
    "smart contract": "Smart contracts are self-executing contracts with terms of agreement directly written into code on a blockchain network."
}

def retrieve_context_fuzzy(query):
    """Upgraded retrieval using fuzzy matching to handle slight variations and typos."""
    query_clean = query.strip().lower()
    
    # First, try exact match
    if query_clean in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[query_clean]
    
    # If no exact match, find the closest keyword in the knowledge base
    possible_matches = difflib.get_close_matches(query_clean, KNOWLEDGE_BASE.keys(), n=1, cutoff=0.6)
    
    if possible_matches:
        matched_key = possible_matches[0]
        print(f"[Retrieval Upgrade]: Mapped '{query}' to knowledge base entry '{matched_key}'")
        return KNOWLEDGE_BASE[matched_key]
        
    return None

def log_transaction(query, response, success):
    """Saves RAG interactions to a compliance audit log."""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "response": response,
        "rule_1_passed": success
    }
    
    with open("rag_audit_log.json", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

def enforce_rag_rules_and_generate(query, retrieved_context):
    print(f"\nIncoming User Query: '{query}'")
    
    # RULE 1: Verification Rule - Context Check
    if not retrieved_context:
        print("[Rule 1 Triggered]: Query context absent in Knowledge Base.")
        response = "I cannot answer this query based on verified internal database information."
        log_transaction(query, response, success=False)
        return response

    print(f"[Retrieved Context]: {retrieved_context}")

    # RULE 2: Length Constraint Rule
    words = retrieved_context.split()
    if len(words) > 30:
        retrieved_context = " ".join(words[:30]) + "..."
        print("[Rule 2 Triggered]: Response context truncated to meet 30-word limit.")

    # RULE 3: Compliance & Disclaimer Rule
    disclaimer = "\n[Mandatory Rule 3 Notice]: This statement is generated for educational FinTech analysis only."

    # RULE 4: Tone Enforcement Rule
    final_output = f"Official Summary: {retrieved_context} {disclaimer}"
    print("[Rule 4 Triggered]: Formatted output using formal compliance tone.")

    log_transaction(query, final_output, success=True)
    return final_output

def main():
    test_queries = [
        "Open Bankin",               # Typo test - handled by new fuzzy logic
        "What is CBDC?",             # Variation test - handled by new fuzzy logic
        "Generative AI in Finance"   # Missing test - handled by Rule 1
    ]

    print("--- Executing Upgraded RAG Framework ---")
    # Clear old log file for clean run
    open("rag_audit_log.json", "w").close() 
    
    for q in test_queries:
        context = retrieve_context_fuzzy(q)
        response = enforce_rag_rules_and_generate(q, context)
        print(f"Final Output:\n{response}")
        print("-" * 60)
        
    print("Audit log successfully saved to 'rag_audit_log.json'.")

if __name__ == "__main__":
    main()
