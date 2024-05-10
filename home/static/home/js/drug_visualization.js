// Embedding your graph data directly into the JS file
var graphData = {
  nodes: [
    {id: "MedsDrug", label: "Drug"},
    {id: "MedsCountry", label: "Country"},
    {id: "MedsManufacturer", label: "Manufacturer"},
    {id: "MedsAgent", label: "Agent"},
    {id: "MedsPresentation", label: "Presentation"},
    {id: "MedsBg", label: "Bg"},
    {id: "MedsIngredient", label: "Ingredient"},
    {id: "MedsName", label: "Name"},
    {id: "MedsForm", label: "Form"},
    {id: "MedsDosage", label: "Dosage"},
    {id: "MedsAtc", label: "ATC"},
    {id: "MedsResparty", label: "Resparty"},
    {id: "MedsRescountry", label: "Rescountry"},
    {id: "MedsRegnum", label: "Regnum"},
    {id: "MedsStrength", label: "Strength"},
    {id: "MedsSubsidy", label: "Subsidy"}
  ],
  edges: [
    {source: "MedsDrug", target: "MedsCountry"},
    {source: "MedsDrug", target: "MedsManufacturer"},
    {source: "MedsDrug", target: "MedsAgent"},
    {source: "MedsDrug", target: "MedsPresentation"},
    {source: "MedsDrug", target: "MedsBg"},
    {source: "MedsDrug", target: "MedsIngredient"},
    {source: "MedsDrug", target: "MedsName"},
    {source: "MedsDrug", target: "MedsForm"},
    {source: "MedsDrug", target: "MedsDosage"},
    {source: "MedsDrug", target: "MedsAtc"},
    {source: "MedsDrug", target: "MedsResparty"},
    {source: "MedsDrug", target: "MedsRescountry"},
    {source: "MedsDrug", target: "MedsRegnum"},
    {source: "MedsDrug", target: "MedsStrength"},
    {source: "MedsDrug", target: "MedsSubsidy"}
  ]
};




// Find the index of the nodes based on their id to set as source or target
function findNodeIndex(id) {
  return graphData.nodes.findIndex(node => node.id === id);
}

// Update the edges to use node indices
graphData.edges = graphData.edges.map(function(edge) {
  return {
    source: findNodeIndex(edge.source),
    target: findNodeIndex(edge.target)
  };
});





// Your existing WebCola and D3.js code would follow here
// Use graphData to initialize and render the graph

// WebCola and D3.js code to visualize the data
document.addEventListener("DOMContentLoaded", function() {
      // Log the number of nodes and edges
  console.log("Number of nodes:", graphData.nodes.length);
  console.log("Number of edges:", graphData.edges.length);

  var width = 960,
      height = 500;

  var color = d3.scaleOrdinal(d3.schemeCategory10);

  var svg = d3.select("#visualization").append("svg")
      .attr("width", width)
      .attr("height", height);

  var simulation = cola.d3adaptor(d3)
      .linkDistance(60)
      .handleDisconnected(true)
      .avoidOverlaps(true)
      .size([width, height]);

  simulation
      .nodes(graphData.nodes)
      .links(graphData.edges)
      .start();

  var link = svg.selectAll(".link")
      .data(graphData.edges)
      .enter().append("line")
      .attr("class", "link");

  var node = svg.selectAll(".node")
      .data(graphData.nodes)
      .enter().append("circle")
      .attr("class", "node")
      .attr("r", 5)
      .style("fill", function(d) { return color(d.id); })
      .call(simulation.drag);

  simulation.on("tick", function() {
      link.attr("x1", function(d) { return d.source.x; })
          .attr("y1", function(d) { return d.source.y; })
          .attr("x2", function(d) { return d.target.x; })
          .attr("y2", function(d) { return d.target.y; });

      node.attr("cx", function(d) { return d.x; })
          .attr("cy", function(d) { return d.y; });

  // Log edge coordinates for debugging
  if (simulation.alpha() < 0.03) {  // log only when the simulation has stabilized
    simulation.stop(); // stop the simulation to prevent excessive logging
    link.each(function(d) {
      console.log(`Edge from ${d.source.id} to ${d.target.id}: x1=${d.source.x}, y1=${d.source.y}, x2=${d.target.x}, y2=${d.target.y}`);
    });
  }
});


  // Log the simulation data for debugging
  console.log("Simulation nodes:", simulation.nodes());
  console.log("Simulation edges:", simulation.links());
});