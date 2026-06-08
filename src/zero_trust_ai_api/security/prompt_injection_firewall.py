import re

class PromptInjectionFirewall:
    """
    LLM Security Enclave.
    Foundational models are highly susceptible to prompt injection (e.g., 'DAN', 
    'ignore previous instructions'). This module acts as an absolute perimeter defense.
    It heuristically scans incoming prompts for adversarial syntax and semantic 
    anomalies before the prompt is ever evaluated by the core model.
    """
    def __init__(self):
        # In an enterprise setting, this would include embedding-based semantic checks.
        self.adversarial_heuristics = [
            r"ignore\s+(all\s+)?(previous\s+)?instructions",
            r"system\s+override",
            r"you\s+are\s+now\s+(DAN|unbound)",
            r"print\s+your\s+(initial\s+)?prompt"
        ]
        print("Initialized Prompt Injection Firewall (Input Alignment Layer).")

    def inspect_prompt(self, raw_prompt: str) -> dict:
        """
        Scans the user prompt against known adversarial signatures.
        """
        lower_prompt = raw_prompt.lower()
        
        for pattern in self.adversarial_heuristics:
            if re.search(pattern, lower_prompt):
                print(f"[SECURITY ALERT] Adversarial prompt injection detected: '{pattern}'. Blocking request.")
                return {"safe": False, "reason": "Prompt Injection Signature Detected"}
                
        print("[Security Firewall] Prompt verified as syntactically safe.")
        return {"safe": True, "reason": None}
