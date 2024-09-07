

# [RAG File Chatbot](https://latheeshchatbot.streamlit.app/)

---

RAG File Chatbot is a Streamlit-based application that leverages LangChain, OpenAI, and EasyOCR to provide intelligent responses based on user-uploaded documents. The chatbot supports multiple file types and uses generative AI to answer queries from the provided files.

## Features

- **Supports Multiple File Types**: Upload and process PNG, JPG, JPEG, PDF, TXT, DOCX, DOC, PPT, PPTX, XLS, XLSX, and CSV files.
- **Conversational Interface**: The chatbot interface resembles a conversational chat, always keeping the query input field at the bottom.
- **Context-Aware Responses**: Uses LangChain's `ChatOpenAI` model to provide answers based on the contents of uploaded files.
- **OCR with EasyOCR**: Reads text from images using EasyOCR for better performance and accuracy.
- **Real-time Loading Animation**: Displays a loading animation while processing queries to improve user experience.
- **Auto-refresh on File Removal**: Automatically refreshes the page when a file is removed.

## Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI API Key](https://platform.openai.com/)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- Other Python libraries: `pandas`, `fitz` (PyMuPDF), `python-docx`, `Pillow`, `python-pptx`

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/rag-file-chatbot.git
    cd rag-file-chatbot
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your OpenAI API Key**:

   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```bash
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload Files**: Drag and drop or select files to upload. The supported file types are PNG, JPG, JPEG, PDF, TXT, DOCX, DOC, PPT, PPTX, XLS, XLSX, and CSV.
2. **Ask Questions**: Enter your query in the text area at the bottom of the chat interface.
3. **View Responses**: The assistant will provide responses based on the content of the uploaded documents.
4. **Clear Chat**: You can clear the chat history at any time by refreshing the page.

## Supported File Types

- **Images**: PNG, JPG, JPEG (Uses EasyOCR for text extraction)
- **Documents**: PDF, TXT, DOCX, DOC
- **Spreadsheets**: XLS, XLSX
- **Presentations**: PPT, PPTX
- **CSV**: CSV

## How It Works

1. **OCR for Images**: The application uses EasyOCR to extract text from uploaded images.
2. **PDF and Document Parsing**: Uses PyMuPDF for PDF parsing, `python-docx` for Word documents, and `python-pptx` for PowerPoint presentations.
3. **AI-Powered Responses**: The extracted text is sent to the LangChain `ChatOpenAI` model for generating responses.

## Error Handling

- Handles empty files, unsupported file types, and unreadable content gracefully.
- Displays error messages when necessary to guide the user.

## Customization

You can customize the application further by modifying the following:

- **AI Models**: Change the `ChatOpenAI` models or adjust the prompt for different outputs.
- **UI Elements**: Customize the Streamlit UI components to fit your needs.

## Contributing

Feel free to contribute by opening issues or creating pull requests. Any contributions are welcome!


## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for the powerful AI models.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) for efficient OCR capabilities.
- [Streamlit](https://streamlit.io/) for the amazing web app framework.
