$(document).ready(function(){

    // $("#unit2-lock").addClass("disabled");
    // $("#final-lock").addClass("disabled");

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

    $("#next_unit").click(function(){
        $("#unit2-lock").removeClass("disabled").addClass("btn btn-primary");
        window.location.href = "/";

    });
});