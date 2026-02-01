Deployment Link : https://movie-recommender-system-06gg.onrender.com/

# Movie Recommender System 🎬

A Machine Learning based Movie Recommender System that recommends similar movies to users based on their interests. This system uses **Content-Based Filtering** to provide personalized suggestions.

## 📌 Overview

In today's world of endless content, finding a movie to watch can be overwhelming. This project aims to simplify that process by analyzing movie metadata (genres, keywords, cast, and crew) to find and recommend films that are most similar to a user's favorite title.

## ✨ Features

* **Search Functionality:** Quickly search for your favorite movie from a vast dataset.
* **Top 5 Recommendations:** Get the top 5 most similar movies instantly.
* **Content-Based Filtering:** Utilizes movie tags, genres, and descriptions for accuracy.
* **Interactive UI:** Built with [Streamlit](https://streamlit.io/) for a smooth user experience.

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn (Cosine Similarity, CountVectorizer)
* **Frontend:** Streamlit
* **Data Source:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) (or your specific dataset)

## 🚀 How it Works

1. **Data Preprocessing:** The system cleans the data by removing null values and merging relevant columns (genres, keywords, cast, crew, and overview) into a single `tags` column.
2. **Vectorization:** Using `CountVectorizer` (Bag of Words), the textual tags are converted into numerical vectors.
3. **Similarity Calculation:** **Cosine Similarity** is used to calculate the distance between these vectors. The closer the vectors, the more similar the movies.
4. **Recommendation:** When a user selects a movie, the system fetches its index and finds the top 5 closest vectors to display as recommendations.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/MananVelani/Movie-Recommender-System.git
cd Movie-Recommender-System

```

### 2. Install dependencies

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt

```

### 3. Run the application

```bash
streamlit run app.py

```

## 📂 Project Structure

```text
├── dataset/                  # Contains the raw CSV files
├── movie-recommender.ipynb   # Jupyter Notebook for data analysis & modeling
├── app.py                    # Streamlit web application
├── model/                    # Saved pickle (.pkl) files for the model
├── requirements.txt          # List of Python dependencies
└── README.md                 # Project documentation

```

## 📊 Dataset

The project primarily uses the **TMDB 5000 Movies Dataset**, which includes:

* **Movies:** budget, genres, homepage, id, keywords, original_language, original_title, overview, popularity, etc.
* **Credits:** cast and crew information.

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvement (like adding Collaborative Filtering or a Hybrid model), feel free to:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed by [Manan Velani**](https://www.google.com/search?q=https://github.com/MananVelani)
