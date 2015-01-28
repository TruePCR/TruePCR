// Plot dataset

 $(function(){
   $.getJSON('/1/well/15/dye/SYBR', function(data){
     console.log(data);
     data2 = [];
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

 });
