// Fetch data when user submit the form
$('form').submit( (e)=>{

        e.preventDefault();
        $('.col-md-4').detach();
        $('#loading').show();
        $('#error').hide();

            $.ajax({
                url: '/data',
                data: $('form').serialize(),
                type: "POST",
                success: function(response) {
                            console.log(response);
                            $.fn.inseart_result(response);
                            $('#loading').hide();
                            $('#lat').removeAttr('value');
                            $('#lng').removeAttr('value');

                    },
                error: function(error) {
                            console.log(error);
                            $('#loading').hide();
                            $('#error').show();
                            $('#lat').removeAttr('value');
                            $('#lng').removeAttr('value');
                    }
                });
    });


// Create HTML block, and append it on the page
$.fn.inseart_result = (data)=> {

        var index = 0;
        var obj = $.parseJSON(data);

        $.each(obj, (_, value)=>{
            $.each(value, (k,v)=>{
         
                var ele = "<div class='col-md-4 box'>";
                    ele += " <h2>" + k + "</h2>";
                    ele += " <div class='clearfix'>";
                    ele += "   <div id='barlength' class='c100 p" + v.split(".")[0] + " center '>";
                    ele += "   <span id=perc>" + v  + "</span>";
                    ele += "   <div class='slice'>";
                    ele += "   <div class='bar'></div>";
                    ele += "   <div class='fill'></div>";
                    ele += "</div></div></div>";
                
              $('#results').append(ele);
            });
        });
    };