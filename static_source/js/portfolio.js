$(document).ready(function() {
    $('.portfolio li').hover( function() {
        $(this).find('h5').slideDown();
    }, function(){
        $(this).find('h5').slideUp();
    });
});