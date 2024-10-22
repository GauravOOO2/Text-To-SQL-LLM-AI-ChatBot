
# 🧠 AI Chatbot with Gemini LLM, LangChain, SQL, and Streamlit

This project is an AI-powered chatbot application built using **Google's Gemini LLM**, **LangChain**, **ChromaDB**, and **Streamlit**. The chatbot is specifically designed to retrieve answers based solely on a local SQL database of students' records. This ensures that the bot doesn't generate random or hallucinated answers but provides SQL query-based responses strictly from the dataset.

## 📝 Project Overview

This chatbot is a data retrieval tool that leverages **Google Gemini's Language Model (LLM)**, allowing it to convert natural language questions into SQL queries. The queries are then run against a local SQLite database, and the results are returned to the user via a simple and intuitive **Streamlit** UI. **LangChain** is used as part of the backend to help integrate the LLM and the SQL query generation process.

The core idea behind this project is to have a reliable, data-constrained chatbot that will **only answer based on the data available in the database**—it does not generate responses that are not tied to the underlying database. This makes it particularly useful for scenarios where data accuracy and consistency are paramount.

## 🌟 Key Features

1. **Gemini LLM Integration**: The app uses Google's Gemini LLM to process user inputs and convert them into SQL queries dynamically.
2. **SQL Query Generation**: The bot is capable of transforming user questions into precise SQL queries that retrieve the necessary information from the `STUDENT` table in an SQLite database.
3. **Data Accuracy**: The chatbot restricts its answers to the information available in the `student.db` SQLite database, preventing random responses.
4. **Streamlit UI**: A user-friendly interface built with **Streamlit** allows users to input queries and get responses directly from the chatbot.
5. **LangChain**: Leveraged to build a seamless pipeline between the language model and the database query execution.
6. **SQLite Database**: The data is stored in a local `SQLite` database (`student.db`), containing information about students such as their name, class, section, and marks.
7. **Prompt-Based AI**: The chatbot uses a well-defined prompt to guide its behavior, ensuring SQL query generation adheres to the defined schema of the database.

## ⚙️ Technologies Used

- **Google Gemini LLM**: A language model that processes user queries and generates responses.
- **LangChain**: Used to build robust LLM-powered applications that connect the language model to the database.
- **ChromaDB**: An optional component that helps manage and store embeddings or vectorized data (currently not fully utilized in this version but can be expanded).
- **SQLite**: A lightweight SQL database to store the student data.
- **Streamlit**: A Python framework to build interactive and user-friendly web apps.
- **Python**: Backend and core logic.

## 🛠️ Setup Instructions

To run this project locally or on a cloud platform like Render, follow the steps below.

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo-url/chatbot-sql-gemini.git
cd chatbot-sql-gemini
```

### 2. Install Dependencies

Make sure you have **Python 3.8+** installed. Then, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project directory and add your **Google API key** for Gemini LLM:

```
GOOGLE_API_KEY=your-google-api-key
```

### 4. Initialize the SQLite Database

You can either create the SQLite database (`student.db`) manually, or you can run the `sql.py` script to set up the database with sample student records.

To create the database with predefined student data:

```bash
python sql.py
```

### 5. Run the Streamlit Application

Run the Streamlit app locally using the following command:

```bash
streamlit run app.py
```

### 6. Deploy on Render

If deploying on Render, ensure you:

1. Set the start command as `streamlit run app.py`.
2. Include the `Procfile` in the root of your project with the following content:

```
web: streamlit run app.py
```

3. Configure the environment variable `GOOGLE_API_KEY` in the Render dashboard.

## 💻 Project Structure

```
.
├── app.py                # Main Streamlit app
├── sql.py                # Script to initialize SQLite database with sample student data
├── student.db            # SQLite database (optional, can be generated dynamically)
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (not included in repo)
├── Procfile              # Start command for Render deployment
└── README.md             # Project documentation (this file)
```

### File Descriptions

- **`app.py`**: Contains the main logic for the Streamlit web app, including user input handling, invoking the Gemini LLM, and displaying the SQL query results.
- **`sql.py`**: Initializes an SQLite database with student records, creating the table and populating it with data.
- **`student.db`**: The SQLite database where student data is stored. It contains the table `STUDENT` with columns for name, class, section, and marks.
- **`requirements.txt`**: Lists the Python packages required to run the project (Streamlit, google-generativeai, LangChain, etc.).

## 🔍 How It Works

1. **User Query Input**: The user enters a natural language question in the Streamlit app.
2. **LLM Processing**: The Gemini LLM takes the user question and converts it into an SQL query based on the pre-defined prompt.
3. **SQL Query Execution**: The SQL query is executed against the local SQLite database (`student.db`).
4. **Response**: The chatbot displays the query result as the response to the user. The bot **only retrieves and responds with data present in the `STUDENT` table** and does not generate any other information.

### Example Queries:
- **User**: *"Tell me all students studying in AI & ML class?"*
- **Bot**: *SELECT * FROM STUDENT WHERE CLASS='AI & ML';*
  
  **Response**: `Emily Davis, Michael Brown`

- **User**: *"How many students are there in total?"*
- **Bot**: *SELECT COUNT(*) FROM STUDENT;*
  
  **Response**: `10`

## 🚀 Future Enhancements

- **Expand Dataset**: Include more detailed data fields (e.g., grades, attendance, etc.) to make the chatbot more informative.
- **ChromaDB Integration**: Fully integrate ChromaDB for better vector search and embedding management, expanding the bot's ability to understand queries beyond simple SQL.
- **Enhanced UI**: Improve the frontend design with additional features like charts and visual data representations.
- **Error Handling**: Add more robust error handling for invalid or out-of-scope queries.

## 🧑‍💻 Contributing

Contributions are welcome! If you'd like to improve this project or add new features, feel free to open a pull request.

1. Fork the project.
2. Create a new feature branch.
3. Submit a pull request detailing your changes.

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
