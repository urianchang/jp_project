$('#test').submit(function(event){
    if ($("#guess").val() == $("#answer").val()) {
        $("span").text("Good job!").show();
        return;
    }

    $("span").text("WRONG!").show().fadeOut(3000)
    event.preventDefault();
});
