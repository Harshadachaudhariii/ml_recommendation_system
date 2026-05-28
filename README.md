## Movie Recommendation System

## Problem Statement
With thousands of movies available across streaming platforms, users frequently face "choice paralysis," spending more time scrolling through endless lists than actually watching content. Traditional recommendation engines often rely heavily on user rating histories (collaborative filtering), which fails for new users with no past data (the cold-start problem). Additionally, relying on heavy cloud infrastructure or expensive proprietary APIs to process basic text relationships introduces unnecessary costs and operational complexity for simple content matching.

## Solution Proposed
This Movie Recommendation System solves this problem by delivering a fast, privacy-focused, content-based recommendation engine that runs entirely locally. By analyzing textual features such as genres and plot overviews, the system maps movies into a high-dimensional vector space to find the most visually and contextually similar titles instantly. It features a lightweight, responsive Streamlit user interface coupled with real-time dynamic poster fetching via the TMDB API, giving users a seamless, interactive discovery dashboard without requiring complex cloud databases or user tracking.

## Tech Stack Used
1. Python
2. Streamlit
3. Scikit-Learn (CountVectorizer & Cosine Similarity)
4. Pandas
5. Pickle
6. Requests (TMDB API Integration)

## Infrastructure Required
1. Docker
2. GitHub Actions

## How to Run

Step 1. Clone the Repository
Clone the repository from GitHub to your local machine:
```bash
git clone [https://github.com/Harshadachaudhariii/ml_recommendation_system.git](https://github.com/Harshadachaudhariii/ml_recommendation_system.git)
cd ml_recommendation_system

```

Step 2. Create a Virtual Environment

```bash
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

```

Step 3. Install the Requirements

```bash
python -m pip install -r requirements.txt

```

Step 4. Configure Environment Variables

Create a `.env` file in your root workspace to securely store your TMDB API credentials. Use the following baseline parameters:

```env
TMDB_API_KEY=your_tmdb_api_key_here

```

Step 5. Start the Application

Run the Streamlit frontend application locally:

```bash
streamlit run app.py

```


## Run Locally (Docker)

1. Check if the `Dockerfile` and `docker-compose.yml` are available in the project directory.
2. Build and launch the containerized application stack from the project root directory:

```bash
docker compose up -d --build

```

## Access Application

* **Frontend (Streamlit Dashboard):** `http://localhost:8501`

## Conclusion

This Movie Recommendation System provides a high-performance, cost-free, and deployment-ready architecture for text-based content mapping. By compiling complex natural language features into a pre-computed local similarity matrix, the application delivers instantaneous recommendations with zero runtime model overhead. Packaged inside Docker and integrated with automated GitHub Actions, the project demonstrates a robust production blueprint for deploying isolated, lightweight machine learning interfaces.

