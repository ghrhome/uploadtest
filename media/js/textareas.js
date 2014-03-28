tinymce.init({  
    // General options  
    selector : "textarea",  
    plugins: "image code",
    image_list: [ 
        {title: 'My image 1', value: 'http://www.tinymce.com/my1.gif'}, 
        {title: 'My image 2', value: 'http://www.moxiecode.com/my2.gif'} 
    ]
});  
