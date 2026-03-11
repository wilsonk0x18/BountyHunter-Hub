<h1 align="center">BountyHunter Hub</h1>

<p align="center">
A collection of Python-based tools designed to assist with <b>web reconnaissance</b>, <b>OSINT</b>, and <b>bug bounty learning</b>.  
This toolkit combines several small scripts into a single GUI launcher for easier experimentation and automation.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Interface-Tkinter-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Focus-Recon_&_OSINT-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Project-Type_Beginner_Toolkit-purple?style=for-the-badge"/>
</p>

---

## Overview

BountyHunter Hub is a small toolkit of Python utilities built while learning bug bounty workflows and security automation.

Instead of running separate scripts individually, the project provides a **single graphical interface** that launches multiple recon and OSINT tools.

The project focuses on:

- web reconnaissance
- endpoint discovery
- username OSINT
- custom wordlist generation
- automated Google dork searches

This project is primarily intended as a **learning environment** for understanding how common bug bounty recon tasks can be automated with Python.

---

## Project Structure
BountyHunter-Hub-main/
- KramersEnumerator.py
- KramersIDORBrute.py
- KramersKrawler.py
- KramersPasswordKollaboration.py
- Kramers_Tool_Box.py
- main.py

---

## How the Project Works

### GUI Launcher

The main interface is built with **Tkinter** and acts as a simple launcher for the different scripts.

The GUI is organized into tabs for:

- Web Security
- OSINT
- File Creators
- Google Dorking Auto Run

This makes it easy to switch between different utility types without needing to open each Python file separately.

---

## Included Tools

<table>
<tr>
<th align="left">Tool</th>
<th align="left">Purpose</th>
</tr>

<tr>
<td>KramersEnumerator.py</td>
<td>Enumerates potential subdomains and checks if they return successful responses</td>
</tr>

<tr>
<td>KramersIDORBrute.py</td>
<td>Replaces placeholders in URLs using a wordlist to test endpoint variations</td>
</tr>

<tr>
<td>KramersKrawler.py</td>
<td>Checks a username across multiple social media platforms</td>
</tr>

<tr>
<td>KramersPasswordKollaboration.py</td>
<td>Generates custom password wordlists based on known information</td>
</tr>

<tr>
<td>Kramers_Tool_Box.py</td>
<td>Main Tkinter GUI used to launch the toolkit</td>
</tr>

<tr>
<td>main.py</td>
<td>Basic HTTP response checker for testing websites</td>
</tr>

</table>

---

## Tool Descriptions

### Subdomain Enumerator

This script checks possible subdomains against a target domain and identifies which ones return valid responses.

Example usage:
api.example.com
admin.example.com
dev.example.com

The script reports which hosts respond successfully.

---

### IDOR / URL Brute Script

This script replaces a `!LIST!` placeholder in a URL with entries from a wordlist.

Example:
example.com/user/!LIST!


The script then checks which generated URLs return valid responses.

This helps demonstrate how object references and endpoints can sometimes be discovered.

---

### Username OSINT Tool

The username search script checks whether a username exists across several platforms.

Current checks include:

- TikTok
- YouTube
- Reddit
- Instagram
- Pinterest

This is useful for simple username reuse investigations.

---

### Password Wordlist Generator

This script collects personal details about a target and generates combinations to build a custom wordlist.

Examples of inputs:

- first name
- last name
- birth date
- pet names
- favorite numbers
- special words

This demonstrates how predictable passwords can sometimes be constructed from personal information.

---

### Google Dork Automation

The GUI includes buttons that automatically open Google searches such as:

- login pages
- admin panels
- configuration files
- SQL files
- PDFs
- directory listings
- log files

These searches can help speed up reconnaissance workflows during learning exercises.

---

## Technologies Used

<table>
<tr>
<th align="left">Technology</th>
<th align="left">Purpose</th>
</tr>

<tr>
<td>Python</td>
<td>Main programming language</td>
</tr>

<tr>
<td>Tkinter</td>
<td>Desktop graphical interface</td>
</tr>

<tr>
<td>Requests</td>
<td>HTTP requests and response checks</td>
</tr>

<tr>
<td>BeautifulSoup</td>
<td>HTML parsing and page analysis</td>
</tr>

<tr>
<td>concurrent.futures</td>
<td>Threading support for faster requests</td>
</tr>

<tr>
<td>webbrowser</td>
<td>Launches Google dork searches automatically</td>
</tr>

</table>

---

## Setup

### Install Python Dependencies
pip install requests beautifulsoup4

---

### Launch the Toolkit

Run the main GUI launcher:
python Kramers_Tool_Box.py

This will open the graphical interface where all tools can be launched.

---

## Legal Notice

This toolkit is intended for **educational purposes and authorized security testing only**.

Do not use these tools against systems you do not own or do not have explicit permission to test.

Unauthorized scanning or testing may violate laws and terms of service.

Always follow responsible security practices.
