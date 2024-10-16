document.addEventListener("DOMContentLoaded", function () {
    const searchForm = $("#search-form");
    const searchInput = $("#search-input");
    const recipeList = $("#recipe-list");

    function update_recipe_list() {
        const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        const query = searchInput.val();
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
                recipeList.html(data);
            },
            error: function () {
                console.log("Error: Unable to update recipes list.");
                alert('Error while updating recipes list.');
            },
        });
    }

    searchForm.on("submit", function (event) {
        event.preventDefault();
        update_recipe_list();
    });

    searchInput.on("input", function () {
        update_recipe_list();
    });

    const tagsList = $("#tags-list");
    $("#tags-toggle").click(function () {
        tagsList.toggleClass("d-none");
    });

    const tagSelectors = $('.tag-selector');
    function updateLabelClasses() {
        tagSelectors.each(function () {
            const tagId = $(this).attr("id");
            const isChecked = $(this).is(":checked");
            // Save checkbox state to cookies
            sessionStorage.setItem(tagId, isChecked ? "checked" : "unchecked");
            const label = $(`[for="${tagId}"]`);
            if (isChecked) {
                label.removeClass("bg-secondary").addClass("bg-primary");
            } else {
                label.removeClass("bg-primary").addClass("bg-secondary");
            }
        });
        update_recipe_list(); // Call it once after all labels are updated
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
});
