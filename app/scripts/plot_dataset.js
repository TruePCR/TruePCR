// Plot dataset

 $(function(){
     // default options
     var well = 15;
     var dye = 'SYBR';

     function plot_dataset(well, dye){
         // the main function that fetches and plots the data
         var id = 1; // TODO: vary based on the opened page
         var url = '/' + id + '/well/' + well + '/dye/' + dye;
         // plot graph
         $.getJSON(url, function(data){
             // format the data for Rickshaw
             var data2 = [];
             for(key in data){
                 data2.push({x: +key, y: data[key]});
             }
             visualise(data2);
         });
     };

     function visualise(data){
         // clear old graph
         $('#graph').empty();
         // add new graph
         var graph = new Rickshaw.Graph( {
             element: document.querySelector("#graph"),
             width: 600,
             height: 400,
             series: [{
                 color: 'steelblue',
                 data: data
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
     };

     function plot_model(well, dye){
         var id = 1; // TODO: vary based on the opened page
         var url = '/api/model/' + id + '/well/' + well + '/dye/' + dye;
         // plot graph
         $.getJSON(url, function(data){
             console.log('model data:');
             console.log(data);
         });
     }

     // initial plot
     plot_dataset(well, dye);
     plot_model(well, dye);

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
