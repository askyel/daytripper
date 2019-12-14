/** Global Variables */

var margin = {top: 50, right: 50, bottom: 50, left: 50}
var width = 1000 - margin.left - margin.right;
var height = 500 - margin.top - margin.bottom;

var pageData = {};
var numPages = 225;
var chapterData = {};

var startPage = 0;
var endPage = numPages;

var COLORS = ['red', 'orange', 'yellow', 'yellow-green', 'green', 'teal', 'cyan', 'cyan-blue', 'blue', 'purple', 'magenta', 'pink', 'black', 'white'];
var colorState = COLORS.map(function(c) { return true; });

pageSetup();

function pageSetup() {
  menuSetup();
  lMenuSetup();
  sMenuSetup();

  loadData();
}

function lMenuSetup() {
  chapterInputSetup("#lightness-chapter", drawLChart);
  pageInputSetup("#lightness-page", drawLChart);
}

function sMenuSetup() {
  chapterInputSetup("#saturation-chapter", drawSChart);
  pageInputSetup("#saturation-page", drawSChart);
}

function menuSetup() {
  chapterInputSetup("#chapter", drawColorChart);
  pageInputSetup("#page", drawColorChart);
  colorMenuSetup();
}

function chapterInputSetup(id, drawChart) {
  d3.select(id).on("change", function(d) {
    var selectedOption = d3.select(this).property("value");
    var chapter = Number(selectedOption);

    if (chapter === 0) {
      startPage = 0;
      endPage = numPages;
      drawChart(pageData, 0, numPages);
    } else if (chapter === 1) {
      startPage = 1;
      endPage = 23;
      drawChart(pageData, 1, 23);
    } else if (chapter === 2) {
      startPage = 23;
      endPage = 46;
      drawChart(pageData, 23, 46);
    } else if (chapter === 3) {
      startPage = 46;
      endPage = 69;
      drawChart(pageData, 46, 69);
    } else if (chapter === 4) {
      startPage = 69;
      endPage = 89;
      drawChart(pageData, 69, 89);
    } else if (chapter === 5) {
      startPage = 89;
      endPage = 111;
      drawChart(pageData, 89, 111);
    } else if (chapter === 6) {
      startPage = 111;
      endPage = 134;
      drawChart(pageData, 111, 134);
    } else if (chapter === 7) {
      startPage = 134;
      endPage = 157;
      drawChart(pageData, 134, 157);
    } else if (chapter === 8) {
      startPage = 157;
      endPage = 180;
      drawChart(pageData, 157, 180);
    } else if (chapter === 9) {
      startPage = 180;
      endPage = 203;
      drawChart(pageData, 180, 203);
    } else if (chapter === 10) {
      startPage = 203;
      endPage = numPages;
      drawChart(pageData, 203, numPages);
    }
  });
}

function pageInputSetup(id, drawChart) {
  d3.select(id + "-start").on("change", function(d) {
    startPage = Number(d3.select(this).property("value"));
    drawChart(pageData, startPage, endPage);
  });

  d3.select(id + "-end").on("change", function(d) {
    endPage = Number(d3.select(this).property("value")) + 1;
    drawChart(pageData, startPage, endPage);
  })
}

function colorPalette() {
  var palette = [];
  for (var i = 0; i < 360; i += 30) {
    palette.push(d3.hsl(i, 0.5, 0.5));
  }
  palette.push(d3.hsl(0, 0, 0));
  palette.push(d3.hsl(0, 0, 1));
  return palette;
}

function colorMenuSetup() {
  d3.select("#color-menu").selectAll(".color-buttons").remove();
  var gap = 50;

  var menu = d3.select("#color-menu")
    .append("svg")
    .attr("class", "color-buttons")
    .attr("width", width + margin.left + margin.right)
    .attr("height", 50);

  var palette = colorPalette();

  for (var i in palette) {
    var c = palette[i];
    var cx = margin.left + (width - 15*gap)/2 + i*gap;
    var border = "#aaa";
    if (!colorState[i]) {
      border = "#444";
    }

    var button = menu.append('g')

    button
      .append("circle")
        .attr("cx", cx)
        .attr("cy", 35)
        .attr("r", 15)
        .attr("fill", border);

    button
      .append("circle")
        .attr("id", i)
        .attr("cx", cx)
        .attr("cy", 35)
        .attr("r", 10)
        .attr("fill", c)
        .on("click", function(d) {
          colorState[this.id] = !colorState[this.id];
          colorMenuSetup();
          drawColorChart(pageData, startPage, endPage);
        });
  }

  // var menu = d3.select("#color-menu")
  //   .append("svg")
  //   .attr("class", "color-buttons")
  //   .attr("width", width + margin.left + margin.right)
  //   .attr("height", 50);

  var defs = menu.append("defs");

  var gradient = defs.append("linearGradient")
     .attr("id", "gradient")
     .attr("x1", "0%")
     .attr("x2", "100%")
     .attr("y1", "0%")
     .attr("y2", "100%");

  gradient.append("stop")
     .attr('class', 'start')
     .attr("offset", "0%")
     .attr("stop-color", palette[0])
     .attr("stop-opacity", 1);

  gradient.append("stop")
    .attr('class', 'start')
    .attr("offset", "50%")
    .attr("stop-color", palette[2])
    .attr("stop-opacity", 1);

  gradient.append("stop")
     .attr('class', 'end')
     .attr("offset", "100%")
     .attr("stop-color", palette[7])
     .attr("stop-opacity", 1);

   menu.append('g')
     .append("circle")
       .attr("id", "all-colors")
       .attr("cx", margin.left + (width - 15*gap)/2 + 14*gap)
       .attr("cy", 35)
       .attr("r", 15)
       .attr("fill", "url(#gradient)")
       .on("click", function(d) {
         colorState = COLORS.map(function(c) { return true; });
         colorMenuSetup();
         drawColorChart(pageData, startPage, endPage);
       });

  menu.append('g')
    .append("circle")
      .attr("id", "no-colors")
      .attr("cx", margin.left + (width - 15*gap)/2 + 15*gap)
      .attr("cy", 35)
      .attr("r", 15)
      .attr("fill", "#444")
      .on("click", function(d) {
        colorState = COLORS.map(function(c) { return false; });
        colorMenuSetup();
        drawColorChart(pageData, startPage, endPage);
      });
}

function loadData() {
  d3.csv("data/data2.csv", function (data) {
    pageData = data;
    d3.csv("data/data_chapters2.csv", function (data) {
      chapterData = data;
      drawLChart(pageData, 0, numPages);
      drawSChart(pageData, 0, numPages);
      drawColorChart(pageData, 0, numPages);
    });
  });
}

function drawLChart(dataSource, start, end) {
  drawLineChart(dataSource, "lightness", start, end);
}

function drawSChart(dataSource, start, end) {
  drawLineChart(dataSource, "saturation", start, end);
}

function drawLineChart(dataSource, feature, start, end) {
  var data = dataSource.slice(start, end);

  var chart = d3.select("#" + feature + "-chart");
  chart.selectAll("." + feature + "-svg").remove();

  var svg = chart.append("svg")
    .attr("class", feature + "-svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

  // AXES //

  var x = d3.scaleLinear()
    .domain([ start, end-1 ])
    .range([ 0, width ]);
  var xAxis = svg.append("g")
    .attr("class", "axis")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).ticks(5).tickSize(0))

  // Add X axis label:
  svg.append("text")
      .attr("text-anchor", "middle")
      .attr("x", width/2)
      .attr("y", height+40 )
      .style("fill", "white")
      .text("Page #");

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([ 0, 1 ])
    .range([ height, 0 ]);
  var yg = svg.append("g")
    .call(d3.axisLeft(y).ticks(2).tickSize(0));
  yg.select("path")
    .attr("stroke", "white")
    .attr("stroke-width", 3)

  svg.append("path")
    .datum(data)
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 1.5)
    .attr("d", d3.line()
      .x(function(d) { return x(d[""]) })
      .y(function(d) { return y(d[feature]) })
    )
}

function drawColorChart(dataSource, start, end) {
  var data = dataSource.slice(start, end);

  var chart = d3.select("#chart");
  chart.selectAll(".custom-chart").remove();

  var svg = chart
    .append("svg")
      .attr("class", "custom-chart")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

  var keys = COLORS.filter((c, i) => colorState[i]);

  // color palette
  var color = d3.scaleOrdinal()
    .domain(keys)
    .range(colorPalette().filter((c, i) => colorState[i]));

  var stackedData = d3.stack()
    .keys(keys)
    (data)

  // AXES //

  var x = d3.scaleLinear()
    .domain([ start, end-1 ])
    .range([ 0, width ]);
  var xAxis = svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).ticks(5).tickSize(0));

  // Add X axis label:
  svg.append("text")
      .attr("text-anchor", "middle")
      .attr("x", width/2)
      .attr("y", height+40 )
      .style("fill", "white")
      .text("Page #");

  // Add Y axis label:
  // svg.append("text")
  //     .attr("text-anchor", "end")
  //     .attr("x", 0)
  //     .attr("y", -20 )
  //     .text("Color %")
  //     .attr("text-anchor", "start")

  // Add Y axis
  var maxData = Math.max(...stackedData[keys.length - 1].map((y) => y[1]));

  var y = d3.scaleLinear()
    .domain([ 0, maxData ])
    .range([ height, 0 ]);
  svg.append("g")
    .call(d3.axisLeft(y).ticks(2).tickSize(0));

  // BRUSHING //

  // Add a clipPath: everything out of this area won't be drawn.
  var clip = svg.append("defs").append("svg:clipPath")
      .attr("id", "clip")
      .append("svg:rect")
      .attr("width", width )
      .attr("height", height )
      .attr("x", 0)
      .attr("y", 0);

  // Add brushing
  var brush = d3.brushX()
      .extent( [ [0,0], [width,height] ] ) // initialize 0,0 -> width,height
      .on("end", updateChart)

  // Create the scatter variable: where both the circles and the brush take place
  var areaChart = svg.append('g')
    .attr("clip-path", "url(#clip)")

  // Area generator
  var area = d3.area()
    .x(function(d) { return x(d.data[""]); })
    .y0(function(d) { return y(d[0]); })
    .y1(function(d) { return y(d[1]); })

  // Show the areas
  areaChart
    .selectAll("mylayers")
    .data(stackedData)
    .enter()
    .append("path")
      .attr("class", function(d) { return "myArea " + d.key })
      .style("fill", function(d) { return color(d.key); })
      .attr("d", area)

  // Add the brushing
  areaChart
    .append("g")
      .attr("class", "brush")
      .call(brush);

  var idleTimeout
  function idled() { idleTimeout = null; }

  // A function that update the chart for given boundaries
  function updateChart() {

    extent = d3.event.selection

    // If no selection, back to initial coordinate. Otherwise, update X axis domain
    if(!extent){
      if (!idleTimeout) return idleTimeout = setTimeout(idled, 350); // This allows to wait a little bit
      x.domain(d3.extent(data, function(d) { return d[""]; }))
    }else{
      x.domain([ x.invert(extent[0]), x.invert(extent[1]) ])
      areaChart.select(".brush").call(brush.move, null) // This remove the grey brush area as soon as the selection has been done
    }

    // Update axis and area position
    xAxis.transition().duration(1000).call(d3.axisBottom(x).ticks(5).tickSize(0))
    areaChart
      .selectAll("path")
      .transition().duration(1000)
      .attr("d", area)
  }

}

function updateChartColor(color) {
  console.log(color);
}
