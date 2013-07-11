// -------------------------------------------------------------------
// markItUp!
// -------------------------------------------------------------------
// Copyright (C) 2008 Jay Salvat
// http://markitup.jaysalvat.com/
// -------------------------------------------------------------------


// mIu nameSpace to avoid conflict.
miu = (function($){
    
    var editors = {};
    
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
     * Work around bug in python-markdown where header underlines must be at least 3 chars
     * */
    function markdownTitle(markItUp, char) {
        heading = '';
        n = $.trim(markItUp.selection || markItUp.placeHolder).length;
        if (n < 3) { n = 3; }
        for(i = 0; i < n; i++) {
            heading += char;
        }
        return '\n'+heading;
    }
    
    /*
     * Default editors configuration
     * */
    var settings = {
        onShiftEnter:   {keepDefault:false, openWith:'\n\n'},
        nameSpace:     'markdown',
        
        /* 
         * MarkDown tags
         * http://en.wikipedia.org/wiki/Markdown
         * http://daringfireball.net/projects/markdown/
         * */
        
        markupSet: [
            {name:'First Level Heading', key:'1', placeHolder:'Your title here...', closeWith:function(markItUp) { return markdownTitle(markItUp, '=') }, className: 'miu-icon miu-icon-h1' },
            {name:'Second Level Heading', key:'2', placeHolder:'Your title here...', closeWith:function(markItUp) { return markdownTitle(markItUp, '-') }, className: 'miu-icon miu-icon-h2' },
            {name:'Heading 3', key:'3', openWith:'### ', placeHolder:'Your title here...', className: 'miu-icon miu-icon-h3' },
            {name:'Heading 4', key:'4', openWith:'#### ', placeHolder:'Your title here...', className: 'miu-icon miu-icon-h4' },
            {name:'Heading 5', key:'5', openWith:'##### ', placeHolder:'Your title here...', className: 'miu-icon miu-icon-h5' },
            {name:'Heading 6', key:'6', openWith:'###### ', placeHolder:'Your title here...', className: 'miu-icon miu-icon-h6' },
            {separator:'---------------' },     
            {name:'Bold', key:'B', openWith:'**', closeWith:'**', className: 'miu-icon miu-icon-bold'},
            {name:'Italic', key:'I', openWith:'_', closeWith:'_', className: 'miu-icon miu-icon-italic'},
            {separator:'---------------' },
            {name:'Bulleted List', openWith:'- ', className: 'miu-icon miu-icon-list-bullet' },
            {name:'Numeric List', openWith:function(markItUp) {
                return markItUp.line+'. ';
            }, className: 'miu-icon miu-icon-list-numeric'},
            {separator:'---------------' },
            {name:'Picture', key:'P', replaceWith:'![[![Alternative text]!]]([![Url:!:http://]!] "[![Title]!]")', className: 'miu-icon miu-icon-picture'},
            {name:'Link', key:'L', openWith:'[', closeWith:']([![Url:!:http://]!] "[![Title]!]")', placeHolder:'Your text to link here...', className: 'miu-icon miu-icon-link' },
            {separator:'---------------'},  
            {name:'Quotes', openWith:'> ', className: 'miu-icon miu-icon-quotes'},
            {name:'Code Block / Code', openWith:'(!(\t|!|`)!)', closeWith:'(!(`)!)', className: 'miu-icon miu-icon-code'},
            {separator:'---------------'},
            {name:'Preview', call:'preview', className:"preview", className: 'miu-icon miu-icon-preview'}
        ]
    };
    
    /*
     * Add "X-CSRFToken" header to every AJAX request within current domain
     * */
    $('html').ajaxSend(function(event, xhr, settings) {
        var isLocal = !settings.url.match(/^https?:\/\/([^\/]+)/i);
        
        if(isLocal || RegExp.$1 == document.location.host){
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    });
    
    /*
     * Single markItUp'ed textarea class
     * */
    function Editor(textareaId, extraSettings){
        
        /*
         * Editor instance: default mIu settings extended with what you passed to miu.init(..., extraSettings)
         * */
        var editorSettings = $.extend(settings, extraSettings);

        /*
         * Initialize/re-initialize the editor
         * */
        function init(){
            $('#' + textareaId).markItUp(editorSettings);
        }
        
        /*
         * Dynamically adds button to the editor at index position
         * */
        function addButton(conf, index){
            var index = (!index || index > editorSettings.markupSet.length ? editorSettings.markupSet.length : index);
            editorSettings.markupSet = $.merge(editorSettings.markupSet.slice(0, index), 
                                               $.merge([conf], 
                                                       editorSettings.markupSet.slice(index)));
            init();
        }
        
        /*
         * Dynamically removes button from the editor at index position
         * */
        function removeButton(index){
            editorSettings.markupSet = $.merge(editorSettings.markupSet.slice(0, index),
                                               editorSettings.markupSet.slice(index + 1));
            init();
        }
        
        /*
         * Get/set editor settings
         * */
        function config(newSettings){
            if(newSettings){
                editorSettings = newSettings;
                init();
            }
            return editorSettings;
        }
        
        /* ----- initializing ------ */
        
        this.addButton = addButton;
        this.removeButton = removeButton;
        this.config = config;
        this.init = init;
        
        init();
    }
    
    return {
        /*
         * Get/set default mIu settings
         * */
        config: function(newSettings){
            if(newSettings){
                settings = newSettings;
            }
            return settings;
        },
        
        /*
         * Returns editor instance by textarea id, 
         * if no textareaId passed then all instances will be returned
         * */
        editors: function(textareaId){
            return textareaId ? editors[textareaId] : editors;
        },
                
        /*
         * Shortcut for initializing editor
         * */
        init: function(textareaId, extraSettings){
            $(document).ready(function() {
                editors[textareaId] = new Editor(textareaId, extraSettings);
            });
        }
        
    }
    
})(jQuery || django.jQuery);
