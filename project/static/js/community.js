$('#c_frame_sb_u_co').on('click' ,function(){
    if($("#c_frame_sb").width() == 325){

        framemoving(100, 1000,"right","left");
        $('#c_frame_sb_d').removeClass("act");


    }else{
        framemoving(325,775,"left","right");
        $('#c_frame_sb_d').addClass("act");

    }

});

function framemoving(swidth, mwidth, A_add, A_remo){

    $('#c_frame_sb').css({"width" : swidth, "transition": "all 400ms 0s ease"})
    $('#c_frame_mc').css({"width" : mwidth, "transition": "all 400ms 0s ease"})

    $("#sb_cont").removeClass("dli-arrow-" + A_remo);
    $("#sb_cont").addClass("dli-arrow-"+A_add);



}


$("#info").on('click' , function(){
    $("#hide_ui_sendimg").toggle();

});



$("#stamp").on('click' , function(){
    $("#hide_ui_stamp").toggle();

});