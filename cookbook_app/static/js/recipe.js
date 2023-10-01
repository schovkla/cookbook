document.addEventListener("DOMContentLoaded", function () {
    $(".single-tag-selector").each(function () {
        function searchSingleTag() {
            console.log("Searching by single tag");
            sessionStorage.clear();
            const tagId = $(this).attr("for");
            console.log("FO g " + tagId);
            sessionStorage.setItem(tagId, "checked");
        }

        $(this).on("click", searchSingleTag);
    });

});