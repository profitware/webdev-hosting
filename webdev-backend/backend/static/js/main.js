// DOM is ready
$(document).ready(function () {
	
	// deal with selecting appended element
	
	$('.navbar-header').on('click', '.logout-btn', function () { $.get('/logout'); setTimeout(function () {  location.reload(); }, 1000); })
	

	
	$('.logon-btn').click(function () {
		
		uname = $('#uname').val();
		pwd = $('#pwd').val();
		$.post('/?uname=' + uname + '&pwd=' + pwd,  function( resp ) {
			
			if ( resp != 'loginFailure') {
				
				$('form').remove();
				$('.navbar-header').append('Logggged as: ' + uname + '<button type="submit" class="btn btn-default logout-btn">Log out</button>');
				
			}
			else {
			
			alert('Login unsuccessful')
			
			}
		});

	});
	
});
	
	
