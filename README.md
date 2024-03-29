# Song_Title_Generator
It is a simple application that generates a number of random words in English and then searches for recordings' titles that contain these words. The user can specify the number of random words to be used. It is based on Random Words API and "MusicBrainz" API.

# Instructions (Command line)
1. Clone or fork this public repository from main branch to get a local copy of this code.
2. Run main.py with your Python 3 interpreter in the prefered command line.
3. When a question appears on your command line, enter a number between 5 and 20 (inclusively). This will specify the number of random words to pull from Random Word API.
4. If an error appears when communicating with either of the APIs, you can enter 'y', 'Y', 'yes' or 'Yes' to try again or anything else to exit the program.

# Instructions (Tkinter)
1. Clone or fork this public repository from main branch to get a local copy of this code.
2. Run gui.py with your Python 3 interpreter in the prefered command line.
3. In the top right corner, you can enter a number between 5 and 20 (inclusively). This will specify the number of random words to pull from Random Word API.
4. To see the results, click the button "Generate words and search" in the middle of the window.

# Notes:
- This code was developed using Python 3.7.4 and MacOS 11.6 Big Sur. The code does not use any external libraries (if running in command line) and does not need to be compiled. To run the version with user interface, make sure you have Tkinter library installed.
- You must have internet connection to use this application.