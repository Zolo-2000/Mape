
(function($){
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

