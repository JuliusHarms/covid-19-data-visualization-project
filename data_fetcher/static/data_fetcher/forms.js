// wait for the DOM to be loaded
$(document).ready(function() {
    // bind 'myForm' and provide a simple callback function
      $('#myForm').ajaxForm({url:"records",
                             dataType:"json",
                             success: function (response){
                                plotting_linechart(response);
                             }
                          });

      $('#myForm2').ajaxForm({url:"countries_by_infectionrate",
                             dataType:"json",
                             success: function (response){
                                plotting_barchart(response);
                             }
                          });

      $('#myForm3').ajaxForm({url:"total_stats_country",
                              dataType:"json",
                              success: function (response){
                                $("#country_data1").text(response[0]);
                                $("#country_data2").text(response[1]);
                                $("#country_data3").text(response[2]);
                                $("#country_data4").text(response[3]);
                                $("#country_data5").text(response[4]);
                                $("#country_data6").text(response[5]);
                              }
                         });
        });

        $('#myForm4').ajaxForm({url:"countries_by_sum_cases",
                             dataType:"json",
                             success: function (response){
                                plotting_barchart2(response);
                             }
                          });

        $('#myForm5').ajaxForm({url:"countries_by_sum_deaths",
                             dataType:"json",
                             success: function (response){
                                plotting_barchart3(response);
                             }
                          });

      $('#myForm6').ajaxForm({url:"countries_by_cases_per_pop",
                             dataType:"json",
                             success: function (response){
                                plotting_barchart4(response);
                             }
                          });

      $('#myForm7').ajaxForm({url:"countries_by_deaths_per_pop",
                             dataType:"json",
                             success: function (response){
                                plotting_barchart5(response);
                             }
                          });

      $('#myForm8').ajaxForm({url:"countries_by_deathrate",
                             dataType:"json",
                             success: function (response){
                                plotting_barchart6(response);
                             }
                          });
