let addRecipe = document.getElementById('addRecipe');
let generateShoppingList = document.getElementById('generateShoppingList');
let recipesList = document.getElementById('recipesList');
let clearList = document.getElementById('clearRecipesList');
let serverAddress = document.getElementById('serverAddress');

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

            fetch(serverAddress.value, {
                method: 'post', 
                body: JSON.stringify(data.recipesArray)
            })
            .then(response => response.json())
            .then(json => displayResults(json))
            .catch(displayError())

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

function displayResults(json) {
    let resultPlaceholder = document.getElementById('resultPlaceholder');
    document.getElementById('recipesListPlaceholder').style.display='none';
    resultPlaceholder.style.display='block';
    resultPlaceholder.innerHTML = '<pre>' + JSON.stringify(json, undefined, 2) + '</pre>';
    document.getElementById('ajax-loader-overlay').style.display = 'none';
}

function displayError() {
    let resultPlaceholder = document.getElementById('resultPlaceholder');
    document.getElementById('recipesListPlaceholder').style.display = 'none';
    resultPlaceholder.style.display = 'block';
    resultPlaceholder.innerHTML = '<p>Wystąpił błąd podczas komunikacji z serwerem</p>';
    document.getElementById('ajax-loader-overlay').style.display = 'none';
}