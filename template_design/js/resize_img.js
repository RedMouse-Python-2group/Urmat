$(document).ready(function(){
    $(".zoomIn").click(function(){
        $("#resize-img img").animate({
            height: '+=10px',
            width: '+=10px'
        });
    });
    
    $(".zoomOut").click(function(){
         $("#resize-img img").animate({
            height: '-=10px',
            width: '-=10px'
        });
    })
});