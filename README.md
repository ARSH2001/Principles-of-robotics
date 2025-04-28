# Principles of Robotics - Spring 1401 🚀

[![Made With](https://img.shields.io/badge/Made%20with-Python%2C%20Webots-blue)]()
[![University](https://img.shields.io/badge/University-IUT-orange)]()

---
## 📚 Table of Contents

- [About The Repository](#about-the-repository)
- [Homework 02 - AIUT Robotics Toolbox](#homework-02---aiut-robotics-toolbox)
- [Homework 03 - Webots Simulation](#homework-03---webots-simulation)
- [Final Project - Line Follower Robot](#final-project---line-follower-robot)
  - [Hardware Implementation](#hardware-implementation)
  - [Simulation](#simulation)
- [How to Use](#how-to-use)

---

## 📖 About The Repository

This repository contains my projects and homework for the **Principles of Robotics** course at **Isfahan University of Technology (Spring 1401)**.  
It showcases practical applications of robotics principles using Python, Webots, and microcontroller programming.

---

## 🛠 Homework 02 - AIUT Robotics Toolbox

- A Jupyter Notebook exercise focused on the **AIUT_RoboticsToolbox** in Python.
- Covers basic robotics concepts like forward/inverse kinematics and simple simulations using the toolbox.

---

## 🤖 Homework 03 - Webots Simulation

- Robot modeling, design, and simulation using the **Webots** platform.
- Basic robots are created and controlled inside a simulated environment.

---

## 🚗 Final Project - Line Follower Robot

### 🔩 Hardware Implementation

The final project involves designing and building a **line follower robot** using the following components:

| Component                         | Quantity/Details                        |
|------------------------------------|-----------------------------------------|
| IR Sensors                        | 17                                      |
| LCD Display                       | 2x16 characters                         |
| Microcontroller                   | Atmega32                                |
| Motors                             | 2× ZGA25RP 12V, 600 RPM                 |
| Motor Driver                      | L298N                                   |
| Op-Amps                           | 5× LM324                                |
| Push Buttons, LEDs, Capacitors, etc.| Various                                 |
| Battery and Flat Cables           | Included                                |

**Working Principle:**
- **Center sensors on the line:** Both motors spin at equal speed.
- **Left sensors detect line:** Right motor spins faster to correct path.
- **Right sensors detect line:** Left motor spins faster to adjust direction.

---

### 🖥️ Simulation

- A simplified model using **three IR sensors** (left, center, right) was simulated.
- Sensor data are compared with threshold values to adjust motor speeds in real-time.

---

> 📄 For full technical documentation, refer to the [Final Project Report (PDF)](./path/to/Line%20follower%20report%20(1).pdf).

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/ARSH2001/Principles-of-robotics.git
2. Navigate to homework folders and open Jupyter Notebook files or Webots projects.

3. Explore the final project implementation and report.
