function plotting_linechart(response){

    $("#placeholder").height(800);
    $("#placeholder").width(800);

    $("#placeholder2").height(800);
    $("#placeholder2").width(800);

    $("#placeholder3").height(800);
    $("#placeholder3").width(800);

    console.log(response);

    var data_for_countries = [];

    for(i = 1;i<response.length;i++){
      var data_for_country = [];
      var data1 = response[i].map(function myfunc(value,index,array){
          value[0] = new Date(value[0]).getTime();
          return value.slice(0,1).concat(value.slice(1,2));
        });
      var data2 = response[i].map(function myfunc(value,index,array){
          value[0] = new Date(value[0]).getTime();
          return value.slice(0,1).concat(value.slice(2,3));
        });
      var data3 = response[i].map(function myfunc(value,index,array){
        value[0] = new Date(value[0]).getTime();
        return value.slice(0,1).concat(value.slice(3,4));
      });
      data_for_country.push(data1);
      data_for_country.push(data2);
      data_for_country.push(data3);
      data_for_countries.push(data_for_country);
    }

    console.log(data_for_countries);

    var dataset1 = [];
    var dataset2 = [];
    var dataset3 = [];

    for(i=0;i<data_for_countries.length;i++){
      var country_dataset1 = {label:response[0][i],data:data_for_countries[i][0]};
      var country_dataset2= {label:response[0][i],data:data_for_countries[i][1]};
      var country_dataset3 = {label:response[0][i],data:data_for_countries[i][2]};
      dataset1.push(country_dataset1);
      dataset2.push(country_dataset2);
      dataset3.push(country_dataset3);
    }

    console.log(dataset1[0].data.length);

    var tick_size = 1;

    if(dataset1[0].data.length > 15 ){
      tick_size = 3;
    }
    if(dataset1[0].data.length > 30){
      tick_size = 14;
    }

    var options1 = {
      series: {
        lines: {
          show: true
            },
            points: {
                 radius: 3,
                 fill: true,
                 show: true
             }
         },
        xaxis: {
          mode: "time",
          tickSize: [tick_size, "day"],
          tickLength: 0,
          axisLabel: "2020",
          axisLabelUseCanvas: true,
          axisLabelFontSizePixels: 12,
          axisLabelFontFamily: 'Verdana, Arial',
          axisLabelPadding: 10
        },
        yaxis: {
          axisLabel: "Number of People",
          axisLabelUseCanvas: true,
          axisLabelFontSizePixels: 12,
          axisLabelFontFamily: 'Verdana, Arial',
          axisLabelPadding: 3
          },
    };

  var options2 = {
      series: {
        lines: {
          show: true
            },
            points: {
                 radius: 3,
                 fill: true,
                 show: true
             }
         },
        xaxis: {
          mode: "time",
          tickSize: [tick_size, "day"],
          tickLength: 0,
          axisLabel: "2020",
          axisLabelUseCanvas: true,
          axisLabelFontSizePixels: 12,
          axisLabelFontFamily: 'Verdana, Arial',
          axisLabelPadding: 10
        },
        yaxis: {
          axisLabel: "Number of people",
          axisLabelUseCanvas: true,
          axisLabelFontSizePixels: 12,
          axisLabelFontFamily: 'Verdana, Arial',
          axisLabelPadding: 3
          },
    };

    var options3 = {
      series: {
        lines: {
          show: true
            },
            points: {
                 radius: 3,
                 fill: true,
                 show: true
             }
         },
        xaxis: {
          mode: "time",
          tickSize: [tick_size, "day"],
          tickLength: 0,
          axisLabel: "2020",
          axisLabelUseCanvas: true,
          axisLabelFontSizePixels: 12,
          axisLabelFontFamily: 'Verdana, Arial',
          axisLabelPadding: 10
        },
        yaxis: {
          axisLabel: "Infections per 100.000",
          axisLabelUseCanvas: true,
          axisLabelFontSizePixels: 12,
          axisLabelFontFamily: 'Verdana, Arial',
          axisLabelPadding: 3
          },
      };

    $.plot(placeholder,dataset1,options1);
    $.plot(placeholder2,dataset2,options2);
    $.plot(placeholder3,dataset3,options3);
}


function plotting_barchart(response){


  $("#placeholder4").height(800);
  $("#placeholder4").width(1200);

  var raw_data = response.map(function f(value,index,array){
      value = [value[1],index];
      return value;
  });

  var data_set = [{label:"Infectionrate by Country",data:raw_data,color:"#AB5800"}];

  console.log(raw_data)

  var ticks = response.map(function f(value,index,array){
      value = [index,value[0]];
      return value;
  });

  console.log(ticks);

  var options = {
            series: {
                bars: {
                    show: true
                }
            },
            bars: {
                align: "center",
                barWidth: 0.5,
                horizontal: true,
                fillColor: { colors: [{ opacity: 0.5 }, { opacity: 1}] },
                lineWidth: 1
            },
            xaxis: {
                axisLabel: "Average Infections per 100.000 in the last 14 days",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 10,
                max: 1000,
                tickColor: "#5E5E5E",
                color: "black"
            },
            yaxis: {
                axisLabel: "Country/territroy name",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 3,
                tickColor: "#5E5E5E",
                ticks:ticks,
                color: "black"
            },
            legend: {
                noColumns: 0,
                labelBoxBorderColor: "#858585",
                position: "ne"
            },
            grid: {
                hoverable: true,
                borderWidth: 2,
                backgroundColor: { colors: ["#171717", "#4F4F4F"] }
            }
        };

        $.plot("#placeholder4",data_set,options);

}

function plotting_barchart2(response){


  $("#placeholder5").height(800);
  $("#placeholder5").width(1200);

  var raw_data = response.map(function f(value,index,array){
      value = [value[1],index];
      return value;
  });

  var data_set = [{label:"Total Cases by Country",data:raw_data,color:"#AB5800"}];

  var ticks = response.map(function f(value,index,array){
      value = [index,value[0]];
      return value;
  });

  function getFirst(value,index,array){
    return value[0];
  };

  values = raw_data.map(getFirst);
  max_value = values.reduce(function(a,b){
    return Math.max(a,b);
  });



  var options = {
            series: {
                bars: {
                    show: true
                }
            },
            bars: {
                align: "center",
                barWidth: 0.5,
                horizontal: true,
                fillColor: { colors: [{ opacity: 0.5 }, { opacity: 1}] },
                lineWidth: 1
            },
            xaxis: {
                axisLabel: "Total Cases",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 10,
                max: 2*max_value,
                tickFormatter: function formatter(val){
                  return  "<span>" +  val/1000 + "k</span>";
                },
                tickColor: "#5E5E5E",
                color: "black"
            },
            yaxis: {
                axisLabel: "Country/territroy name",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 3,
                tickColor: "#5E5E5E",
                ticks:ticks,
                color: "black"
            },
            legend: {
                noColumns: 0,
                labelBoxBorderColor: "#858585",
                position: "ne"
            },
            grid: {
                hoverable: true,
                borderWidth: 2,
                backgroundColor: { colors: ["#171717", "#4F4F4F"] }
            }
        };

        $.plot("#placeholder5",data_set,options);

}

function plotting_barchart3(response){

  $("#placeholder6").height(800);
  $("#placeholder6").width(1200);

  var raw_data = response.map(function f(value,index,array){
      value = [value[1],index];
      return value;
  });

  var data_set = [{label:"Deaths per Country",data:raw_data,color:"#AB5800"}];

  console.log(raw_data)

  var ticks = response.map(function f(value,index,array){
      value = [index,value[0]];
      return value;
  });

  console.log(ticks);


  function getFirst(value,index,array){
    return value[0];
  };

  values = raw_data.map(getFirst);
  max_value = values.reduce(function(a,b){
    return Math.max(a,b);
  });

  var options = {
            series: {
                bars: {
                    show: true
                }
            },
            bars: {
                align: "center",
                barWidth: 0.5,
                horizontal: true,
                fillColor: { colors: [{ opacity: 0.5 }, { opacity: 1}] },
                lineWidth: 1
            },
            xaxis: {
                axisLabel: "Total Deaths",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 10,
                max: 2*max_value,
                tickColor: "#5E5E5E",
                tickFormatter: function formatter(val){
                  return  "<span>" +  val/1000 + "k</span>";
                },
                color: "black"
            },
            yaxis: {
                axisLabel: "Country/territroy name",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 3,
                tickColor: "#5E5E5E",
                ticks:ticks,
                color: "black"
            },
            legend: {
                noColumns: 0,
                labelBoxBorderColor: "#858585",
                position: "ne"
            },
            grid: {
                hoverable: true,
                borderWidth: 2,
                backgroundColor: { colors: ["#171717", "#4F4F4F"] }
            }
        };

        $.plot("#placeholder6",data_set,options);

}

function plotting_barchart4(response){


  $("#placeholder7").height(800);
  $("#placeholder7").width(1200);

  var raw_data = response.map(function f(value,index,array){
      value = [value[1],index];
      return value;
  });

  var data_set = [{label:"Cases per population",data:raw_data,color:"#AB5800"}];

  console.log(raw_data)

  var ticks = response.map(function f(value,index,array){
      value = [index,value[0]];
      return value;
  });

  console.log(ticks);

  function getFirst(value,index,array){
    return value[0];
  };

  values = raw_data.map(getFirst);
  max_value = values.reduce(function(a,b){
    return Math.max(a,b);
  });

  var options = {
            series: {
                bars: {
                    show: true
                }
            },
            bars: {
                align: "center",
                barWidth: 0.5,
                horizontal: true,
                fillColor: { colors: [{ opacity: 0.5 }, { opacity: 1}] },
                lineWidth: 1
            },
            xaxis: {
                axisLabel: "Cases/Population in 2019",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 10,
                max: 1.5*max_value,
                tickColor: "#5E5E5E",
                color: "black"
            },
            yaxis: {
                axisLabel: "Country/territroy name",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 3,
                tickColor: "#5E5E5E",
                ticks:ticks,
                color: "black"
            },
            legend: {
                noColumns: 0,
                labelBoxBorderColor: "#858585",
                position: "ne"
            },
            grid: {
                hoverable: true,
                borderWidth: 2,
                backgroundColor: { colors: ["#171717", "#4F4F4F"] }
            }
        };

        $.plot("#placeholder7",data_set,options);

}

function plotting_barchart5(response){


  $("#placeholder8").height(800);
  $("#placeholder8").width(1200);

  var raw_data = response.map(function f(value,index,array){
      value = [value[1],index];
      return value;
  });

  var data_set = [{label:"Death per Population",data:raw_data,color:"#AB5800"}];

  console.log(raw_data)

  var ticks = response.map(function f(value,index,array){
      value = [index,value[0]];
      return value;
  });

  console.log(ticks);


  function getFirst(value,index,array){
    return value[0];
  };

  values = raw_data.map(getFirst);
  max_value = values.reduce(function(a,b){
    return Math.max(a,b);
  });

  var options = {
            series: {
                bars: {
                    show: true
                }
            },
            bars: {
                align: "center",
                barWidth: 0.5,
                horizontal: true,
                fillColor: { colors: [{ opacity: 0.5 }, { opacity: 1}] },
                lineWidth: 1
            },
            xaxis: {
                axisLabel: "Deather per Population",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 10,
                max: 1.5*max_value,
                tickColor: "#5E5E5E",
                color: "black"
            },
            yaxis: {
                axisLabel: "Country/territroy name",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 3,
                tickColor: "#5E5E5E",
                ticks:ticks,
                color: "black"
            },
            legend: {
                noColumns: 0,
                labelBoxBorderColor: "#858585",
                position: "ne"
            },
            grid: {
                hoverable: true,
                borderWidth: 2,
                backgroundColor: { colors: ["#171717", "#4F4F4F"] }
            }
        };

        $.plot("#placeholder8",data_set,options);

}

function plotting_barchart6(response){


  $("#placeholder9").height(800);
  $("#placeholder9").width(1200);

  var raw_data = response.map(function f(value,index,array){
      value = [value[1],index];
      return value;
  });

  var data_set = [{label:"Deathrate by Country",data:raw_data,color:"#AB5800"}];

  console.log(raw_data)

  var ticks = response.map(function f(value,index,array){
      value = [index,value[0]];
      return value;
  });

  console.log(ticks);


  function getFirst(value,index,array){
    return value[0];
  };

  values = raw_data.map(getFirst);
  max_value = values.reduce(function(a,b){
    return Math.max(a,b);
  });

  var options = {
            series: {
                bars: {
                    show: true
                }
            },
            bars: {
                align: "center",
                barWidth: 0.5,
                horizontal: true,
                fillColor: { colors: [{ opacity: 0.5 }, { opacity: 1}] },
                lineWidth: 1
            },
            xaxis: {
                axisLabel: "Deathrate",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 10,
                max: 1.5*max_value,
                tickColor: "#5E5E5E",
                color: "black"
            },
            yaxis: {
                axisLabel: "Country/territroy name",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 3,
                tickColor: "#5E5E5E",
                ticks:ticks,
                color: "black"
            },
            legend: {
                noColumns: 0,
                labelBoxBorderColor: "#858585",
                position: "ne"
            },
            grid: {
                hoverable: true,
                borderWidth: 2,
                backgroundColor: { colors: ["#171717", "#4F4F4F"] }
            }
        };

        $.plot("#placeholder9",data_set,options);

}
