# AIUB Notice Scraper & Telegram Alert Bot

An automated Python-based web scraper that monitors the **AIUB notice board**, checks the latest notices for predefined keywords, and sends matching notice titles to a Telegram bot.

The project uses **GitHub Actions** to run the scraper automatically every 5 minutes and maintains a persistent record of previously detected notices to prevent duplicate notifications. It is also configured to run as a web application on **Render**.

## Features

* Scrapes the first page of the AIUB notice board.
* Checks notice titles against predefined keywords.
* Sends matching new notices to a Telegram bot.
* Prevents duplicate notifications using a persistent `seen_notices.txt` file.
* Runs automatically every 5 minutes using GitHub Actions.
* Automatically commits and pushes updated notice history to GitHub.
* Uses environment variables for sensitive Telegram credentials.
* Can be hosted as a web application on Render.

## How It Works

The application follows this process:

```text
AIUB Notice Board
        │
        ▼
   Python Scraper
        │
        ▼
Extract Notice Titles
        │
        ▼
Check Keywords
        │
        ▼
Check seen_notices.txt
        │
        ├── Already seen → Ignore
        │
        └── New match
                │
                ▼
        Send Telegram Alert
                │
                ▼
       Add to seen_notices.txt
                │
                ▼
       GitHub Actions commits
       and pushes the updated file
```

### Keyword Matching

The scraper currently monitors for the following keywords:

```python
allowed_texts = ['exam','schedule']
```

A notice is considered a match when all configured keywords are present in its title.

## Technologies Used

* **Python**
* **Requests** – HTTP requests and Telegram API communication
* **BeautifulSoup** – HTML parsing and notice extraction
* **python-dotenv** – Environment variable management
* **Telegram Bot API** – Notification delivery
* **GitHub Actions** – Automated execution every 5 minutes
* **Git/GitHub** – Persistent storage of processed notices
* **Render** – Web application hosting

## Project Structure

```text
Web-Scrapper-Using-Python/
│
├── .github/
│   └── workflows/
│       └── ...
│
├── .gitignore
├── README.md
├── ScrapperBot.py
├── keep_alive.py
├── requirements.txt
└── seen_notices.txt
```

### Important Files

**`ScrapperBot.py`**

Contains the main scraping, keyword matching, duplicate detection, and Telegram notification logic.

**`seen_notices.txt`**

Stores the titles of previously processed matching notices. This prevents the same notice from generating repeated Telegram notifications.

**`keep_alive.py`**

Contains the components used to keep the application running when deployed as a web application.

**`requirements.txt`**

Contains the Python dependencies required by the project.

**`.github/workflows/`**

Contains the GitHub Actions workflow responsible for automatically running the scraper.

## GitHub Actions Automation

The scraper is scheduled to run every 5 minutes using GitHub Actions:

```yaml
on:
  schedule:
    - cron: "*/5 * * * *"
```

During each execution, GitHub Actions:

1. Checks out the repository.
2. Sets up Python 3.10.
3. Installs the required dependencies.
4. Runs `ScrapperBot.py`.
5. Checks whether `seen_notices.txt` was modified.
6. Commits the updated file if a new notice was detected.
7. Pushes the change back to the repository.

This allows the repository itself to act as persistent storage for the scraper's processed-notice history.

## Environment Variables

The project uses environment variables for sensitive credentials.

Required variables:

```text
TELEGRAM_TOKEN
MY_CHAT_ID
USERNAME
```

These values should **not** be hard-coded or committed to the repository.

For GitHub Actions, the values are stored using **GitHub Secrets**.

For local development or Render, configure the corresponding environment variables through the platform's environment-variable settings.

## Telegram Notifications

When a new notice matches the configured keywords, the scraper sends the notice title through the Telegram Bot API.

For example:

```text
New matching AIUB notice title
```

Only notices that have not previously been recorded in `seen_notices.txt` trigger a notification.

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/averagedude05/Web-Scrapper-Using-Python.git
cd Web-Scrapper-Using-Python
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
MY_CHAT_ID=your_telegram_chat_id
USERNAME=your_username
```

Do not commit the `.env` file to GitHub.

### 4. Run the scraper

```bash
python ScrapperBot.py
```

The scraper will check the AIUB notice board and send a Telegram notification when it finds a new matching notice.

## Deployment

### GitHub Actions

GitHub Actions is used for the periodic scraping workflow.

The workflow automatically executes every 5 minutes and updates `seen_notices.txt` when a new matching notice is found.

### Render

The project is also configured to run as a web application on Render using the project's keep-alive/web-server component.

Render environment variables should be configured for:

```text
TELEGRAM_TOKEN
MY_CHAT_ID
USERNAME
```

## Duplicate Detection

Duplicate notifications are avoided through `seen_notices.txt`.

When a matching notice is found:

```text
1. Read the notice title.
2. Check whether the title already exists in seen_notices.txt.
3. If it exists, ignore the notice.
4. If it does not exist, send the Telegram notification.
5. Add the title to seen_notices.txt.
6. GitHub Actions commits and pushes the updated file.
```

This allows future scheduled executions to recognize previously processed notices.

## Future Improvements

Possible improvements include:

* Monitoring multiple pages of the notice board.
* Supporting more flexible keyword matching.
* Storing notice URLs along with titles.
* Adding timestamps to detected notices.
* Using a database instead of a text file for persistent state.
* Adding a web dashboard for monitored notices.
* Adding multiple Telegram recipients or channels.
* Improving error handling and retry mechanisms.
* Develop a REST API to expose scraped notice data in JSON format for programmatic access.
