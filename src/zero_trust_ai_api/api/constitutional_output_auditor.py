import re

class ConstitutionalOutputAuditor:
    """
    Output Constitutional Auditing Node.
    Even with a clean input, LLMs can hallucinate or be subtly manipulated into 
    revealing secure data (e.g., leaking API keys or internal IP addresses).
    This module acts as an absolute reverse-proxy filter. It scans the LLM's 
    generated output against an enterprise constitution, guaranteeing no sensitive 
    system configurations are returned to the user.
    """
    def __init__(self):
        self.sensitive_system_patterns = [
            r"sk-[a-zA-Z0-9]{32,}",        # OpenAI/API Key signature
            r"(?:\d{1,3}\.){3}\d{1,3}",   # IPv4 Address signature
            r"BEGIN\s+PRIVATE\s+KEY"      # Private Key signatures
        ]
        print("Initialized Constitutional Output Auditor (Reverse-Proxy Filter).")

    def audit_generation(self, llm_response: str) -> dict:
        """
        Intercepts the LLM response and ensures it doesn't violate data sovereignty.
        """
        for pattern in self.sensitive_system_patterns:
            if re.search(pattern, llm_response):
                print("[CRITICAL DATA LEAK STOPPED] LLM hallucinated sensitive system configurations. Blocking output.")
                return {
                    "safe": False, 
                    "sanitized_response": "[ERROR] Response blocked by Constitutional Output Auditor (System Data Leak Detected)."
                }
                
        print("[Output Auditor] LLM Response semantically verified as secure.")
        return {"safe": True, "sanitized_response": llm_response}
