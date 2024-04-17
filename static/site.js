$(document).ready(function(){
    $("#next_button").click(function(){
        // Handle next button click
        if("{{question.next_q}}" == "end"){
            window.location.href = "/";
        } else {
            window.location.href = "/quiz/{{question.next_q}}";
        }
    });

    $("#prev_button").click(function(){
        // Handle previous button click
        if("{{question.prev_q}}" == "beg"){
            window.location.href = "/";
        } else {
            window.location.href = "/quiz/{{question.prev_q}}";
        }
    });
});