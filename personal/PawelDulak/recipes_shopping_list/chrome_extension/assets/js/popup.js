let addRecipe = document.getElementById('addRecipe');
let generateShoppingList = document.getElementById('generateShoppingList');
let recipesList = document.getElementById('recipesList');
let clearList = document.getElementById('clearRecipesList');

document.addEventListener("DOMContentLoaded", function () {
    updateRecipesList();
});

addRecipe.onclick = function(element) {
    let color = element.target.value;
    let tabsStore = null;
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        addRecipeToList(tabs[0]);
    });
};

generateShoppingList.onclick = function(element) {
    chrome.storage.sync.get('recipesArray', function (data) {
        if (data.recipesArray.length > 0) {
            document.getElementById('ajax-loader-overlay').style.display='block';
        } else {
            alert('Nie ma żadnych przepisów do wysłania do serwera');
        }
    });
}

clearList.onclick = function(element) {
    if (confirm('Czy jesteś pewien?')) {
        chrome.storage.sync.set({
            recipesArray: [],
        }, function () {
            console.log('removed recipes from the list');
            updateRecipesList();
        });
    }
}

function addRecipeToList(thisTab) {
    chrome.storage.sync.get('recipesArray', function(data) {
        data.recipesArray.push({
            title: thisTab.title,
            url: thisTab.url
        });
        chrome.storage.sync.set({
            recipesArray: data.recipesArray,
        }, function () {
            updateRecipesList();
        });
    });
}

function updateRecipesList() {
    recipesList.innerHTML = '';
    chrome.storage.sync.get('recipesArray', function(data) {
        if (data.recipesArray.length > 0) {
            data.recipesArray.forEach(function(recipe){
                recipesList.innerHTML += '<li>' + recipe.title + '</li>';
            });
        } else {
            recipesList.innerHTML = '<li>Brak przepisów na liście</li>';
        }
    });
}