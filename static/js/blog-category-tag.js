$(document).ready(function(){
    var classArray = ["badge badge-primary", "badge badge-secondary","badge badge-success",
    "badge badge-danger","badge badge-warning","badge badge-info","badge badge-dark"];

    $(".blog-category-tag span").each(function(){
       $(this).addClass(classArray[Math.floor(Math.random()*classArray.length)]);
    });
});