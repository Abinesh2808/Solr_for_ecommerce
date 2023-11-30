document.addEventListener('DOMContentLoaded', function () {
    var searchForm = document.querySelector('form');
    searchForm.addEventListener('submit', function (event) {
        event.preventDefault();

        var searchInput = document.getElementById('searchInput').value;

        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ searchInput: searchInput }),
        })
        .then(response => response.json())
        .then(data => {
            // Update the UI with the search results
            displaySearchResults(data);
        })
        .catch(error => {
            console.error('Error fetching search results:', error);
        });
    });

    function displaySearchResults(results) {
        var resultsContainer = document.querySelector('.results-container');
        resultsContainer.innerHTML = ''; // Clear previous results

        if (results.length > 0) {
            for (var i = 0; i < results.length; i++) {
                var productDiv = document.createElement('div');
                productDiv.classList.add('product');

                var productName = document.createElement('h3');
                productName.textContent = results[i].name;

                var productCategory = document.createElement('p');
                productCategory.textContent = 'Category: ' + results[i].category;

                var productBrand = document.createElement('p');
                productBrand.textContent = 'Brand: ' + results[i].brand;

                var productPrice = document.createElement('p');
                productPrice.textContent = 'Price: ' + results[i].price + ' /-';

                // Add more product details to display

                productDiv.appendChild(productName);
                productDiv.appendChild(productCategory);
                productDiv.appendChild(productBrand);
                productDiv.appendChild(productPrice);

                resultsContainer.appendChild(productDiv);
            }
            // Show the results container after displaying results
            resultsContainer.style.display = 'block';
        } else {
            // Display a message when no products are found
            resultsContainer.innerHTML = '<p>No products found.</p>';
            // Hide the results container when no results are found
            resultsContainer.style.display = 'none';
        }
    }
});
