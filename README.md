Introduction

The Inventory Management System with Intelligent Agent is a web-based application developed to help businesses efficiently monitor stock levels and make informed restocking decisions. Traditional inventory systems rely heavily on manual checks and fixed thresholds, which often lead to overstocking or stock shortages.

This project enhances conventional inventory management by integrating a simple intelligent agent that introduces automated decision-making. The agent continuously analyzes inventory levels and recommends optimal restocking quantities when stock levels fall below a predefined minimum threshold.

The system is designed to be lightweight, scalable, and suitable for educational as well as small-scale commercial use.

🎯 Problem Statement

Many small and medium businesses still manage inventory using:

Manual stock tracking

Spreadsheet-based systems

Static restocking rules

These approaches often cause:

Delayed restocking

Frequent stockouts

Overstocking

Human errors in judgment

There is a need for a system that can automatically analyze stock levels and assist in decision-making, reducing manual intervention.

💡 Proposed Solution

This project proposes a web-based inventory management system integrated with an intelligent restocking agent.

Key Idea:

Instead of relying on fixed manual inputs, the system introduces logic-based intelligence to recommend restocking quantities dynamically.

The intelligent agent:

Monitors inventory levels

Compares them against minimum thresholds

Automatically suggests restocking quantities when needed

This approach brings automation and intelligence into inventory operations.

🧠 Intelligent Agent Logic

The intelligent agent follows a simple yet effective rule-based decision-making strategy:

Decision Rule:
If current_quantity < minimum_threshold
→ recommended_restock = 2 × minimum_threshold

Benefits of This Approach:

Prevents frequent restocking

Reduces risk of stock shortages

Minimizes manual intervention

Demonstrates intelligent system behavior

Although simple, this logic closely reflects real-world inventory replenishment strategies used in practice.

✨ Features

📋 View all inventory items

➕ Add new inventory items

⚠️ Automatic low-stock detection

🤖 Intelligent restocking recommendations

📊 Stock status indicators (Healthy / Low Stock)

🖥️ Clean and responsive user interface

🗄️ Persistent data storage using SQLite

🏗️ System Architecture

The system follows a modular architecture, separating concerns for better maintainability.

Architecture Components:

Frontend: HTML, CSS, Jinja2 templates

Backend: Flask (Python)

Database: SQLite

Agent Module: Decision-making logic for restocking

Data Flow:

User adds inventory items via UI

Data is stored in SQLite database

Backend fetches inventory data

Intelligent agent analyzes stock levels

Restock recommendations are generated

Results are displayed on the UI

🛠️ Technologies Used

Python 3

Flask – Backend web framework

SQLite – Lightweight relational database

HTML5 & CSS3 – Frontend UI

Jinja2 – Template rendering

Git & GitHub – Version control