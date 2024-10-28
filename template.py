import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s : %(lineno)s : %(message)s ]"
)


Project_Name = "finance-bot"

list_of_files =[
    "dataset/test.csv",
    "notebook-experiment/Finance-Chatbot.ipynb",
    f"src/{Project_Name}/__init__.py",
    f"src/{Project_Name}/components/__init__.py",
    f"src/{Project_Name}/components/data_ingestion.py",
    f"src/{Project_Name}/components/data_validation.py",
    f"src/{Project_Name}/components/data_preprocessing.py",
    f"src/{Project_Name}/components/vector_embeddings.py",
    f"src/{Project_Name}/components/llm_model.py",
    f"src/{Project_Name}/components/prompt.py",
    f"src/{Project_Name}/pipeline/__init__.py",
    f"src/{Project_Name}/pipeline/llm_pipeline.py",
    "static/style.css",
    "app.py",
    "interface.py",
    "setup.py",
    "requirements.txt",
    ".env",
    ".env.example"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

