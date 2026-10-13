# ==============================================================================
# Course: SY BCom FinTech | Subject: AI ML 1 - CCA2
# Admin Name: [Yukta Kulkarni]
# Admin PRN: [1302250198]
# File 4: RAG Framework (Retrieval-Augmented Generation) with Additional Rules
# ==============================================================================

# Simulated Vector Store / Knowledge Base
class FinTechRAG:
    def __init__(self):
        # Updated rules focusing on tax, equity, and e-commerce
        self.rules_database = {
            "TAX_01": "Section 80C: Deductions on investments up to INR 1.5 Lakhs are allowed for specific mutual funds (ELSS).",
            "TAX_02": "LTCG Equity: Long Term Capital Gains on equity mutual funds exceeding INR 1 Lakh are taxed at 10% without indexation.",
            "GST_01": "E-Commerce: Handcrafted home decor items and concrete products typically attract a GST slab of 12% to 18% depending on the material.",
            "CORP_01": "Corporate Finance: Startups registered under DPIIT can claim a tax holiday for 3 consecutive years."
        }
        
    def retrieve_context(self, query):
        """Find rules that match the keywords in the query."""
        keywords = query.lower().split()
        matched_rules = []
        
        for rule_id, rule_text in self.rules_database.items():
            # If any keyword from the query is in the rule
            if any(word in rule_text.lower() for word in keywords):
                matched_rules.append(f"[{rule_id}] {rule_text}")
                
        return matched_rules

    def generate_answer(self, query):
        """Simulate the generation phase of RAG."""
        print(f"User Query: '{query}'")
        context = self.retrieve_context(query)
        
        if not context:
            return "RAG Output: I could not find specific rules regarding this query in the database.\n"
            
        combined_context = "\n".join(context)
        return (
            f"RAG Output: Based on the retrieved financial rules, here is the context:\n"
            f"{combined_context}\n"
            f"Ensure your corporate filings comply with the above directives.\n"
        )

if __name__ == "__main__":
    bot = FinTechRAG()
    
    # Test queries
    q1 = "What are the rules for equity mutual funds and LTCG?"
    print(bot.generate_answer(q1))
    
    q2 = "Tell me about GST on handcrafted home decor."
    print(bot.generate_answer(q2))
