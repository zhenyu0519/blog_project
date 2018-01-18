$(document).ready(function(){
   // get current position
   if(navigator.geolocation){
       navigator.geolocation.getCurrentPosition(showPosition);
   } else{
       //gonna use the react.js here if nothing show then hide this part
       console.log('Nothing show here')
   }

   // show lon and lat
   function showPosition(position){
       var lat = position.coords.latitude;
       var lon = position.coords.longitude;
       getWeather(lat, lon);
       // may return something else
       return;
   }

   // get the weather forecast from yahoo weather api
    function getWeather(lat, lon) {
        $.ajax({
            //this is the endpoint
            url:"https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"" +
            "("+lat+", "+lon+")\") and u = 'c'"+
            "&format=json&env=store://datatables.org/alltableswithkeys",
            success: function(response){
                showInfo(response);
            },
            error: function(){
              console.log("error is " + err);
            }
        })
    }
    //gonna use react.js here later
    function showInfo(response){
       console.log("hello " + response);
        $("#weather-icon").attr("src","http://l.yimg.com/a/i/us/we/52/"+response.query.results.channel.item.condition.code+".gif");
        $("#location").html("<h3>" +response.query.results.channel.location.city+ ", "+response.query.results.channel.location.region+"</h3>");
        $("#date").html("<p>"+response.query.results.channel.lastBuildDate+"</p>");
        $("#current").html("<h3>"+response.query.results.channel.item.condition.temp+" &#8451; </h3>");
        $("#description").html("<h4>"+response.query.results.channel.item.condition.text+"</h4>");
        $("#min-max").html("<h4>"+response.query.results.channel.item.forecast[0].low+" &#8451; ~ "+response.query.results.channel.item.forecast[0].high+" &#8451; </h4>");
        $("#description-tomorrow").html("<p> Weather of Tomorrow: "+response.query.results.channel.item.forecast[1].text+"</p>");
    }
});