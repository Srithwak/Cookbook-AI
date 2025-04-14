document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const loadingElement = document.getElementById('loading');
    const recipeResult = document.getElementById('recipe-result');

    loadingElement.style.display = 'none';

    generateBtn.addEventListener('click', async () => {
        const ingredients = document.getElementById('ingredients').value.trim();
        const mealType = document.getElementById('meal-type').value;
        const dishName = document.getElementById('dish-name').value.trim();
        const cuisine = document.getElementById('cuisine').value;

        if (!ingredients) {
            alert('Please enter at least one ingredient!');
            return;
        }

        try {
            loadingElement.style.display = 'flex';
            recipeResult.innerHTML = '';

            const result = await window.recipeAPI.generateRecipe(
                ingredients,
                mealType,
                dishName,
                cuisine
            );

            const formattedResult = result
                .replace(/\n\n/g, '<br><br>')
                .replace(/\n/g, '<br>')
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\*(.*?)\*/g, '<em>$1</em>')
                .replace(/#{3} (.*?)\n/g, '<h3>$1</h3>')
                .replace(/#{2} (.*?)\n/g, '<h2>$1</h2>')
                .replace(/#{1} (.*?)\n/g, '<h1>$1</h1>');

            recipeResult.innerHTML = formattedResult;
        } catch (error) {
            recipeResult.innerHTML = `<p class="error">Error: ${error}</p>`;
        } finally {
            loadingElement.style.display = 'none';
        }
    });
});