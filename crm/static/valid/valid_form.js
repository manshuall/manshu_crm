$(document).ready(function(){
    $('#id_username').keyup(function(){
        myfun();
    })
    function myfun()
    {

        //user name validation for only view messages

        var user_val= $('#id_username').val();
        if(user_val.length=='')
        {
            $('label:first').html("Enter User name")
            $('label:first').css("color","red");
        }
        else if(user_val.length>50)
        {
            $('label:first').html("User must be less than 20")
            $('label:first').css("color","red");
        }
        else if(user_val.length<3)
        {
            $('label:first').html("Enter Valid User name")
            $('label:first').css("color","red");
        }
        else
        {
            $('label:first').html("Username*")
            $('label:first').css("color","#858796");
        } 
        
    }

     //Password name validation for only view messages
     $('#id_password').keyup(function(){
         var pass_val=$('#id_password').val();
         if(pass_val.length=='')
         {
            $('label[for="id_password"]').html("Plese Enter Password")
            $('label[for="id_password"]').css("color","red");
         }
         else if(pass_val.length<6)
        {
            $('label[for="id_password"]').html("Password must be grater than 6 digit")
            $('label[for="id_password"]').css("color","red");
        }
        else
        {
            $('label[for="id_password"]').html("Password*")
            $('label[for="id_password"]').css("color","#858796");
        } 

     })
})