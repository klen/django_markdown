// -------------------------------------------------------------------
// markItUp!
// -------------------------------------------------------------------
// Copyright (C) 2008 Jay Salvat
// http://markitup.jaysalvat.com/
// -------------------------------------------------------------------
// MarkDown tags example
// http://en.wikipedia.org/wiki/Markdown
// http://daringfireball.net/projects/markdown/
// -------------------------------------------------------------------
// Feel free to add more tags
// -------------------------------------------------------------------

// mIu nameSpace to avoid conflict.
miu = (function($){
    
    var settings = {
        onShiftEnter:       {keepDefault:false, openWith:'\n\n'},
        markupSet: [
            {name:'First Level Heading', key:'1', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '=') } },
            {name:'Second Level Heading', key:'2', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '-') } },
            {name:'Heading 3', key:'3', openWith:'### ', placeHolder:'Your title here...' },
            {name:'Heading 4', key:'4', openWith:'#### ', placeHolder:'Your title here...' },
            {name:'Heading 5', key:'5', openWith:'##### ', placeHolder:'Your title here...' },
            {name:'Heading 6', key:'6', openWith:'###### ', placeHolder:'Your title here...' },
            {separator:'---------------' },     
            {name:'Bold', key:'B', openWith:'**', closeWith:'**'},
            {name:'Italic', key:'I', openWith:'_', closeWith:'_'},
            {separator:'---------------' },
            {name:'Bulleted List', openWith:'- ' },
            {name:'Numeric List', openWith:function(markItUp) {
                return markItUp.line+'. ';
            }},
            {separator:'---------------' },
            {name:'Picture', key:'P', replaceWith:'![[![Alternative text]!]]([![Url:!:http://]!] "[![Title]!]")'},
            {name:'Link', key:'L', openWith:'[', closeWith:']([![Url:!:http://]!] "[![Title]!]")', placeHolder:'Your text to link here...' },
            {separator:'---------------'},  
            {name:'Quotes', openWith:'> '},
            {name:'Code Block / Code', openWith:'(!(\t|!|`)!)', closeWith:'(!(`)!)'},
            {separator:'---------------'},
            {name:'Preview', call:'preview', className:"preview"}
        ]
    };
    
    function getCookie(name) {
        var value = null;
        
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    value = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        
        return value;
    }
    
    /*
     * Add "X-CSRFToken" header to every AJAX request within current domain
     * */
    $('html').ajaxSend(function(event, xhr, settings) {
        var isLocal = !settings.url.match(/^https?:\/\/([^\/]+)/i);
        
        if(isLocal || RegExp.$1 == document.location.host){
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    })
    
    
    return {
        settings: settings,
        
        /*
         * work around bug in python-markdown where header underlines must be at least 3 chars
         * */
    	markdownTitle: function(markItUp, char) {
    		heading = '';
    		n = $.trim(markItUp.selection || markItUp.placeHolder).length;
    		if (n < 3) { n = 3; }
    		for(i = 0; i < n; i++) {
    			heading += char;
    		}
    		return '\n'+heading;
    	},
        
        /*
         * Shortcut for initializing editor
         * */
        init: function(textareId, extraSettings){
            $(document).ready(function() {
                $('#' + textareId).markItUp($.extend(settings, extraSettings));
            });
        }
        
    }
    
})(jQuery || django.jQuery);
