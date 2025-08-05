# Generative AI Hands-on
A beginner-friendly repository to get started with various Generative AI models through different APIs. This repository contains interactive Jupyter notebooks & python scripts demonstrating the usage of popular Gen AI services for text and image generation.

## Prerequisites

- Python 3.13
- API keys:
  - Google AI Studio (Gemini)
  - Azure AI Foundry
  - GROQ
  - Hugging Face

## Setup
1. **Clone this repository:**
```
git clone https://github.com/yourusername/Gen-AI-Hands-on.git
cd Gen-AI-Hands-on
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
GOOGLE_API_KEY=your_google_api_key
AZURE_API_KEY=your_azure_api_key
GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
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

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. We also plan to add more examples.