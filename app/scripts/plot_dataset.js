// Plot dataset

 $(function(){
     var well = 15;
     var dye = 'SYBR';

     function plot_dataset(well, dye){
         var id = 1;
         var url = '/' + id + '/well/' + well + '/dye/' + dye;
         console.log(url);
         // plot graph
         $.getJSON(url, function(data){
             console.log(data);
             var data2 = [];
             for(key in data){
                 data2.push({x: +key, y: data[key]});
             }
             var graph = new Rickshaw.Graph( {
                 element: document.querySelector("#chart-custom"),
                 width: 300,
                 height: 200,
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
             graph.render();
         });
     };

     plot_dataset(well, dye);

     // on well change redraw the graph
     $('#well-input').on("change", function(){
         well = $(this).val();
         console.log($(this).val());
         plot_dataset(well, dye);
     });

     // on colour change redraw the graph
     $('#dye-input').on("change", function(){
         dye = $(this).val();
         console.log($(this).val());
         plot_dataset(well, dye);
     });

 });
