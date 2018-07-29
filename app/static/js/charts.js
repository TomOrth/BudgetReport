function barChart(id, data, nameKey) {
    var xValue = [],
        yValue = [];
    
    $.each(data, function(index, value){
        xValue.push(value.amount)
        yValue.push(value[nameKey]);
    });

    var trace1 = {
        x: xValue,
        y: yValue,
        textangle: 270,
        type: 'bar',
        text: xValue,
        textposition: 'auto',
        hoverinfo: 'none',
        orientation: 'h',
        marker: {
          color: 'rgb(64,81,181)'        
        },
        textfont: {
            color: '#ffffff'
        }
      };
      
      var data = [trace1];
      
      var layout = {
        margin: {
            b: 50,
            t: 50
        },
        xAxis: {
            fixedrange: true
        },
        yAxis: {
            fixedrange: true
        }
      };
      
      Plotly.newPlot(id, data, layout, {displayModeBar: false});
}

