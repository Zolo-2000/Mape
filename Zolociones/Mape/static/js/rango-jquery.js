$(document).ready(function() {
			$("#about-btn").click( function(event) {
        		alert("You clicked the button using JQuery!");
    		});
            $('.modal-trigger').leanModal();
            $('input#input_text, textarea#textarea1').characterCounter();
            $('.parallax').parallax();
            $('select').material_select('destroy');
});