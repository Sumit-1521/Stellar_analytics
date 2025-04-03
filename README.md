# 🌌 Stellar Analytics

🚀 A web-based analytics platform for analyzing exoplanet datasets to assess habitability potential. This project consists of a **React frontend** and a **Flask backend**, where users can interact with data via a dashboard.

---

## 📌 Overview

This project focuses on analyzing exoplanet datasets to assess their habitability potential. The analysis includes data cleaning, handling missing values, calculating astrophysical parameters, and developing indices like the Earth Similarity Index (ESI) and Habitability Index (HI). The results provide insights into the potential habitability of exoplanets based on scientifically rigorous methods.

---

## 📌 Features

### **🔹 Data Science Features**

✅ **Data Cleaning & Preprocessing**: Handles missing values using astrophysical formulas.
✅ **Earth Similarity Index (ESI) Calculation**: Determines how similar exoplanets are to Earth.
✅ **Habitability Index (HI) Computation**: Ranks planets based on habitability criteria.
✅ **Classification System**: Categorizes planets into Habitable, Marginally Habitable, and Non-Habitable.
✅ **Visualizations**: Heatmaps, scatter plots, and ranking charts for insights.

### **🔹 Web Dashboard Features**

✅ **Interactive UI**: Users can explore habitability metrics using a modern dashboard.
✅ **Dynamic Graphs**: View real-time ESI & HI calculations with data visualizations.
✅ **Upload Dataset**: Users can upload new exoplanet datasets for analysis.
✅ **Two-Part Web System**:

- A **React.js frontend** for UI visualization.
- A **Flask backend** for handling data processing & API requests.

---

## 🚀 How to Run the Project

This project consists of **two parts**:
1️⃣ **Flask Backend** (API & Machine Learning processing)
2️⃣ **React Frontend** (Dashboard & Visualization)

### **🔹 Step 1: Clone the Repository**

```sh
git clone https://github.com/your-username/Stellar_Analytics.git
cd Stellar_Analytics
```

### **🔹 Step 2: Set Up the Flask Backend**

1️⃣ Navigate to the backend folder:

```sh
cd backend
```

2️⃣ Install Python dependencies:

```sh
pip install -r requirements.txt
```

3️⃣ Run the Flask server:

```sh
python app.py
```

🔹 The API will start on **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**.

---

### **🔹 Step 3: Set Up the React Frontend**

1️⃣ Open a new terminal and navigate to the frontend folder:

```sh
cd ../frontend
```

2️⃣ Install Node.js dependencies:

```sh
npm install
```

3️⃣ Start the React app:

```sh
npm start
```

🔹 The React app will start on **[http://localhost:3000/](http://localhost:3000/)**.

### **Handling Different Localhost Ports**

Since React (`localhost:3000`) and Flask (`localhost:5000`) run on different ports, update the **frontend API calls** to match the backend:

- Open `frontend/src/config.js`
- Set API URL: `const API_URL = "http://127.0.0.1:5000";`
- Ensure `CORS` is enabled in Flask (`from flask_cors import CORS; CORS(app)`).

---


## 📢 Contributing

Pull requests are welcome! If you find a bug or have an improvement suggestion, feel free to open an issue.

---

## 🔗 Contact

📧 Email: **[sumitkumarsheoran89@gmail.com](mailto\:sumitkumarsheoran89@gmail.com)**\
📌 GitHub: **[your-username](https://github.com/your-username)**

🚀 **Enjoy Exploring the Universe!** 🌠

