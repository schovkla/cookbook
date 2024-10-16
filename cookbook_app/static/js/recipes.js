document.addEventListener("DOMContentLoaded", function () {
    // Handle search form submission via AJAX
    const searchForm = $("#search-form")
    const searchInput = $("#search-input")
    const recipeList = $("#recipe-list")

    function update_recipe_list() {
        const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        const query = searchInput.value;
        const selectedTags = [];
        const tagSelectors = $('.tag-selector');
        tagSelectors.each(function () {
            if (this.checked) {
                const tagId = $(this).attr('id');
                selectedTags.push(tagId);
            }
        });
        $.ajax({
            url: endpoint_url,
            method: "POST",
            data: {
                csrfmiddlewaretoken: csrfToken,
                query: query,
                selected_tags: selectedTags,
            },
            dataType: "html",
            success: function (data) {
                recipeList.innerHTML = data;
            }, error: function (data) {
                alert('Error while updating recipes list.');
            },
        });
    }

    searchForm.on("submit", function (event) {
        event.preventDefault();
        update_recipe_list();
    });

    searchInput.on("input", function (event) {
        update_recipe_list();
    })

    let tagsList = $("#tags-list");

    $("#tags-toggle").click(function () {
        tagsList.toggleClass("d-none");
    })


    const tagSelectors = $('.tag-selector');
    // Update labels classes on click
    function updateLabelClasses() {
        tagSelectors.each(function () {
            const tagId = $(this).attr("id");
            const isChecked = $(this).is(":checked");
            // Save checkbox state to cookies
            sessionStorage.setItem(tagId, isChecked ? "checked" : "unchecked");
            const label = $(`[for="${tagId}"]`);
            if (isChecked) {
                label.removeClass("bg-secondary");
                label.addClass("bg-primary");
            } else {
                label.removeClass("bg-primary");
                label.addClass("bg-secondary");
            }
            update_recipe_list();
        });
    }

    tagSelectors.each(function () {
        $(this).on("change", updateLabelClasses);
        const tagId = $(this).attr("id");
        const storedValue = sessionStorage.getItem(tagId);
        if (storedValue === "checked") {
            $(this).prop("checked", true);
        }
    });
    updateLabelClasses();

    function update_tags_visibility() {
        if ($(".tag-selector:checked").length > 0) {
            tagsList.removeClass("d-none");
        } else {
            tagsList.addClass("d-none");
        }
    }

    update_tags_visibility();
})
