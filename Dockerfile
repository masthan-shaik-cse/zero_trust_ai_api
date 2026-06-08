FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

COPY src/ ./src/
COPY config/ ./config/
COPY models/ ./models/

CMD ["python", "src/zero_trust_ai_api/main.py", "--run_all_enterprise_pipelines"]
