# 🎓 Smart Attendance System

> Final Year Major Project — B.Tech Computer Science, JNCT Rewa (2024)

A real-time **face recognition based attendance system** built with Python, OpenCV, and Firebase. The system detects student faces via webcam, matches them against stored encodings, and automatically logs attendance to a cloud database — eliminating manual roll calls entirely.

---

## 🚀 Features

- **Real-Time Face Detection**
  - Detects and recognizes student faces live via webcam
  - Uses `face_recognition` library for accurate face matching

- **Automated Attendance Logging**
  - Marks attendance automatically when a face is recognized
  - Prevents duplicate entries using a 30-second cooldown per student

- **Firebase Cloud Integration**
  - Student data stored in Firebase Realtime Database
  - Student photos stored in Firebase Cloud Storage

- **Interactive UI**
  - Custom background interface built with OpenCV and cvzone
  - Displays student info (name, ID, major, year, attendance count) on recognition
  - Multiple UI modes: Loading → Info Display → Already Marked

- **Face Encoding Pipeline**
  - Encodes known student faces and saves to a pickle file for fast matching
  - Auto-uploads student images to Firebase Storage during encoding

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Face Recognition | OpenCV, face_recognition, cvzone |
| Database | Firebase Realtime Database |
| Storage | Firebase Cloud Storage |
| UI | OpenCV with custom background overlay |
| Data | Pickle (face encodings), NumPy |

---

## 📂 Project Structure

```
smart-attendance-system/
├── main.py                  # Main app — webcam capture, face matching, UI
├── EncodeGenerator.py       # Encodes student faces and uploads to Firebase
├── AddDataToDatabase.py     # Seeds student data into Firebase
├── encodeFile.p             # Saved face encodings (generated)
├── Images/                  # Student photos (named by student ID)
├── Resources/
│   ├── background.png       # UI background
│   └── Modes/               # UI mode images (loading, info, already marked)
└── serviceAccountKey.json   # Firebase credentials (NOT uploaded to GitHub)
```

---

## ⚙️ How It Works

**Step 1 — Add student data**
```bash
python AddDataToDatabase.py
```
Seeds student records (name, major, year, attendance count) into Firebase.

**Step 2 — Generate face encodings**
```bash
python EncodeGenerator.py
```
Reads photos from `Images/` folder, generates face encodings, saves to `encodeFile.p` and uploads images to Firebase Storage.

**Step 3 — Run the system**
```bash
python main.py
```
Opens webcam, detects faces in real time, matches against known encodings and logs attendance to Firebase automatically.

---

## 🔒 Security Note

`serviceAccountKey.json` contains Firebase credentials and is **excluded from this repository**.
To run this project, generate your own Firebase service account key from:
> Firebase Console → Project Settings → Service Accounts → Generate New Private Key

---

## 📊 How Attendance is Marked

1. Webcam captures live frame
2. Frame is resized and converted for face detection
3. Detected face encodings are compared against stored encodings
4. On match — student info is fetched from Firebase
5. If last attendance was **more than 30 seconds ago** → attendance is marked ✅
6. If **less than 30 seconds** → "Already Marked" mode is shown ❌
7. Student info and photo are displayed on screen for confirmation

---

## 🖥️ Prerequisites

```
pip install opencv-python
pip install face_recognition
pip install cvzone
pip install firebase-admin
pip install numpy
```

---

## 📜 License

This project is licensed under the MIT License.
