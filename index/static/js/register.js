$(function () {
    let registerStatus= 0;
    $('input[name="phone"]').blur(
        function () {
            if ($(this).val().trim().length == 0)
                return;
            $.get('/check_phone', {'phone': $(this).val()},
                function (data) {
                    $("#phone-tip").html(data.data);
                    registerStatus = data.status;
                    if (data.status == 1) {
                        $("#phone-tip").css('color', 'red');

                    } else {
                        $("#phone-tip").css('color', 'green');
                    }
                }, 'json');
            $("#form").submit(function () {
                if(registerStatus == 1){
                    return false;
                }else{
                    return true;
                }
            })
        }
    )

});



