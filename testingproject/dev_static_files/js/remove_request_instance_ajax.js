function removeRequestInstance(obj, id) {
	row = $(obj).parents(".row");
	
	if (confirm('Are you sure you want to delete this instance?')) {
		$.getJSON("/remove/?id=" + id, { }, function() {
			$(obj).parents(".row").animate({opacity: 'hide'}, "slow");
			});
	}
}
