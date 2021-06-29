// JavaScript Document

    var i=0;
	var m;
	$(".hbut").hide();
	$("#main").hover(function(){
		$(".hbut").show();	
},function(){
		$(".hbut").hide();
	});

	$(document).ready(function(){
		setInterval( function autodo(){
	i++;
	if(i>5){i=1}
	doit(i);
		
},1420);
$(".anvli").hover(function(){
			 i = $(this).val();
			 doit(i);		
});
$("#pre").click(function(){
			 i--;
			 if(i<0){i=5}
			 doit(i);		
});
$("#next").click(function(){
			 i++;
			 if(i>5){i=1}
			 doit(i);		
});
});
function doit(i){
		 m = -1050*(i-1);
		 $(".anvli").removeClass("navnow");
		 $("#navli"+i).addClass("navnow");
		 $("#picbox").stop(true, true).animate({"left":m+"px"},1050);
}
