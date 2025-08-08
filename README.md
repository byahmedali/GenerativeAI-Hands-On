# Generative AI Hands-on
A beginner-friendly repository to get started with various Generative AI models through different APIs in Python. This repository contains interactive Jupyter notebooks & Python scripts demonstrating the usage of popular Gen AI services for text and image generation.

## Prerequisites
- Python 3.13
- API keys:
  - [Google AI Studio (Gemini)](https://aistudio.google.com/)
  - [Azure AI Foundry](https://ai.azure.com/)
  - [GROQ](https://console.groq.com/keys)
  - [Hugging Face](https://huggingface.co/settings/tokens)

## Setup
1. **Clone this repository:**
```
git clone https://github.com/byahmedali/GenerativeAI-Hands-On.git
cd GenerativeAI-Hands-On
```

2. **Create and activate a virtual environment:**
```
py -3.13 -m venv venv
# On Windows
.\venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate
```

3. **Install dependencies:**
```
pip install -r requirements.txt
```

4. **Create a `.env` file in the root directory and add your API keys:**
```
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
HF_TOKEN=your_huggingface_api_key
AZURE_OPENAI_API_KEY=your_azure_api_key
```

#### If you are going to run notebooks in Jupyter
5. **Add your virtual environment to Jupyter as a new kernel:**
```
python -m ipykernel install --user --name=venv --display-name "GenAI Hands-on"
```

6. **Launch the local Jupyter Notebook server, and make sure to open & run notebooks using `GenAI Hands-on` kernel:**
```
jupyter notebook
```

## Available Notebooks
- [Azure AI Foundry](./notebooks/Azure%20AI%20Foundry%20API.ipynb)
- [Google AI Studio](./notebooks/Google%20AI%20Studio%20API.ipynb)
- [GROQ](./notebooks/GROQ%20API.ipynb)
- [Hugging Face](./notebooks/Hugging%20Face%20API.ipynb)
- [Ollama](./notebooks/Ollama%20Local%20Models.ipynb)

## Available Scripts
- [LangChain Chatbot (Gemini)](./scripts/LangChain%20Chatbot%20(Gemini).py)
- [Text to Image (Azure AI)](./scripts/Text%20to%20Image%20(Azure%20AI).py)

## Available User-Interfaces
- [Groq Chatbot (Chainlit)](./interfaces/Groq%20Chatbot%20(Chainlit).py)
- [Groq Chatbot (Streamlit)](./interfaces/Groq%20Chatbot%20(Streamlit).py)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. We also plan to add more examples.