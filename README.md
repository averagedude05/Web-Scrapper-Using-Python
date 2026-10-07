# Campus Lost & Found Management System

A web-based **Campus Lost & Found Management System** developed as an academic project for **CSC 3215: Web Technologies** at American International University-Bangladesh (AIUB).

The system provides a centralized platform for students to report lost or found items, search for possible matches, submit claims, and manage item information. Administrators can review reports, manage users, verify claims, and update item statuses.

## 📌 Project Overview

Students often rely on social media groups, messaging platforms, or informal communication to report lost belongings. These approaches can make it difficult to search for items, track reports, and verify ownership.

This project aims to provide a structured platform where:

* Users can report lost and found items.
* Found items can be searched and managed.
* Users can submit and track claims.
* Administrators can review reports and claims.
* Item statuses can be tracked throughout the recovery process.

## ✨ Features

### 🔐 Authentication & Account Management

* User registration and login
* Secure logout
* Password management
* Profile management
* Role-based access control

### 🔎 Lost Item User

* Report lost items with relevant details
* Search and browse found items
* Submit claims for matching items
* Track claim status

### 📦 Found Item User

* Report found items
* Add item name, category, date, location, description, and image
* View submitted found items
* Edit or withdraw submissions
* Update found-item information

### 👨‍💼 Admin

* Review and manage item reports
* Manage claim requests
* Approve or reject claims
* Manage user accounts
* Manage item categories
* Update item statuses

## 🛠️ Technologies Used

| Technology   | Purpose                           |
| ------------ | --------------------------------- |
| PHP          | Backend development               |
| MySQL        | Database management               |
| JavaScript   | Client-side functionality         |
| HTML5        | Page structure                    |
| CSS3         | Styling                           |
| Bootstrap    | Responsive UI                     |
| XAMPP        | Local development environment     |
| Git & GitHub | Version control and collaboration |

## 🗄️ Database

The system uses a relational **MySQL database** to manage:

* Users
* Lost items
* Found items
* Claims
* Item categories
* Item statuses
* Related system data and relationships

The database was designed with relational tables and appropriate relationships to maintain data consistency and support the application's workflows.

## 👥 Team & Contribution

This project was developed collaboratively as part of **CSC 3215: Web Technologies**.

### My Contributions

* Developed the **Found Item User** module.
* Implemented functionality for reporting and managing found-item submissions.
* Worked on editing and updating found-item information.
* Designed and implemented parts of the **MySQL database**.
* Worked on database relationships and integration with application workflows.
* Helped coordinate team responsibilities and task assignments during development.

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

* XAMPP
* PHP
* MySQL
* Git
* A web browser

### Installation

1. Clone the repository:

```bash
git clone https://github.com/averagedude05/campus-lost-found-management-system.git
```

2. Move the project folder into the XAMPP `htdocs` directory:

```text
C:\xampp\htdocs\
```

3. Start **Apache** and **MySQL** from the XAMPP Control Panel.

4. Open **phpMyAdmin** and create the required database.

5. Import the project's SQL/database file into MySQL.

6. Configure the database connection in the project if required.

7. Open the application in your browser:

```text
http://localhost/<project-folder-name>/
```

## 📂 Project Structure

```text
Campus-Lost-Found/
│
├── admin/
├── found-item-user/
├── lost-item-user/
├── assets/
├── css/
├── js/
├── images/
├── database/
└── README.md
```


