function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqm = document.getElementById("uiSqm");
    var roomnum = document.getElementById("uiRoomnum");
    var addcost = document.getElementById("uiAddcost");
    var flattype = document.getElementById("uiFlattype");
    var heattype = document.getElementById("uiHeattype");
    var roomcon = document.getElementById("uiRoomcon");
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        livingSpace: parseFloat(sqm.value),
        noRooms: parseFloat(roomnum.value),
        additionCost: parseFloat(addcost.value),
        typeOfFlat: flattype.value,
        heating_type: heattype.value,
        condition: roomcon.value,
        regio2: location.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Euro</h2>";
        console.log(status);
    });
  }
  


function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var flattype = data.flattype;
            var uiFlattype = document.getElementById("uiFlattype");
            $('#uiFlattype').empty();
            for(var i in flattype) {
                var opt = new Option(flattype[i]);
                $('#uiFlattype').append(opt);
            }
            var heattype = data.heattype;
            var uiHeattype = document.getElementById("uiHeattype");
            $('#uiHeattype').empty();
            for(var i in heattype) {
                var opt = new Option(heattype[i]);
                $('#uiHeattype').append(opt);
            }
            var roomcon = data.roomcon;
            var uiRoomcon = document.getElementById("uiRoomcon");
            $('#uiRoomcon').empty();
            for(var i in roomcon) {
                var opt = new Option(roomcon[i]);
                $('#uiRoomcon').append(opt);
            }
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }

window.onload = onPageLoad