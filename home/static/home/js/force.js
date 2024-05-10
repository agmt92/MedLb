var width = 600,
    height = 600;

var color = d3.scale.category20();

var dist = (width + height) / 4;

var force = d3.layout.force()
    .charge(-120)
    .linkDistance(dist)
    .size([width, height]);

function getrank(rval) {
  return (rval / 2.0) + 3; // Adjust as needed
}

function getcolor(rval) {
  return color(rval); // Adjust if you don't have 'rank'
}

var svg = d3.select("#visualization").append("svg") // Make sure this is the right selector for your SVG container
    .attr("width", width)
    .attr("height", height);

function loadData(json) {
  force
      .nodes(json.nodes)
      .links(json.links)
      .start();

  var link = svg.selectAll("line.link")
      .data(json.links)
      .enter().append("line")
      .attr("class", "link")
      .style("stroke-width", function(d) { return Math.sqrt(d.value); });

  var node = svg.selectAll("circle.node")
      .data(json.nodes)
      .enter().append("circle")
      .attr("class", "node")
      .attr("r", function(d) { return getrank(d.rank); }) // Make sure nodes have 'rank'
      .style("fill", function(d) { return getcolor(d.rank); }) // Adjust if you don't have 'rank'
      .call(force.drag);

  node.append("title")
      .text(function(d) { return d.label; }); // Changed from d.url to d.label

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  });
}

// Assuming spiderJson is your data variable that contains nodes and links
loadData(spiderJson);
