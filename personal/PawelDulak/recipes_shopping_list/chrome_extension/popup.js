let addRecipe = document.getElementById('addRecipe');
let generateShoppingList = document.getElementById('generateShoppingList');
let recipesList = document.getElementById('recipesList');

document.addEventListener("DOMContentLoaded", function () {
    updateRecipesList();
});

chrome.storage.sync.get('recipesArray', function (data) {
    console.log(data.recipesArray);
    console.log('get called in popup.js');
});

addRecipe.onclick = function (element) {
    let color = element.target.value;
    let tabsStore = null;
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        addRecipeToList(tabs[0]);
    });
};

function addRecipeToList(thisTab) {
    chrome.storage.sync.get('recipesArray', function (data) {
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
    chrome.storage.sync.get('recipesArray', function (data) {
        if (data.recipesArray.length > 0) {
            data.recipesArray.forEach(function(recipe){
                recipesList.innerHTML += '<li>' + recipe.title + '</li>';
            });
        } else {
            recipesList.innerHTML = '<li>Brak przepisów na liście</li>';
        }
    });
}