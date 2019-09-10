$(document).ready(function(){
    $('#email').keyup(function(){
        var data = $("#regForm").serialize()
        $.ajax({
            method: "POST",
            url: "/check-em",
            data: data
        })
        .done(function(res){
            $('#emailMsg').html(res)
        })
    })
})