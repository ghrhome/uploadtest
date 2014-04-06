tinymce.init({  
    // General options  
    selector : "textarea",  
    plugins: "uploadimage",
    toolbar: " styleselect | bold italic | uploadimage  |  alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
    image_list: [ 
        {title: 'My image 1', value: 'http://www.tinymce.com/my1.gif'}, 
        {title: 'My image 2', value: 'http://www.moxiecode.com/my2.gif'} 
    ]
});  
