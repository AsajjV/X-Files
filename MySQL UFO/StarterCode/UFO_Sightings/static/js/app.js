function buildMetadata(state) {
    var url = `/states/${state}`; //this url says, "look here for ___ sample number"
    console.log(url);
  
    // @TODO: Complete the following function that builds the metadata panel
  
    // Use `d3.json` to fetch the metadata for a sample
    d3.json(url).then(function(response) { //give me the jsonified data for the url above
      console.log(response);
  
      metaData = [response];
      console.log(metaData);

      // Use d3 to select the panel with id of `#sample-metadata`
      statePanel = d3.select("#state-metadata")
      // Use `.html("") to clear any existing metadata
      statePanel.html(""); //replace the last displayed data before putting in new data below.

      // Use `Object.entries` to add each key and value pair to the panel
      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.
      metaData.forEach((selectState) => {

      Object.entries(selectState).forEach(([key, value]) => {
        var row = statePanel.append("tr");
        row.text(key + ": " + value);
      })
    })
  })
}

// function buildCharts(state) {
//   var graphUrl = `/states/${state}`; //this url says, "look here for ___ sample number"
//     console.log(graphUrl);

//   // @TODO: Use `d3.json` to fetch the sample data for the plots
//   d3.json(graphUrl).then(function(response) { //give me the jsonified data for the url above
//     console.log(response);


// }

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/states").then((stateNames) => {
    console.log(stateNames);
  stateNames.forEach((state) => {
      selector
        .append("option")
        .text(state)
        .property("value", state);
    });

    // Use the first sample from the list to build the initial plots
    const firstState = stateNames[0];
    // buildCharts(firstState);
    buildMetadata(firstState);
  });
}

function optionChanged(newState) {
  // Fetch new data each time a new sample is selected
  // buildCharts(newState);
  buildMetadata(newState);
}

// Initialize the dashboard
init();
