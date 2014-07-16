$(function() {

    $("#submit-all").css("display", "none");

    Dropzone.options.datasetUpload = {

        // Whether Dropzone should upload dropped files immediately
        autoProcessQueue : true,

        addRemoveLinks : true,
        dictRemoveFile : "remove",
        previewsContainer : "#dataset-previews",
        clickable : "#dataset-upload",
        // we did this in the template
        //dictDefaultMessage : "drop dataset here",

        init : function() {
            var submitButton = document.querySelector("#submit-all");
            myDropzone = this;

            submitButton.addEventListener("click", function() {
                // Tell Dropzone to process all queued files.
                myDropzone.processQueue();
            });

            // You might want to show the submit button only when
            // files are dropped here:
            this.on("addedfile", function() {
                // Show submit button here and/or inform user to click it.
                $("#submit-all").css("display", "inherit");
                // hide the "drop here" message
                $("#dataset-upload .dz-message").css("display", "none");
                // we could also automatically submit, but we won't
                //document.forms["dataset-upload"].submit();
            });

        }
    };

    $.getJSON( "/api/index", function( data ) {
        console.log(data);
    });
});

