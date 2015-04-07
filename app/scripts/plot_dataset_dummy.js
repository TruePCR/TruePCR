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
