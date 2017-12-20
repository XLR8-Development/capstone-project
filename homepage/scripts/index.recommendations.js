(function(context) {

    // utc_epoch comes from index.py
    console.log('Current epoch in UTC is ' + context.utc_epoch);

    var options = {
        target: '#ajax_test',
    }

    $('#formlib-inputform').ajaxForm(options);

})(DMP_CONTEXT.get());

$(function() {
  var options = {
      target: '#ajax_test',
  }

  $('#formlib-inputform').ajaxForm(options);
})

// Function for counting characters
$("#id_tweet").on('input', function(){
    var currentLength = this.value.length;

    $('#charNum').text((140 - currentLength) + " characters remaining");
    if (currentLength < 50) {
      $('#charNum').css('color', '#000000');
    } else {
      $('#charNum').css('color', '#ff0000');
    }
});



// update button
// $('.btn.btn-primary').click(function() {
//     $('#ajax_test').load('/homepage/index.recommendations');
// });
