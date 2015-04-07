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
