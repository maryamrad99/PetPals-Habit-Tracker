
# PetPals Habit Tracker app
A Python-Based CLI habit tracker that gamifies building habits with virtual pets. 
Each habit is paired with a pet: completing habits increases your pet’s happiness and XP, while missing habits lowers happiness and breaks streaks.


## What is it?
PetPals is a command-line application written in Python.  
- Users can create, complete, and remove habits.  
- Each habit is linked to a pet species (e.g., cat, dog).  
- Completing habits grows streaks and levels up your pet.  
- Missing habits reduces pet happiness.  
- Analytics provide insights like the **longest streak overall** or the **happiest pet**.  
- All data is saved in JSON files so that progress persists between sessions.  


## How to run +  Installation
Requirements are listed in `requirements.txt`.  

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Run the CLI app:**
   ```bash
   python3 -m petpals.cli
   ```

4.  Use the menu options to: 
   - Add a new habit with a pet
   - Complete habits to increase streaks and pet happiness
   - View streaks and analytics
   - Remove habits
   

4. **Run the test:**
   ```bash
   pytest -q
   ```
  