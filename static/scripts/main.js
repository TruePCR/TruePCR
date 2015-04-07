function refresh_datasets(){
    // callback that displays the uploaded datasets
    $.getJSON( "/api/index", function( data ) {
        var items = [];
        $.each(data, function( key, val ) {
            items.push("<li><a href='/" + val.pk + "/'>" +
                       val.fields.file + "</a></li>");
        });
        console.log(data);
        var container = $('ul#datasets');
        container.empty().append(items);
    });
}

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

            this.on("complete", function() {
                refresh_datasets();
            });

        }
    };

});

// Plot dataset

 $(function(){
     // default options
     var well = 15;
     var dye = 'SYBR';

     function plot_dataset(well, dye){
         var id = 1; // TODO: vary based on the opened page
         var url = '/' + id + '/well/' + well + '/dye/' + dye;
         // plot graph
         $.getJSON(url, function(data){
             // format the data for Rickshaw
             var data2 = [];
             for(key in data){
                 data2.push({x: +key, y: data[key]});
             }
             // clear old graph
             $('#graph').empty();
             // add new graph
             var graph = new Rickshaw.Graph( {
                 element: document.querySelector("#graph"),
                 width: 600,
                 height: 400,
                 series: [{
                     color: 'steelblue',
                     data: data2
                     //   [
                     //   { x: 0, y: 40 },
                     //   { x: 1, y: 49 },
                     //   { x: 2, y: 38 },
                     //   { x: 3, y: 30 },
                     //   { x: 4, y: 32 }
                     // ]
                 }]
             });
             // set the axes
             var axes = new Rickshaw.Graph.Axis.X({
                 graph: graph,
                 orientation: 'top'
             });

             var y_axis = new Rickshaw.Graph.Axis.Y({
                 graph: graph,
                 orientation: 'left',
                 tickFormat: Rickshaw.Fixtures.Number.formatKMBT,
                 element: document.getElementById('y_axis')
             });
             graph.render();
         });
     };

     // initial plot
     plot_dataset(well, dye);

     // on well change redraw the graph
     $('#well-input').on("change", function(){
         well = $(this).val();
         plot_dataset(well, dye);
     });

     // on colour change redraw the graph
     $('#dye-input').on("change", function(){
         dye = $(this).val();
         plot_dataset(well, dye);
     });

 });

// dummy function to test the plotting

$(function(){
    console.log('test test');
    var graph = new Rickshaw.Graph( {
        element: document.querySelector("#graph_dummy"),
        width: 600,
        height: 400,
        series: [{
            color: 'steelblue',
            data: [
                { x: 0, y: 40 },
                { x: 1, y: 49 },
                { x: 2, y: 38 },
                { x: 3, y: 30 },
                { x: 4, y: 32 }
            ]
        }]
    });
    // set the axes
    var axes = new Rickshaw.Graph.Axis.X({
        graph: graph,
        orientation: 'top',
        tickSize: 10
    });

    var y_axis = new Rickshaw.Graph.Axis.Y({
        graph: graph,
        orientation: 'left',
        tickFormat: Rickshaw.Fixtures.Number.formatKMBT,
        element: document.getElementById('y_axis')
    });

    graph.render();
});
