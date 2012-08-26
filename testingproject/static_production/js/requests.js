function removeRequestInstance(obj, id) {
	row = $(obj).parents(".log_instance");
	
	if (confirm('Are you sure you want to delete this instance?')) {
		$.getJSON("/remove/?id=" + id, { }, function() {
			$(obj).parents(".log_instance").animate({opacity: 'hide'}, "slow");
			});
	}
}
