# Cookbook-AI
# Recipe Generator

An Electron-based desktop application that leverages Google's Generative AI to create delicious recipes based on available ingredients.

## Overview

This cross-platform desktop application combines the power of Google's Gemini AI with a user-friendly interface to help users discover new recipes based on ingredients they have on hand. By integrating Python's AI capabilities with Electron's desktop application framework, Recipe Generator provides an intuitive way to get cooking inspiration.

## Features

- **Ingredient-Based Recipe Generation**: Enter the ingredients you have, and get customized recipes
- **Meal Type Filtering**: Specify breakfast, lunch, dinner, or snack recipes
- **Cuisine Selection**: Choose from various cuisine types (Italian, Mexican, Indian, etc.)
- **Specific Dish Requests**: Optionally request a specific dish using your ingredients
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Technologies Used

- **Electron.js**: Cross-platform desktop application framework
- **Node.js**: JavaScript runtime for the backend
- **Python**: Handles AI integration and recipe generation
- **Google Generative AI (Gemini)**: Provides intelligent recipe recommendations
- **HTML/CSS/JavaScript**: Frontend interface and styling

## Installation

### Prerequisites
- Node.js and npm
- Python 3.6+ 
- Google Generative AI Python package

### Setup
1. Clone the repository
```
git clone https://github.com/srithwak/recipe-generator.git
cd recipe-generator
```

2. Install Node.js dependencies
```
npm install
```

3. Install Python dependencies
```
pip install google-generativeai
```

4. Add your API key from Gemini
```
touch API_KEY.txt
```

5. Start the application
```
npm start
```

## How It Works

1. User inputs ingredients and preferences through the Electron interface
2. The application securely passes this data from the frontend to the Node.js backend using Electron's IPC mechanism
3. Node.js spawns a Python child process to interact with Google's Generative AI API
4. The AI generates a recipe based on the provided inputs
5. The recipe is returned through the same communication channels and displayed to the user

## Architecture

The application follows a modular architecture:
- **Main Process** (main.js): Handles application lifecycle and IPC
- **Renderer Process** (renderer.js): Manages the user interface
- **Preload Script** (preload.js): Provides a secure bridge between processes
- **Python Backend** (recipe_bot.py): Interfaces with the Gemini AI API

## Future Enhancements

- Save favorite recipes
- Export recipes to PDF
- Dietary restriction filters
- Ingredient substitution suggestions
- Meal planning functionality

## License

MIT
