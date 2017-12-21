(function(context) {

    // utc_epoch comes from index.py
    console.log('Current epoch in UTC is ' + context.utc_epoch);
    $('.loader').hide();

})(DMP_CONTEXT.get());

$(function() {

  console.log('Test');
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

$('.btn.btn-primary').click(function() {
  $('.loader').show();
});

// update button
// $('.btn.btn-primary').click(function() {
//     $('#ajax_test').load('/homepage/index.recommendations');
// });
