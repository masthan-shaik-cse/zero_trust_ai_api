# Zero-Trust AI API Wrapper

A comprehensive cybersecurity framework for wrapping foundational generative models and autonomous fleet APIs, designed following the principles of Zero-Trust Architecture.

## Features
- **Defensive API Wrappers (`api/defensive_wrapper.py`)**: Sanitizes inputs and redact sensitive LLM outputs (e.g., system prompts or API keys) dynamically.
- **Cryptographic Safety (`security/crypto_audit.py`)**: Implements HMAC validation to verify the integrity of incoming requests from edge devices, and audits model weights against supply-chain attacks.
- **ZeroTrust Middleware (`middleware/zero_trust_auth.py`)**: Strict, context-aware identity verification ("Never trust, always verify") for users and agentic systems.

## Competencies Demonstrated
- Advanced Penetration Testing
- Cryptographic Safety Protocols
- Vulnerability Auditing
- Certified Ethical Hacker (CEH) Master Principles

## Usage
Wrap any LangChain or direct LLM invocation with the `DefensiveAPIWrapper` to instantly gain rate limiting and output sanitization.
