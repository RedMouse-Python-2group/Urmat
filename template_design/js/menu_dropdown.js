$(document).ready(function(){
   $('#main-nav li').hover(
       function(){$('ul:first',this).slideDown(250);},
       function(){$('ul:first',this).slideUp(250);});
});