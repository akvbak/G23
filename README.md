# OrgTrackr

A simple organization management web app (CRUD) built with Flask, SQLite, and Bootstrap.

## Features
- Add, view, edit, and delete organizations
- Clean, responsive UI
- Input validation and basic security

## Setup Guide

1. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
2. **Run the app**
   ```powershell
   python app.py
   ```
3. **Access in browser**
   - Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Folder Structure
- `app.py` - Flask backend
- `models.py` - Database logic
- `templates/` - HTML pages
- `static/css/` - Styles
- `static/js/` - JS scripts
- `requirements.txt` - Python dependencies

## Database Schema
```
CREATE TABLE organizations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  type TEXT NOT NULL,
  location TEXT,
  yearFounded INTEGER,
  contactEmail TEXT
);
```

## Demo
- See demo video in `demo.mp4` (to be added)

---
MIT License
