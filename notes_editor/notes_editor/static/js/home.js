$(document).ready(function() {
alert("namita")
    $(document).on('click', '#create_folder', function() {
  alert("hello")
   var folder_name = $('#folder_name').val()

    var data = {'folder_name': folder_name }

	$.ajax({
            type: 'POST',
            url: '/create_folder/',
            data: JSON.stringify(data),
            dataType: 'json',
            success: function(response) {
                alert(response.status)
            },
            error: function() {
                alert('Something went wrong');
            }
   });
   });

  });