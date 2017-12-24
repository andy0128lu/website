d3.csv("tourist2.csv", function(error, data) {
    if(error){
        console.log(error);
    }
    else{
    var dataobj = { children: data }; //data type for Pack Layout

    var pack = d3.layout.pack();    //new object of layout

    pack = pack.padding(2).size([800,500]).sort(function(a,b) { return b.value - a.value; });

    var nodes = pack.nodes(dataobj);

    nodes = nodes.filter(function(it) { return it.parent; });
    var color = d3.scale.category20();
    d3.select("svg")
      .selectAll("circle")                 
      .data(nodes)                         
      .enter()                             
      .append("circle")                    
      .attr({
        cx: function(it) { return it.x; }, 
        cy: function(it) { return it.y; },
        r : function(it) { return it.r; }, 
        fill: function(it) { return color(it.country); },
        stroke: "#444",                    
      });

    d3.select("svg").selectAll("text").data(nodes).enter()
      .append("text")
      .attr({
        x: function(it) { return it.x; },
        y: function(it) { return it.y; },
        "text-anchor": "middle",
        "font-size": "16px",                    
      }).text(function(it)  { return (it.value>60000?it.country:""); }); 
    }
    

});
