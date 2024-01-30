$(document).ready(function(){
    $('#toggle_change').click(function(){
        $.ajax({
            url: '/toggle',
            type: 'POST',
            success: function(response){
                location.reload();
            }
        });
    });
});