import importlib

packages = {
    'python-dotenv': 'dotenv',
    'requests': 'requests',
    'numpy': 'numpy',
    'pandas': 'pandas',
    'scipy': 'scipy',
    'pytorch': 'torch',
    'jupyterlab': 'jupyterlab',
    'ipywidgets': 'ipywidgets',
    'matplotlib': 'matplotlib',
    'scikit-learn': 'sklearn',
    'chromadb': 'chromadb',
    'jupyter-dash': 'jupyter_dash',
    'sentencepiece': 'sentencepiece',
    'pyarrow': 'pyarrow',
    'faiss-cpu': 'faiss',
    'beautifulsoup4': 'bs4',
    'plotly': 'plotly',
    'bitsandbytes': 'bitsandbytes',
    'transformers': 'transformers',
    'sentence-transformers': 'sentence_transformers',
    'datasets': 'datasets',
    'accelerate': 'accelerate',
    'openai': 'openai',
    'anthropic': 'anthropic',
    'google-generativeai': 'google.generativeai',
    'gradio': 'gradio',
    'gensim': 'gensim',
    'modal': 'modal',
    'ollama': 'ollama',
    'psutil': 'psutil',
    'setuptools': 'setuptools',
    'speedtest-cli': 'speedtest',
    'langchain': 'langchain',
    'langchain-core': 'langchain',
    'langchain-text-splitters': 'langchain.text_splitter',
    'langchain-openai': 'langchain.llms.openai',
    'langchain-chroma': 'langchain.vectorstores.chroma',
    'langchain-community': 'langchain',
    'feedparser': 'feedparser',
    'twilio': 'twilio',
    'pydub': 'pydub',
}

for pkg_name, import_name in packages.items():
    try:
        importlib.import_module(import_name)
        print(f"Successfully imported {import_name} ({pkg_name})")
    except ImportError:
        print(f"Failed to import {import_name} ({pkg_name})")