document.addEventListener("DOMContentLoaded", function () {
    const recipeNote = document.getElementById("recipe_note");
    let isEditMode = false;

    recipeNote.addEventListener("click", function () {
        if (!isEditMode) {
            recipeNote.contentEditable = "true";
            recipeNote.focus();
            isEditMode = true;
        }
    })

    recipeNote.addEventListener("blur", function () {
        if (isEditMode) {
            recipeNote.contentEditable = "false";
            isEditMode = false;
            const newNote = recipeNote.textContent;
            const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
            const recipeId = recipeNote.getAttribute("data-recipe-id");

            // Save note on server.
            $.ajax({
                url: "/update_note/",
                method: "POST",
                data: {
                    csrfmiddlewaretoken: csrfToken,
                    new_note: newNote,
                    recipe_id: recipeId,
                },
            });
        }
    });
})
