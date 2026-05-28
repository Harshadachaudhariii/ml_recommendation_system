# Movie Recommendation System

## Problem Statement
With thousands of movies available across streaming platforms, users frequently face "choice paralysis," spending more time scrolling through endless lists than actually watching content. Traditional recommendation engines often rely heavily on user rating histories (collaborative filtering), which fails for new users with no past data (the cold-start problem). Additionally, relying on heavy cloud infrastructure or expensive proprietary APIs to process basic text relationships introduces unnecessary costs and operational complexity for simple content matching.

## Solution Proposed
This Movie Recommendation System solves this problem by delivering a fast, privacy-focused, content-based recommendation engine that runs entirely locally. By analyzing textual features such as genres and plot overviews, the system maps movies into a high-dimensional vector space to find the most visually and contextually similar titles instantly. It features a lightweight, responsive Streamlit user interface coupled with real-time dynamic poster fetching via the TMDB API, giving users a seamless, interactive discovery dashboard without requiring complex cloud databases or user tracking.

## Tech Stack Used
1. **Python** — Core application logic.
2. **Streamlit** — Web interface and interactive dashboard.
3. **Scikit-Learn** — Text vectorization (`CountVectorizer`) and matrix calculation (`Cosine Similarity`).
4. **Pandas** — Data manipulation and preprocessing.
5. **Pickle** — Serialization of processed datasets and similarity matrices.
6. **Requests** — Live TMDB API integration for movie posters.

## Infrastructure Required
1. **Docker & Docker Compose** — Containerization and local orchestration.
2. **GitHub Actions** — Continuous Integration (CI) automation.
3. **GitHub Container Registry (GHCR)** — Cloud hosting for production Docker images.

---

## How to Run

Step 1: Clone the Repository
```bash
git clone https://github.com/Harshadachaudhariii/ml_recommendation_system.git
```
Step 2: Create and Activate a Virtual Environment

```bash
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```
Step 3: Install the Dependencies
```bash
python -m pip install -r requirements.txt
```
Step 4: Configure Environment Variables
Create a .env file in the root directory to securely store your TMDB API credentials:
```bash
TMDB_API_KEY=your_tmdb_api_key_here
```
Step 5: Start the Application
```bash
streamlit run app.py
```
## Run Containerized Production Stack (Docker Compose)
This project utilizes a fully automated CI/CD pipeline via GitHub Actions. Every push to the repository builds a production-ready container image and publishes it to the GitHub Container Registry (GHCR).

The local docker-compose.yml file is configured with volume mounting to allow the container to read heavy model assets (similarity.pkl ~762 MB) directly from your host machine directory, avoiding heavy cloud image distribution and satisfying GitHub's 100 MB file limitations.

Prerequisites
Ensure Docker Desktop is installed and running on your machine.

Ensure your local `.env` file is configured with your `TMDB_API_KEY`.

Deployment Steps
1. Pull the latest production image directly from GHCR:
```bash
docker compose pull
```
2. Launch the application stack in detached background mode:
```bash
docker compose up -d
```
Access Application http://localhost:8501 

## Conclusion
This Movie Recommendation System provides a high-performance, cost-free, and deployment-ready architecture for text-based content mapping. By compiling complex natural language features into a pre-computed local similarity matrix, the application delivers instantaneous recommendations with zero runtime model overhead. Packaged inside Docker and integrated with automated GitHub Actions, the project demonstrates a robust production blueprint for deploying isolated, lightweight machine learning interfaces.
