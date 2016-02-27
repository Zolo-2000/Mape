(function($){
  L.mapbox.accessToken = 'pk.eyJ1Ijoiem9sbyIsImEiOiJ0VlphRlZFIn0.gLAS81dTkxi1W5FqVMKwXg';
  var map = L.mapbox.map('map', 'zolo.lkgcf241').setView([-130.39, -78.56], 13);
  
  addCurrentLocationToMap = function() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position){
        var lat= position.coords.latitude,
        long = position.coords.longitude;
        console.log('--- Tu posision actual es: ---');
        console.log('Lat: ', + lat);
        console.log('Long: ', + long);
        console.log('---------------------------');
        var marker = L.marker([lat, long]).addTo(map);
        marker.bindPopop('Estas en: <br>' + lat + ', ' + long).openPopup();
       });
    }else{
      console.log("No dispones de geolocalizacion en tu navegador")
    }
  }
  $("#CurrentLocation").click(addCurrentLocationToMap);

  var options = [
  {selector: '.class', offset: 200, callback: 'globalFunction()' },
  {selector: '.other-class', offset: 200, callback: 'globalFunction()' }
    
  ];
    WebFontConfig = {
    google: { families: [ 'Comfortaa:400,700,300:latin' ] }
  };
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

