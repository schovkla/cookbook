document.addEventListener("DOMContentLoaded", function () {
    let tagsList = $("#tags-list");

    $("#tags-toggle").click(function () {
        tagsList.toggleClass("d-none");
    })
})
