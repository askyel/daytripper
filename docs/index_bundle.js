!function(t){var e={};function n(r){if(e[r])return e[r].exports;var a=e[r]={i:r,l:!1,exports:{}};return t[r].call(a.exports,a,a.exports,n),a.l=!0,a.exports}n.m=t,n.c=e,n.d=function(t,e,r){n.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:r})},n.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},n.t=function(t,e){if(1&e&&(t=n(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)n.d(r,a,function(e){return t[e]}.bind(null,a));return r},n.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return n.d(e,"a",e),e},n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},n.p="",n(n.s=0)}([function(t,e){var n,r,a,o,i=960,s=500,l="Overall",c={},f={};function d(t){return t.replace(/\s/g,"")}function u(){var t=v(l+"Diff");for(var e in c)d3.select("#"+d(e)).style("fill",function(){return y(e,l,t)})}function p(t,e){c[t].selected=e}function v(t){var e=0;for(var n in c)if("United States"!==n){d3.select("#"+d(n));if(c[n].selected){var r=c[n][t];Math.abs(r)>e&&(e=Math.abs(r))}}return e}function y(t,e,n){var r=e+"Diff",a=c[t][r];return a?c[t].selected?a>0?d3.interpolate("#ffffff","#ff7f50")(Math.abs(a)/n):d3.interpolate("#ffffff","#50d0ff")(Math.abs(a)/n):"#000":"#444"}function h(){d3.selectAll(".chart").remove();var t=v(l+"Diff"),e=Number(c["United States"][l]);if(0!==t){var n={top:20,right:150,bottom:40,left:110},r=d3.scale.linear().domain([e-t,e+t]).range([0,i-n.left-n.right]),a=d3.select("body").append("svg:svg").attr("width",i).attr("height",65+n.top+n.bottom).attr("class","chart").append("g").attr("transform","translate("+n.left+","+n.top+")").attr("width",i-n.left-n.right).attr("height",50).attr("class","main"),o=d3.axisBottom().scale(r);a.append("g").attr("transform","translate(0,50)").attr("class","axis").call(o).selectAll(".tick line").attr("stroke","#fff").selectAll(".tick text").attr("fill","#fff"),a.append("g").attr("class","axis-label").append("text").attr("text-anchor","middle").attr("x",i/2-n.left-20).attr("y",n.top+50+15).style("color","white").text("Percent of Population Below Poverty Level in 2016");var s=a.append("svg:g");for(var f in c)if(c[f].selected){var d=r(c[f][l]);s.append("svg:circle").attr("cx",function(){return d}).attr("cy",function(){return 25}).attr("r",6).style("visibility",function(){return c[f][l]?"visible":"hidden"}).attr("fill",function(){return y(f,l,v(l+"Diff"))}).attr("stroke-width","2px").attr("stroke",function(){return"United States"===f?(console.log("Found"),"#AAA"):""}).on("mouseover",g(f)).on("mouseout",function(){d3.select(".tooltip").transition().duration(200).style("opacity",0)})}}}d3.selectAll(".option").on("click",function(){d3.selectAll(".option").classed("active",!1),d3.select("#"+this.id).classed("active",!0),m(this.id),h()}),d3.select("#allStates").on("click",function(){b(!0)}),d3.select("#noStates").on("click",function(){b(!1)}),d3.json("data/state-categories.json",function(t){for(var e in t)d3.select("#"+t[e].type),d3.select("#"+e).on("click",function(){var e=t[this.id];for(var n in b(!1),e.states){var r=e.states[n];p(r,!0)}u(),h()}).on("mouseover",function(){var e=t[this.id];d3.select("#state-option-description").text(e.description)}).on("mouseout",function(){d3.select("#state-option-description").text("")})}),n=d3.geo.albersUsa().translate([i/2,s/2]).scale([1e3]),r=d3.geo.path().projection(n),a=d3.select("body").append("div").attr("class","tooltip").style("opacity",0),o=d3.select("#map").append("svg").attr("width",i).attr("height",s),d3.json("data/us-states.json",function(t){o.selectAll("path").data(t.features).enter().append("path").attr("d",r).classed("selected",!0).attr("id",function(t){return d(t.properties.name)}).style("stroke","#fff").style("stroke-width","1").on("click",function(t){var e=c[t.properties.name][l];if(e){var n=!c[t.properties.name].selected;p(t.properties.name,n),u(),h()}}).on("mouseover",function(t){var e=t.properties.name,n=c[t.properties.name][l];n&&(e+=": "+n),a.transition().duration(200).style("opacity",1),a.text(e).style("left",d3.event.pageX+"px").style("top",d3.event.pageY-28+"px")}).on("mouseout",function(t){a.transition().duration(200).style("opacity",0)}),d3.csv("data/poverty_demographics.csv",function(t){var e=Object.keys(t[0]);for(var n in e)f[e[n]]=0;for(var r=0;r<t.length;r++){var a=t[r].State;for(var n in c[a]={selected:!0},e){var o=t[r][e[n]];c[a][e[n]]=o,Math.abs(o)>f[e[n]]&&(f[e[n]]=Math.abs(o))}}m(l),h()})});var g=function(t){return function(){var e=t,n=c[t][l];n&&(e+=": "+n),d3.select(".tooltip").transition().duration(200).style("opacity",1),d3.select(".tooltip").text(e).style("left",d3.event.pageX+"px").style("top",d3.event.pageY-12+"px").style("transform","translate(-50%, -100%)")}};function m(t){var e=v((l=t)+"Diff");for(var n in c)d3.select("#"+d(n)).style("fill",function(){return y(n,t,e)})}function b(t){for(var e in c)p(e,t);p("United States",!0),u(),h()}}]);