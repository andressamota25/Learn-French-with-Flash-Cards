# 🇫🇷 Flashy - French Flashcard App

A simple and interactive flashcard app built with Python and Tkinter to help you learn French vocabulary!

## 📚 About the Project

Flashy is a graphical flashcard application that displays French words and flips the card after 3 seconds to show the English translation. Users can mark whether they knew the word or not, and the app will save their progress automatically—so they don’t see words they already learned!

This project was created to practice GUI programming with Tkinter, file handling, and basic data persistence with pandas.

---

## 🛠️ Features

- 🧠 Learn French vocabulary with a simple flashcard UI
- ⏱️ Automatic card flip after 3 seconds
- ✅ Mark words as known to remove them from the deck
- 💾 Saves learning progress in a CSV file
- 🎨 Custom visuals with images for a more engaging experience

---

## 📌 What I Used

- Python
- Tkinter
- pandas
- CSV file for data storage

---

## 📂 File Structure

Flashy/
├── data/
│ ├── french_words.csv # Original vocabulary dataset
│ └── words_to_learn.csv # Progress-tracking file (generated after first run)
├── images/
│ ├── card_front.png # Front of the flashcard
│ ├── card_back.png # Back of the flashcard
│ ├── right.png # "I knew this" button
│ └── wrong.png # "I didn’t know this" button
├── main.py # Main application script
└── README.md # Project documentation



