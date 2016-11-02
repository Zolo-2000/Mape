$(document).ready(function() {
  $('.modal-trigger').leanModal();
  $('input#input_text, textarea#textarea1').characterCounter();
  $('.parallax').parallax();
  $('select').material_select('destroy');
  $('.button-collapse').sideNav();
  $('.collapsible').collapsible({
      accordion: false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
  });
  $('.fixed-action-btn').closeFAB();
  $('.dropdown-button').dropdown({
        inDuration: 300,
        outDuration: 225,
        constrain_width: false, // Does not change width of dropdown to that of the activator
        hover: true, // Activate on hover
        gutter: 0, // Spacing from edge
        belowOrigin: false // Displays dropdown below the button
      }
    );
  $('ul.tabs').tabs();
  $('.tooltipped').tooltip({delay: 50});
  $('.materialboxed').materialbox();
  $('.slider').slider({full_width: true});
  
  var options = [{selector: '.class', offset: 200, callback: 'globalFunction()' },
  {selector: '.other-class', offset: 200, callback: 'globalFunction()' }];
  WebFontConfig = {
    google: { families: [ 'Comfortaa:400,700,300:latin' ] }
  };
});