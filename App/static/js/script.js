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

// EDIT PATIENT MODAL
    $('table').on('click', 'button.edit_patient_click',function (ele) {
        //the <tr> variable is use to set the parentNode from "ele
        var tr = ele.target.parentNode.parentNode;

        //I get the value from the cells (td) using the parentNode (var tr)
        var patient_id = tr.cells[1].textContent;
        var patient_firstname = tr.cells[2].textContent;
        var patient_lastname = tr.cells[3].textContent;
        var patient_email = tr.cells[4].textContent;
        var patient_age = tr.cells[5].textContent;
        var patient_gender = tr.cells[6].textContent;
        var patient_phone = tr.cells[7].textContent;
        var patient_note = tr.cells[8].textContent;
        var patient_created = tr.cells[9].textContent;

        console.log(patient_id);
        //Prefill the fields with the gathered information
        $('h5.modal-title').html('Edit Patient: '+patient_firstname+' '+patient_lastname+' id:'+patient_id);
        
        $('#patient_firstname').val(patient_firstname);
        $('#patient_lastname').val(patient_lastname);
        $('#patient_email').val(patient_email);
        $('#patient_age').val(patient_age);
        $('#patient_gender').val(patient_gender).attr('selected', 'selected');
        $('#patient_phone').val(patient_phone);
        $('#patient_note').val(patient_note);
        $('#patient_created_at').val(patient_created);

        $("#edit_patient_modal").modal("show");
        //If you need to update the form data and change the button link
        // $("form#ModalForm").attr('action', window.location.href+'/update/'+id);
        // $("a#saveModalButton").attr('href', window.location.href+'/update/'+id);
    });


    // $("#edit_patient_click").click(function(){
    //     var $row = $(this).closest('tr');
    //     var patient_id = $row.find('#patient_id').text();
    //     var firstname =  $row.find('#firstname').text();
    //     var lastname =  $row.find('#lastname').text();
    //     var email =  $row.find('#email').text();
    //     var age =  $row.find('#age').text();
    //     var gender =  $row.find('#gender').text();
    //     var phone =  $row.find('#phone').text();
    //     var note =  $row.find('#note').text();
    //     var created_at =  $row.find('#created_at').text();
        
    //     console.log(patient_id);
    //     // $('#patient_firstname').val(firstname);
    //     // $('#patient_lastname').val(lastname);
    //     // $('#patient_email').val(email);
    //     // $('#patient_age').val(age);
    //     // $('#patient_gender').val(gender);
    //     // $('#patient_phone').val(phone);
    //     // $('#patient_note').val(note);
    //     // $('#patient_created_at').val(created_at);
    // });

 });