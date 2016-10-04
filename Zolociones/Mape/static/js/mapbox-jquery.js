(function($){
// Provide your access token
L.mapbox.accessToken = '{{ MAPBOX_ACCESS_TOKEN }}';
// Create a map in the div #map
var map = L.mapbox.map('map', 'mapbox.light', {
}).setView([-1.67, -78.66], 14);

map.on('contextmenu', function(e) {
  alert(e.latlng);
});

var tile = map.getTileJSON();

L.mapbox.featureLayer({
    // this feature is in the GeoJSON format: see geojson.org
    // for the full specification
    type: 'Feature',
    geometry: {
        type: 'Point',
        // coordinates here are in longitude, latitude order because
        // x, y is the standard for GeoJSON and many formats
        coordinates: [
          -1.67, -78.66
        ]
    },
    properties: {
        title: 'Peregrine Espresso',
        description: '1718 14th St NW, Washington, DC',
        // one can customize markers by adding simplestyle properties
        // https://www.mapbox.com/guides/an-open-platform/#simplestyle
        'marker-size': 'large',
        'marker-color': '#BE9A6B',
        'marker-symbol': 'cafe'
    }
}).addTo(map);

addCurrentLocationToMap = function() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position){
      var lat= position.coords.latitude,
      longit = position.coords.longitude;
      console.log('--- Tu posision actual es: --- {{ MAPBOX_ACCESS_TOKEN }}');
      console.log('Lat: ', + lat);
      console.log('Long: ', + longit);
      console.log('---------------------------');
      var marker = L.marker([lat, longit], {
        icon: L.mapbox.marker.icon({
      'marker-size': 'large',
      'marker-symbol': 'bus',
      'marker-color': '#fa0'})
      });
      marker.addTo(map);
      marker.bindPopup('Estas en: <br>' + lat + ', ' + longit).openPopup();
    });
  }else{
    console.log("No dispones de geolocalizacion en tu navegador")
  }
};

// 
(function() {
  var wf = document.createElement('script');
  wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
    '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
  wf.type = 'text/javascript';
  wf.async = 'true';
  var s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(wf, s);
})// end of document ready
})(jQuery); 
//// end of jQuery name space

