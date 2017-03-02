$('#step1').submit(function(event){
    if ($("#userp1").val() == $("#p1").val()) {
        $("#msg").text("Good job!").show();
        return;
    }

    $("#msg").text("WRONG!").show().fadeOut(3000)
    event.preventDefault();
});

$('#step2').submit(function(event){
    if ($("#userp1").val() == $("#p1").val() && $("#userp2").val() == $("#p2").val()) {
        $("#msg").text("Good job!").show();
        return;
    }

    $("#msg").text("WRONG!").show().fadeOut(3000)
    event.preventDefault();
});

$('#step5').submit(function(event){
    if ($("#userp1").val() == $("#p1").val() && $("#userp2").val() == $("#p2").val() && $("#userp3").val() == $("#p3").val()) {
        $("span").text("Good job!").show();
        return;
    }

    $("span").text("WRONG!").show().fadeOut(3000)
    event.preventDefault();
});

$('#step3').submit(function(event){
    if ($("#userp1").val() == $("#p1").val() && $("#userp2").val() == $("#p2").val() && $("#userp3").val() == $("#p3").val()) {
        $("#msg").text("Good job!").show();
        return;
    }

    $("#msg").text("WRONG!").show().fadeOut(3000)
    event.preventDefault();
});
