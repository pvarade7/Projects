# Subway Reviews Analysis (Yelp Dataset)

This project analyzes a large portion of the Yelp Open Dataset to help Subway understand why its store ratings are lagging and whether its leadership’s goals are realistic. It tests executive claims using real data and visualizations.

## 🧠 Business Problem
Subway’s CEO wants the company-wide average rating raised to **4.5 / 5**, but current performance is much lower. Executives claim:
- Ratings are naturally improving  
- All sandwich chains suffer low ratings  
- Only local restaurants can reach 4.5  
- Online ratings are unreliable  

This project evaluates whether each claim is supported by data.

---

## 📊 Dataset & Tools
- Datasets (ignored in GitHub):
  - `reviews.csv` — ~400k reviews
  - `restaurants.csv` — ~2k restaurants  
- Stack:
  - Python 3  
  - `pandas`, `matplotlib`  
  - Jupyter Notebook (`subway.ipynb`)

---

## 🔍 Key Insights
- Subway’s average rating is **~2.6**, far below the 4.5 target.
- Competitors like **Jersey Mike’s (~3.3)** perform much better → not an industry issue.
- Ratings are **not** improving over time.
- Local restaurants and small chains average **~4.0**, showing high ratings *are* achievable at smaller scale.
- Online reviews include many 2–4 star ratings → not only extremes.

---

## 🧭 How to Run the Notebook

```bash
git clone https://github.com/pvarade7/Projects.git
cd Projects/subway_assignment
pip install pandas matplotlib jupyter
jupyter notebook subway.ipynb
A
