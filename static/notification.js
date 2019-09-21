$("off").click(function(){
alert($(this).text());
    $("off").not($(this)).unbind('click');
});