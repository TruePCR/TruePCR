$(function() {
    Dropzone.options.datasetUpload = {

        // Whether Dropzone should upload dropped files immediately
        autoProcessQueue : true,

        addRemoveLinks : true,
        dictRemoveFile : "remove",
        previewsContainer : "#dataset-previews",
        clickable : "#dataset-upload",

        init : function() {
            var submitButton = document.querySelector("#submit-all");
            myDropzone = this;

            submitButton.addEventListener("click", function() {
                //myDropzone.processQueue();
                // Tell Dropzone to process all queued files.
            });

            // You might want to show the submit button only when
            // files are dropped here:
            this.on("addedfile", function() {
                // Show submit button here and/or inform user to click it.
                //document.forms["dataset-upload"].submit();
            });

        }
    };
});
