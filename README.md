# Clash of Clans Farming Bot

## 📌 Project Goals

This project is focused on developing an intelligent, image-based automation bot to farm **Coins** and **Elixir** efficiently in both the **Main Base** and **Builder Base** of Clash of Clans. The bot operates through screen detection, decision-making algorithms, and error recovery mechanisms to ensure 24/7 efficient farming with minimal detection risk.


(The project is still under development. I am currently busy, and although I had time to work on it earlier, I had to take a break due to medical issues. I will resume work on the project as soon as my semester ends.)

## 🎯 Objectives

- ✅ **Automate Resource Farming**  
  Target Gold and Elixir farming by scanning bases and deploying troops when favorable loot is detected.

- ✅ **Support Both Bases**  
  The bot supports the **Main Village** and **Builder Base**, switching between them intelligently to optimize farming cycles.

- ✅ **Image Detection-Based Logic**  
  Uses image detection to:
  - Identify loot availability
  - Evaluate enemy base defenses
  - Handle training screen and base layouts
  - Deploy troops at strategic points

- ✅ **Error Handling**  
  Detects and handles:
  - Network issues
  - Connection popups
  - App crashes or freezes
  - Unexpected interruptions (e.g., maintenance, login screen)

- ✅ **Anti-Detection Measures**  
  Implements techniques to mimic human-like interactions:
  - Randomized tap positions
  - Varying delays
  - Avoids repetitive patterns
  - Simulates idle time between attacks

- ✅ **Efficiency Optimization**  
  Currently achieving **~300 million coins in 5–6 hours**. Aim is to:
  - Improve target base detection accuracy
  - Reduce downtime between attacks
  - Enhance troop deployment strategy
  - Streamline resource collection

## ⚙️ Technologies Used

- `Python` with `PyAutoGUI`, `OpenCV`, `NumPy`
- Android Emulator (Bluestacks, Nox, LDPlayer)
- ADB (Android Debug Bridge) for reliable device interaction

## 🚧 Future Improvements

- [ ] Reinforcement learning to dynamically adapt attack strategies
- [ ] Machine learning-based loot value prediction
- [ ] Smarter handling of time-limited events and obstacles
- [ ] GUI to monitor and configure farming strategies in real-time
- [ ] Log system for performance tracking and analytics

## 📈 Current Performance

| Metric             | Value                    |
|--------------------|--------------------------|
| Coins per 6 hours  | ~300 million             |
| Elixir per 6 hours | Consistent with Coins    |
| Bot Uptime         | ~70% uptime              |
| Detection Risk     | Minimal (human-like taps)|

---

## 🧠 Developer Notes

> This is a work in progress. I am currently focused on improving image recognition accuracy, optimizing bot efficiency, and implementing robust fail-safes. Exams may slow progress temporarily, but improvements are ongoing.

---

## ⭐️ Community

If you find this project useful or interesting, please consider **starring the repository**. Your support helps motivation and future development.

