const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('recipeAPI', {
  generateRecipe: (ingredients, mealType, dishName, cuisine) => 
    ipcRenderer.invoke('generate-recipe', { ingredients, mealType, dishName, cuisine })
});