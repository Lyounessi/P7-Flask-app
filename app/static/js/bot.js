$(document).ready(function(){
    let mediaDiv = document.createElement('div');
    $.get('app/mediaAnswer.txt', function(data, status){
        $(mediaDiv).html(data);
        console.log(status);
        console.log(mediaDiv);
    });
});