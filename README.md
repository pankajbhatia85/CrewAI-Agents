# CrewAI for Agentic AI

This repository demonstrates the use of **CrewAI** for implementing an Agentic AI workflow. The project is built in Python 3.11.9 and uses OpenAI embeddings for query handling and email generation. It includes a multi-agent process for managing PDF files, chunking, embedding, and query handling with fallback mechanisms. 

---

## Features

1. **PDF Upload and Processing**
   - The first agent allows users to upload a PDF file. ** [example_home_inspection.pdf](https://github.com/user-attachments/files/18613507/example_home_inspection.pdf)

   - CrewAI's PDF tool is used to chunk and embed the document using OpenAI embeddings.

2. **ChromaDB Storage**
   - The embeddings are stored in ChromaDB by default for efficient query retrieval.

3. **Query Handling with Fallback**
   - Queries are first served by the PDF tool based on the stored embeddings.

4. **Email Generation**
   - A second agent automatically generates an email based on the processed query and response.

---

## Requirements

1. **API Keys**:
   - Obtain your API keys for:
     - OpenAI: [OpenAI API Key](https://platform.openai.com/)
     
2. **Dependencies**:
   - All required Python dependencies are listed in the `requirements.txt` file. Install them with:
     ```bash
     pip install -r requirements.txt
     ```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crewai-agentic-ai.git
   cd crewai-agentic-ai
   ```

2. Set up your environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Add your API keys:
   - Create a `.env` file in the root of the project and include the following keys:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     SERPER_API_KEY=your_serper_api_key
     ```

---

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Upload a PDF**:
   - Use the interface to upload a PDF file for processing.

3. **Query the PDF**:
   - Input your query. The agent will:
     - Retrieve answers from the embedded PDF using ChromaDB. [example_home_inspection.pdf](https://github.com/user-attachments/files/18613507/example_home_inspection.pdf)
     - Fallback to the Serper API if the query cannot be resolved by the PDF tool.

4. **Email Generation**:
   - The final response will be converted into an email format by the third agent.

---

## Project Structure

```
crewai-agentic-ai/
├── app.py                # Main application logic
├── requirements.txt      # Python dependencies
├── .env                  # API keys (not included in repo)
├── README.md             # Documentation
└── utils/                # Helper functions and utilities
    ├── pdf_processing.py # PDF chunking and embedding
    ├── query_handler.py  # Query handling logic
    └── email_agent.py    # Email generation logic
```

---

## Technologies Used

- **Python 3.11.9**
- **CrewAI** for Agentic AI workflows
- **OpenAI API** for embeddings
- **ChromaDB** for embedding storage and retrieval

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Support

If you encounter any issues or have questions, feel free to open an issue or contact the maintainer.

---

Happy Coding!
