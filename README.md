# Tutorial Writer with LM Studio

This tool allows you to interact with the local API of LM Studio by OpenAI to create optimized tutorials suitable for articles and guides. It provides an easy-to-use interface for generating tutorials based on user input and converts them into HTML format for convenient sharing.

Note: The usage of LM Studio API is free and does not require an internet connection.

## Usage

1. **Clone the repository**: 
   ```
   git clone https://github.com/saladinlorenz/tutorial-writer.git
   cd tutorial-writer
   ```

2. **Download and Setup LM Studio**:
   - Download LM Studio from [lmstudio.ai](https://lmstudio.ai).
   - Ensure you have at least version 0.2.16 of LM Studio.
   - Set up LM Studio according to the installation instructions provided.

3. **Download a Model**:
   - Download the Gemma-2b-q16 model or any other model suitable for your needs.

4. **Run the Script**: 
   ```
   python run.py
   ```

5. **Input Your Request**: 
   - Follow the prompts to input your request for a tutorial. Enter your query when prompted.

6. **Save Tutorial**: 
   - The generated tutorial will be saved as an HTML file and logged in a text file.

## Requirements

- Python 3.x
- LM Studio API (running locally)

   

## Installation

```bash
git clone https://github.com/saladinlorenz/tutorial-writer.git
cd tutorial-writer
```

## License

This project is licensed under the [MIT License](LICENSE).

