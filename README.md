# 📦 PakCart E-Commerce Analytics Dashboard

An end-to-end business intelligence and data analytics pipeline designed to evaluate retail operations, supply chain performance, and financial metrics for a regional e-commerce marketplace (Daraz-style framework).

## 🚀 Live Application
* **Local instance:** Running successfully on `http://localhost:8501`
* **Production Status:** Ready for Cloud Deployment (Streamlit Community Cloud / Hugging Face Spaces)

## 📌 Project Overview & Maqsad (Objective)
The principal objective of this project is to model a complete production-grade data ecosystem for an e-commerce infrastructure. It transitions messy, high-dimensional operational logs into interactive business vectors, allowing management executives to audit financial leakage, optimize product placement, and evaluate regional performance.

### Key Analytical Pillars:
1. **Financial Revenue Audit:** Separating operational load from absolute financial realization by isolating net delivered revenues against operational leaks.
2. **Supply Chain Integrity:** Tracking structural cancellations (**14.30% baseline**) to help management prevent packaging and logistics cost overheads.
3. **Market Demographics Matrix:** Geographically mapping multi-million transactions across major urban clusters (Karachi, Lahore, Islamabad, Rawalpindi, Faisalabad) to allocate localized marketing spend.
4. **Inventory Configuration:** Parsing cross-categorical distributions (Electronics, Clothing, Groceries, Beauty, Home Decor) to steer warehouse stock schedules.

## ⚙️ Technical Architecture & Stack
* **Core Data Pipeline:** Python (Pandas & NumPy) utilized for programmatic data simulation, feature engineering, and automated structural data cleaning (`fillna` mitigation frameworks).
* **Data Warehouse Layer:** **SQLite Database System** integrated directly via Python's native relational SQL engines. All metric aggregations, filtering channels, and data extractions are calculated using raw database queries rather than basic out-of-memory array modifications.
* **Interactive Business Intelligence Layout:** Built using **Streamlit** for advanced client interaction and interactive grid controls.
* **Data Visualization Component:** Powered by **Plotly Express** for production-grade responsive analytical chart modules.

## 📊 Core SQL Optimization Examples
To demonstrate data engineering proficiency, the analytical framework executes automated structural queries on the backend:
* **Dynamic KPI Card Resolution:**
  ```sql
  SELECT SUM(Total_Amount_PKR) FROM orders WHERE Status = 'Delivered';
  ```
* **Geographical Revenue Segmentation:**
  ```sql
  SELECT City, SUM(Total_Amount_PKR) as Revenue 
  FROM orders 
  WHERE Status = 'Delivered' 
  GROUP BY City 
  ORDER BY Revenue DESC;
  ```

## 📂 Repository Structure
```text
├── app.py               # Main application pipeline (ETL + SQL Engine + Dashboard Layout)
├── requirements.txt     # Python production environment package dependencies
└── README.md            # Extensive technical and business documentation
```

## 🛠️ Installation & Execution

### Prerequisites
Ensure you have Python 3.8+ deployed on your local workstation.

### Local Setup Steps
1. Clone the codebase structure:
   ```bash
   git clone https://github.com
   cd PakCart-Analytics
   ```
2. Setup and activate structural environment constraints (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Ingest required architectural library instances:
   ```bash
   pip install -r requirements.txt
   ```
4. Fire the operational local development server matrix:
   ```bash
   streamlit run app.py
   ```
