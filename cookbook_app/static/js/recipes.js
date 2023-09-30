document.addEventListener("DOMContentLoaded", function () {
    // Handle search form submission via AJAX
    const searchForm = document.getElementById("search-form");
    const searchInput = document.getElementById("search-input");
    const recipeList = document.getElementById("recipe-list");

    function update_recipe_list() {
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        const query = searchInput.value;
        $.ajax({
            url: endpoint_url,
            method: "POST",
            data: {
                csrfmiddlewaretoken: csrfToken,
                query: query,
            },
            dataType: "html",
            success: function (data) {
                recipeList.innerHTML = data;
            },
            error: function (data) {
                alert('Error while updating recipes list.');
            },
        });
    }

    searchForm.addEventListener("submit", function (event) {
        event.preventDefault();
        update_recipe_list();
    });


    let tagsList = $("#tags-list");

    $("#tags-toggle").click(function () {
        tagsList.toggleClass("d-none");
    })
})
