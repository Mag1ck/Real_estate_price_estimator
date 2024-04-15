function getRoomValue() {
  var uiRooms = document.getElementsByName("uiRooms");
  for(var i in uiRooms) {
    if(uiRooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getbuilding_ownershipValue() {
  var uibuilding_ownership = document.getElementsByName("uibuilding_ownership");
  for(var i in uibuilding_ownership) {
    if(uibuilding_ownership[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var uiarea = document.getElementById("uiarea");
  var uifloor = document.getElementById("uifloor");
  var rent = document.getElementById("rent");
  var location = document.getElementById("uiLocations");
  var building_ownership = document.getElementById("building_ownership");
  var construction_status = document.getElementById("construction_status");
  var outdoor = document.getElementById("Outdoor");
  var heating = document.getElementById("Heating");
  var car = document.getElementById("car");
  var rooms = getRoomValue();
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/get_estimated_price"

  $.post(url, {
      area: parseFloat(uiarea.value),
      floor: parseFloat(uifloor.value),
      rent: parseInt(rent.value),
      location: location.value,
      building_ownership: parseInt(building_ownership.value),
      construction_status: parseInt(construction_status.value),
      outdoor: parseInt(outdoor.value),
      heating: parseInt(heating.value),
      car: parseInt(car.value),
      rooms: rooms
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toLocaleString('en-US') + " PLN</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_data"
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
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

window.onload = onPageLoad;