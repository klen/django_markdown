// Starting from Django 1.6+, jQuery is only available as 'django' object attribute.
// Unfortunately, it's not compatible with markitup.js library because it needs global jQuery variable to be initialized.
jQuery = jQuery || django.jQuery;
