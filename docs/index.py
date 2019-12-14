#!/usr/bin/python
print "Content-type: text/html\n"
print """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <script src="https://d3js.org/d3.v3.min.js"></script>
  <script src="https://d3js.org/d3.v4.min.js"></script>
  <script src="https://d3js.org/d3-scale-chromatic.v1.min.js"></script>
  <title>Daytripper</title>
  <style type="text/css">

  path:hover {
    cursor: pointer;
  }

  /* Style for Custom Tooltip */
  div.tooltip {
   	position: absolute;
    width: auto;
    padding: 10px;
  	font: 12px sans-serif;
  	background: black;
    color: white;
  	border:1px solid grey;
  	border-radius: 5px;
  	pointer-events: none;
  }

  body {
  	font: 15px sans-serif;
    background-color: #222222;
    color: white;
    text-align: justify;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
    padding-bottom: 50px;
  }

  h1, h2 {
    text-align: center;
  }

  h2 {
    clear: both;
    background-color: white;
    color: #222;
    padding: 5px 0;
  }

  .inputs {
    overflow: hidden;
    text-align: center;
    margin-bottom: 10px;
    width: auto;
  }

  .inputs .option-group {
    overflow: hidden;
    display: inline-block;
    margin: 20px 20px 0px;
  }

  .axis path {
    stroke: white;
    stroke-width: 3px;
  }

  .tick line {
    stroke-width: 2px;
  }

  .tick text {
    fill: white;
    font-size: 12px;
  }

  .axis-label text {
    fill: white;
  }

  .img-card {
    clear: both;
    float: left;
    padding-bottom: 20px;
  }

  .img-card img {
    width: 49%;
    float: left;
  }

  .img-card p {
    width: 49%;
    float: left;
    padding-left: 2%;
  }

</style>
</head>

<body>
  <div class="header">
    <h1>Daytripper: Visualizing Trends in Color</h1>

    <p>
      Daytripper, a comic book by F&aacute;bio Moon and Gabriel B&aacute;, captures a series
      of seemingly day-to-day moments that end up defining the different story
      arcs in the main character's life. These story arcs include falling in and
      out of love, relationships with parents, friendships, fatherhood, and
      career aspirations versus reality. As these arcs progress throughout the
      book, different themes, characters, and emotions take prominence.
    </p>

    <p>
      I wanted to see if I could capture these story arcs with data on how use
      of color changed across the book. To collect this data, I started with an
      image file for each page and extracted the color information for each
      pixel on three dimensions: hue, lightness, and saturation. Hue represents
      the degree on the color wheel, or where in the rainbow the color is.
      Lightness represents where the color is in the gradient from black to
      white. Saturation represents how concentrated the hue of the color is,
      from grayscale to as vivid as possible. We can visualize how colors in
      Daytripper change on these dimensions individually.
    </p>

    <h2>Chapters</h2>

    <div class="img-card">
      <h3>Lightness</h3>

      <img src="./chapter_lightness.png" />

      <p>
        The line chart to the left illustrates the average lightness of each
        chapter in Daytripper. There is a slight decline in lightness from the
        beginning of the book to Chapter 6, which has the lowest lightness
        factor. This is the chapter with the horrific plane crash that gives
        Br&aacute;s the opportunity to launch his career with a series of obituaries.
        But instead, feeling lost in his life, he goes after his missing friend
        and dies in a crash. In the chapters after Chapter 6, his writing career
        takes off with the publication of his first novel and the lightness of
        the chapters correspondingly increases. It peaks in Chapter 9, the dream
        sequence that ties together many moments visited throughout the book.
        After the peace Br&aacute;s comes to with his life at the end of Chapter 9,
        Chapter 10 darkens with the twilight of Br&aacute;s's last days. Thus this
        lightness trend line not only mirrors Br&aacute;s's career trajectory, but also
        his satisfaction with his life and understanding of his life's purpose.
      </p>
    </div>

    <div class="img-card">
      <h3>Saturation</h3>

      <img src="./chapter_saturation.png" />

      <p>
        The line chart to the left illustrates the average saturation of each
        chapter in Daytripper. The initial decline in saturation over about
        the first half of chapters, subsequent increase in saturation over
        about the second half of chapters, and dropoff at Chapter 10 follows a
        similar pattern to the trend in lightness. The noticeable difference is the
        spike in Chapter 5, which is actually the chapter with the highest
        saturation. This is the chapter from the perspective of Br&aacute;s as a child,
        when he is still discovering the world and innocent to many of the
        concepts such as aging that he will struggle with later. Thus we can
        think of the trend in saturation as representing Br&aacute;s's general
        happiness with his life.
      </p>
    </div>

    <div class="img-card">
      <h3>Hue</h3>

      <img src="./chapter_hue.png" />

      <p>
        The area chart to the left illustrates the average distribution of
        different hues in each chapter in Daytripper. For this analysis, I
        aggregated different hues into 12 different buckets of the same general
        shade. The thickness of the band of a hue on the chart represents the
        percentage of the page that is composed by pixels in that shade. Aside
        from black and white, the most popular hue is actually orange. I think
        orange and yellow hues in particular were used throughout the book to
        represent panels occurring in the past relative to the current time of
        the particular chapter. That could explain the especially prominent use
        of orange and yellow in Chapter 9, the dream flashback chapter. Blues
        and greens are particularly more prominent in Chapter 4. In this chapter,
        Br&aacute;s spends a lot of time in the hospital for the birth of his son. But
        there is a generally subdued melancholy mood over the chapter as Br&aacute;s's
        father passes away and Br&aacute;s himself has a heart attack at the end. While
        other chapters have flashier, more explosive tragedies, the blues and
        greens in Chapter 4 represent the quiet sadness Br&aacute;s keeps to himself
        and his calm passing.
      </p>
    </div>
  </div>

  <h2>Pages</h2>

  <h3>Lightness</h3>

  <p>
    Over the whole book, and within the arc of each chapter, lightness is
    pretty variable. Focusing in on Chapter 7 in particular, the lightness is
    fairly constant until it peaks when Br&aacute;s sees the hut that his friend Jorge
    has been living in, right before he sees him in person. But when Jorge steps
    into the hut, the lightness abruptly drops with the squalor of Jorge's
    living conditions. The lightness makes another sharp decline to its lowest
    point on page 153 as Jorge suddenly cuts himself and then stabs Br&aacute;s. The
    single darkest point of the book is page 136, Br&aacute;s's death in a car crash
    following the plane crash. It closes the most tragic chapter in terms of
    world events of the book.
  </p>

  <div id="lightness-menu" class="inputs">
    <div class="option-group">
      Chapter:
      <select id="lightness-chapter">
        <option value="0">All</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
      </select>
    </div>

    <div class="option-group">
      Page #s:
      <input type="number" id="lightness-page-start" name="Start" min="0" max="224">
      <input type="number" id="lightness-page-end" name="End" min="0" max="224">
    </div>
  </div>

  <div id="lightness-chart"></div>

  <h3>Saturation</h3>

  <p>
    Saturation also shows a great range of concentration over the course of the
    book. Looking at Chapter 6, overall it is one of the lowest saturation
    chapters in the book. At this point Br&aacute;s is feeling unfulfilled by his
    job and missing his friend Jorge. The one noticeable spike in the chapter
    occurs when the plane crashes and the pages are filled with the fiery colors
    of the disaster. The point of lowest saturation in the book is pages 205 and
    206, when Br&aacute;s converses with his doctor in complete blackness at the end of
    Chapter 10, foreshadowing his choice not to continue treatment and let his
    life end. The most saturated page is 193, when in a dream Br&aacute;s reunites with
    his friend Jorge, a rewriting of the violent murder we last saw in that
    setting.
  </p>

  <div id="saturation-menu" class="inputs">
    <div class="option-group">
      Chapter:
      <select id="saturation-chapter">
        <option value="0">All</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
      </select>
    </div>

    <div class="option-group">
      Page #s:
      <input type="number" id="saturation-page-start" name="Start" min="0" max="224">
      <input type="number" id="saturation-page-end" name="End" min="0" max="224">
    </div>
  </div>

  <div id="saturation-chart"></div>

  <h3>Hue</h3>

  <p>
    One frequently appearing pattern in hue within chapters is a spike in the
    frequency of red towards the end of the chapter. The arc of most
    chapters in the book build towards a dramatic event that brings Br&aacute;s to the
    end of his life. Red is used to illustrate violent events such as a gunshot,
    spilling of blood, or car crashes. While greens and blues are not as
    generally popular across the book, they play an important role in Chapter 2.
    After an uncomfortable discussion on race with Jorge, Br&aacute;s dives into the
    ocean, where he meets Olinda. He returns to the shore to see Olinda again at
    the festival. And then at the end of the chapter, he drowns in the ocean.
    The blue and green hues rise and fall in prominence like waves across the
    chart. But while the hue of the water tends towards the greens and teals
    more at the beginning of the chapter, at the end when Br&aacute;s drowns it is the
    deeper blues that dominate.
  </p>

  <p>
    By clicking on the color buttons below, you can add or remove the hues you
    want to focus on from the chart. The rainbow button reselects all the hues
    and the gray button deselects all the hues. On this chart you can also
    drag over an area to set new boundaries on the page numbers.
  </p>

  <div id="menu" class="inputs">
    <div class="option-group">
      Chapter:
      <select id="chapter">
        <option value="0">All</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
      </select>
    </div>

    <div class="option-group">
      Page #s:
      <input type="number" id="page-start" name="Start" min="0" max="224">
      <input type="number" id="page-end" name="End" min="0" max="224">
    </div>
  </div>

  <div id="color-menu" class="option-group" />

  <div id="chart" />

  <script type="text/javascript">

  /** Global Variables */

  var margin = {top: 50, right: 50, bottom: 50, left: 50};
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
    });
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

      var button = menu.append('g');

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
    d3.csv("data/data2.csv", function(data) {
      pageData = data;
      d3.csv("data/data_chapters2.csv", function(data) {
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
      .call(d3.axisBottom(x).ticks(5).tickSize(0));

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
      .attr("stroke-width", 3);

    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d[""]) })
        .y(function(d) { return y(d[feature]) })
      );
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
      (data);

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
        .on("end", updateChart);

    // Create the scatter variable: where both the circles and the brush take place
    var areaChart = svg.append('g')
      .attr("clip-path", "url(#clip)");

    // Area generator
    var area = d3.area()
      .x(function(d) { return x(d.data[""]); })
      .y0(function(d) { return y(d[0]); })
      .y1(function(d) { return y(d[1]); });

    // Show the areas
    areaChart
      .selectAll("mylayers")
      .data(stackedData)
      .enter()
      .append("path")
        .attr("class", function(d) { return "myArea " + d.key })
        .style("fill", function(d) { return color(d.key); })
        .attr("d", area);

    // Add the brushing
    areaChart
      .append("g")
        .attr("class", "brush")
        .call(brush);

    var idleTimeout
    function idled() { idleTimeout = null; }

    // A function that update the chart for given boundaries
    function updateChart() {

      extent = d3.event.selection;

      // If no selection, back to initial coordinate. Otherwise, update X axis domain
      if(!extent){
        if (!idleTimeout) return idleTimeout = setTimeout(idled, 350); // This allows to wait a little bit
        x.domain(d3.extent(data, function(d) { return d[""]; }));
      }else{
        x.domain([ x.invert(extent[0]), x.invert(extent[1]) ]);
        areaChart.select(".brush").call(brush.move, null); // This remove the grey brush area as soon as the selection has been done
      }

      // Update axis and area position
      xAxis.transition().duration(1000).call(d3.axisBottom(x).ticks(5).tickSize(0))
      areaChart
        .selectAll("path")
        .transition().duration(1000)
        .attr("d", area);
    }

  }


  </script>

</body>
</html>
"""
