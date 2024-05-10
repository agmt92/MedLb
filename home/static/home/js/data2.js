// Load the JSON data from the specified path
d3.json("/static/home/js/mdb.json").then(function(graph) {
    console.log("Graph loaded successfully:", graph);

    // Specify the dimensions of the chart
    const width = 1280;
    const height = 720;

    // Define the color scale
    const color = d3.scaleOrdinal(d3.schemeCategory10);

    // Append the SVG object to the div with the id "visualization"
    const svg = d3.select("#visualization").append("svg")
        .attr("viewBox", `0 0 ${width} ${height}`)
        .attr("style", "max-width: 100%; height: auto;");

    // Append a 'g' element to the SVG; this 'g' element will contain all other visual elements
    const container = svg.append("g");

    // Define zoom behavior
    const zoomHandler = d3.zoom()
        .on("zoom", (event) => {
            container.attr("transform", event.transform);
        });

    // Apply the zoom behavior to the SVG element
    svg.call(zoomHandler);

    console.log("SVG container and zoom behavior set up.");

    // Initialize the force simulation
    const simulation = d3.forceSimulation(graph.nodes)
        .force("link", d3.forceLink(graph.links).id(d => d.id).distance(50))
        .force("charge", d3.forceManyBody().strength(-30))
        .force("x", d3.forceX(width / 2))
        .force("y", d3.forceY(height / 2));

    console.log("Force simulation initialized.");

    // Create the links (lines)
    const link = container.selectAll("line")
        .data(graph.links)
        .enter().append("line")
        .attr("stroke", "#999")
        .attr("stroke-opacity", 0.6)
        .attr("stroke-width", d => Math.sqrt(d.value));

    console.log("Links created.");

    // Create the nodes (circles)
    const node = container.selectAll("circle")
        .data(graph.nodes)
        .enter().append("circle")
        .attr("r", 5)
        .attr("fill", d => color(d.group))
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    console.log("Nodes created.");

    // Add titles for nodes
    node.append("title")
        .text(d => d.id);

    console.log("Titles added to nodes.");

    // Drag event handlers
    function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }

    // Simulation tick function
    simulation.on("tick", () => {
        link.attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node.attr("cx", d => d.x)
            .attr("cy", d => d.y);
    });

    console.log("Simulation tick function set up.");
}).catch(error => {
    console.error('Failed to load the graph data:', error);
});
