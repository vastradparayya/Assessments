function submit_test(){
	
	// alert(question);
	// alert(document.getElementById('option_a1').checked)
	var dict = {};
	questions = [];
	var elms = document.getElementById('main_div').children;
    for (var i = 1; i < elms.length+1; i++) {
        var question = document.getElementById("question"+i).innerHTML;
        if(document.getElementById('chk_option_a'+i).checked){
        	var option_a_val = document.getElementById('option_a'+i).innerHTML
        }else{
        	var option_a_val = '';
        }
        if(document.getElementById('chk_option_b'+i).checked){
        	var option_b_val = document.getElementById('option_b'+i).innerHTML
        }else{
        	var option_b_val = '';
        }
        if(document.getElementById('chk_option_c'+i).checked){
        	var option_c_val = document.getElementById('option_c'+i).innerHTML
        }else{
        	var option_c_val = '';
        }
        if(document.getElementById('chk_option_d'+i).checked){
        	var option_d_val = document.getElementById('option_d'+i).innerHTML
        }else{
        	var option_d_val = '';
        }

        dict['question'+i] = question
        dict['option_a'+i] = option_a_val
        dict['option_b'+i] = option_b_val
        dict['option_c'+i] = option_c_val
        dict['option_d'+i] = option_d_val

        if ((option_a_val == '') && (option_b_val == '') && (option_c_val == '') && (option_d_val== '')){
        	alert("Select atleast one option in "+i+"th question");
        	return false;
        }

        questions.push(dict)
        dict = {}
    }
 
    event.preventDefault();
    $.ajax({
      type: "POST",
      url: "/submit_test/",
      data: {
        'data': JSON.stringify(questions)
      },
      success: function (response) {

            window.location.href = '/';
      }
    });
    return false;
}

function chat(){
    var sel = document.getElementById('chat')
    user = sel.value
    if(user === "--select--"){
        alert("Select user to chat")
        return false;
    }
    else{
        $.ajax({
          type: "POST",
          url: "/chat/",
          data: {
            // 'user': JSON.stringify(questions)
            'user': user
          },
          success: function (response) {
            $("dddd").html(response)
                // window.location.href = '/';
          }
        });
        return false;
    }
    
}