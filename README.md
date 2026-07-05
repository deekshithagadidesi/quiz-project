<div align="center">

# ⚡ Circuit Check

### A daily electrical units quiz, wired straight into your browser.

![Made with JavaScript](https://img.shields.io/badge/Made%20with-JavaScript-f7df1e?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Logic%20origin-Python-3776ab?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-e34f26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572b6?style=for-the-badge&logo=css3&logoColor=white)
![Status](https://img.shields.io/badge/status-live-4fd6b0?style=for-the-badge)

</div>

---

## 🔌 What is this?

**Circuit Check** is a lightweight, no-backend quiz game that tests your knowledge of **electrical and SI units** — ohms, watts, henries, farads, and more.

Every day, a fresh set of **5 questions** is pulled from a growing question bank — same questions for everyone that day, new ones tomorrow. No server, no database, no sign-up. Just open it and play.

---

## ⚙️ Features

| ⚡ | Feature |
|---|---|
| 🔁 | **Daily rotation** — a new set of 5 questions every day, automatically |
| 🎯 | **Instant feedback** — see right/wrong answers as you go |
| 📊 | **Score tracking** — end screen shows your score + a verdict |
| 🎨 | **Circuit-board themed UI** — dark mode, copper accents, schematic grid background |
| 📱 | **Responsive** — works on desktop and mobile |
| 🧩 | **Zero dependencies** — pure HTML, CSS & JavaScript, runs in any browser |

---

## 🚀 Try it locally

```bash
git clone https://github.com/your-username/circuit-check.git
cd circuit-check
```

Then just open `quiz.html` in your browser — or use the **Live Server** extension in VS Code for auto-reload while editing.

---

## 🧠 How the daily rotation works

```
today's date  →  seed number  →  shuffle question bank  →  pick first 5
```

The date (e.g. `20260705`) seeds a repeatable shuffle of the question bank, so:
- 🟢 Everyone sees the **same 5 questions** on the same day
- 🔵 A **different 5** appear automatically the next day
- 🚫 No database or server needed — it's all calculated in-browser

---

## 🐍 Where it started

The quiz logic — looping through questions, checking answers, tracking score — was **first built and tested in Python** as a console program. This repo is that same logic **ported to JavaScript** so it can run live in a browser as a shareable website.

```
Python (console)  →  same logic rewritten  →  JavaScript (browser)
```

Browsers can't run Python natively, so JavaScript was the necessary translation — but the core thinking (loops, conditionals, functions, data structures) is identical in both versions.

---

## 🛠️ Built with

- **Python** — where the quiz logic was first designed and tested (loops, conditionals, functions)
- **HTML** — page structure
- **CSS** — circuit-board aesthetic (grid background, copper/signal-green palette)
- **Vanilla JavaScript** — the Python logic re-implemented so it runs in the browser

---

## 📸 Preview

> *Dark schematic background · copper accent buttons · signal-green correct states*

---

## 🌱 Roadmap ideas

- [ ] Add more question categories beyond electrical units
- [ ] Leaderboard / streak tracking
- [ ] Shareable results card for socials
- [ ] Sound effects on correct/wrong

---

<div align="center">

**Built as a hands-on project to learn Python fundamentals — then extended into HTML, CSS & JavaScript to bring it to the web.**

⚡ *Test your circuits. Come back tomorrow for more.* ⚡

</div>
