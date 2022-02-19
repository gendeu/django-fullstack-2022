$(document).ready(function(){
    
    
    // LOGIN FORM CONTROL
    $("#username").on('keyup',function(){
        $("#close_alert_login").click();
        var countusername = this.value.length;
        if(countusername >= 7){
            $("#username_warning").text("");

            $("#username").addClass("is-valid");
            $("#username").removeClass("is-invalid");
        }else{
            $("#username_warning").text("*Must minimum of 7 characters");
            
            $("#username").removeClass("is-valid");
            $("#username").addClass("is-invalid");

        }
       //Code 
    });
    $("#password").on('keyup',function(){
        $("#close_alert_login").click();
        var countpassword = this.value.length;
        if(countpassword >= 7){
            $("#password_warning").text("");

            $("#password").addClass("is-valid");
            $("#password").removeClass("is-invalid");
        }else{
            $("#password_warning").text("*Must minimum of 7 characters");
            
            $("#password").removeClass("is-valid");
            $("#password").addClass("is-invalid");

        }
       //Code 
     });

     $('[data-toggle="tooltip"]').tooltip();
	
	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
 });