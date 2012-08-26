$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

function removeRequestInstance(obj, id) {
	if (confirm('Are you sure you want to delete this instance?')) {
		$.ajax({
			type:		"POST",
			url:		delurl + "?id=" + id,
			data:		{
				"request_id": id
			},
			dataType:	"json",
			success:	function(data) {
				if (data['success']) {
					row = $(obj).parents(".log_instance");
					$(obj).parents(".log_instance").animate({opacity: 'hide'}, "slow");
				}
				else {
					alert("Something went wrong! Try again later.");
				}
			}
		})
	}
}
