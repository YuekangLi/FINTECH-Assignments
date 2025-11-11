function retrieveAction(event){
    let symbol=document.getElementById('symbol').value
    window.location = symbol
}

function makePlot(stockSymbol) {
  fetch('/stock/pricing/'+stockSymbol)
  .then(response => response.json())
  .then(data => {
    // Create Plotly chart
    const chartData = [{
      x: data.dates,
      y: data.adjClosePrices,
      type: 'scatter',
      mode: 'lines',
      marker: {
        color: 'blue'
      }
    }];

    const layout = {
      title: 'Stock Prices for ' + data.symbol,
      xaxis: {
        title: 'Date'
      },
      yaxis: {
        title: 'Price'
      }
    };

    Plotly.newPlot('myChart', chartData, layout);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

}




document.getElementById("retrieve").addEventListener("click", retrieveAction);
document.getElementById("symbol").addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    retrieveAction(event)
  }
})

window.onload = (event) => {
  let symbolField = document.getElementById('submittedSymbol');
  if (symbolField) {
    makePlot(symbolField.value)
  }    
};
