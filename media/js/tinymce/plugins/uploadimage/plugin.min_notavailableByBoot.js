/* 
ghrhome created by ghrhome on 14-4-7.
 */
(function() {
    tinymce.PluginManager.requireLangPack('uploadimage');

    tinymce.create('tinymce.plugins.UploadImage', {
        UploadImage: function(ed, url) {
            var form,
                iframe,
                win,
                throbber,
                editor = ed,
		$ctrl;

            function showDialog() {
                win = editor.windowManager.open({
		//这里是上传打开文件的html
		  //  url:"/media/js/tinymce/plugins/uploadimage/tinymceupload.html",
                    title: ed.translate('Insert an image from your computer'),
                    width:  500 + parseInt(editor.getLang('uploadimage.delta_width', 0), 10),
                    height: 280 + parseInt(editor.getLang('uploadimage.delta_height', 0), 10),
                    body: [
                      // {type: 'iframe',  url: 'javascript:void(0)'},
			{type: 'container',html:'<div><h1>upload your image</h1><div><span class="btn btn-success fileinput-button"><i class="glyphicon glyphicon-plus"></i><span>Add files...</span><!-- The file input field used as target for the file upload widget --><input id="tinymceupload" type="file" name="file" multiple=""></span><div id="progress" class="progress"><div class="progress-bar progress-bar-success"></div></div><div id="files" class="files"></div></div></div>'},
                       // {type: 'textbox', name: 'file', subtype:'file',multiple:'true' ,label:"选择一张图片", id:"tinymceupload"},
                      //  {type: 'textbox', name: 'alt',  label: ed.translate('Image description')},
		//	{type:'container',html:'<div id="tinycontainer" style="background-color:#ccc;width:200px;height:100px"><div>'},
                     //   {type: 'container', classes: 'error', html: "<p style='color: #b94a48;'>&nbsp;</p>",id:"tinyerror" },

                        // Trick TinyMCE to add a empty div that "preloads" the throbber image
                   //     {type: 'container', classes: 'throbber'},
                    ],
                    buttons: [
                      //  {
                     //       text: ed.translate('Insert'),
                      //      onclick: insertImage,
                      //      subtype: 'primary'
                      //  },
                        {
                            text: ed.translate('Cancel'),
                            onclick: ed.windowManager.close
                        }
                    ],
                }, {
                    plugin_url: url
                });
          //          $ctrl=$("#tinymceupload");
	//	    console.log($ctrl.html());
		    tinymceUpload();
		}
	//	console.log($ctrl.html());
                //在此绑定ctrl-uploadfile
                /*jslint unparam: true, regexp: true */
                /*global window, $ */
                function tinymceUpload(){
                    'use strict';
			console.log("testtest");
                        $ctrl=$("#tinymceupload")
			console.log($ctrl);
                    // Change this to the location of your server-side upload handler:
                    var urlto = '/ghrhome/ajaxupload2/';
                   // var $ctrl=$("input#tinymceupload");
			console.log($ctrl.attr("name"));
	            var uploadButton = $('<button/>')
                        .addClass('btn btn-primary')
                        .prop('disabled', true)
                        .text('Processing...')
                        .on('click', function () {
                            var $this = $(this),
                                data = $this.data();
                            $this
                                .off('click')
                                .text('Abort')
                                .on('click', function () {
                                    $this.remove();
                                    data.abort();
                                });
                            data.submit().always(function () {
                                //在此触发insertImage()方法。
                                //insertImage();
                                //
                                $this.remove();
                            });
                        });
                    $ctrl.fileupload({
                        url: urlto,
                        dataType: 'json',
                        autoUpload: false,
                        acceptFileTypes: /(\.|\/)(gif|jpe?g|png)$/i,
                        maxFileSize: 5000000, // 5 MB
                        // Enable image resizing, except for Android and Opera,
                        // which actually support image resizing, but fail to
                        // send Blob objects via XHR requests:
                        disableImageResize: /Android(?!.*Chrome)|Opera/
                            .test(window.navigator.userAgent),
                        previewMaxWidth: 100,
                        previewMaxHeight: 100,
                        previewCrop: true
                    }).on('fileuploadadd', function (e, data) {
                            data.context = $('<div/>').appendTo('#files');
                            $.each(data.files, function (index, file) {
                                var node = $('<p/>')
                                    .append($('<span/>').text(file.name));
                                if (!index) {
                                    node
                                        .append('<br>')
                                        .append( uploadButton.clone(true).data(data));
                                }
                                node.appendTo(data.context);
                            });
                        }).on('fileuploadprocessalways', function (e, data) {
                            var index = data.index,
                                file = data.files[index],
                                node = $(data.context.children()[index]);
                            if (file.preview) {
                                node
                                    .prepend('<br>')
                                    .prepend(file.preview);
                            }
                            if (file.error) {
                                node
                                    .append('<br>')
                                    .append($('<span class="text-danger"/>').text(file.error));
                            }
                            if (index + 1 === data.files.length) {
                                data.context.find('button')
                                    .text('Upload')
                                    .prop('disabled', !!data.files.error);
                            }
                        }).on('fileuploadprogressall', function (e, data) {
                            var progress = parseInt(data.loaded / data.total * 100, 10);
                            $('#progress .progress-bar').css(
                                'width',
                                progress + '%'
                            );
                        }).on('fileuploaddone', function (e, data) {   //这里是loadDone调用
                            $.each(data.result, function (index, file) {
                                //response这里是返回值
                                if (file.url) {
                                    ed.execCommand('mceInsertContent', false, buildHTML2(file));
                                    ed.windowManager.close();
                                } else if (file.error) {
                                    var error = $('<span class="text-danger"/>').text(file.error);
                                    $(data.context.children()[index])
                                        .append('<br>')
                                        .append(error);
                                }
                            });
                        }).on('fileuploadfail', function (e, data) {
                            $.each(data.files, function (index, file) {
                                var error = $('<span class="text-danger"/>').text('File upload failed.');
                                $(data.context.children()[index])
                                    .append('<br>')
                                    .append(error);
                            });
                        }).prop('disabled', !$.support.fileInput)
                        .parent().addClass($.support.fileInput ? undefined : 'disabled');
                }
	//	tinymceUpload();

                //ctrl绑定uploadfile--结束；
                //重构
                function buildHTML2(json) {
                    var default_class = ed.getParam("uploadimage_default_img_class", "");
                    var alt_text = getInputValue("alt");

                    var imgstr = "<img src='" + json["url"] + "'";

                    if(default_class != "")
                        imgstr += " class='" + default_class + "'";
                    imgstr += " alt='" + alt_text + "'/>";

                    return imgstr;
                }

//tinymce 标准程序

            // Add a button that opens a window
            editor.addButton('uploadimage', {
                tooltip: ed.translate('Insert an image from your computer'),
                icon : 'image',
                onclick: showDialog
            });

            // Adds a menu item to the tools menu
            editor.addMenuItem('uploadimage', {
                text: ed.translate('Insert an image from your computer'),
                icon : 'image',
                context: 'insert',
                onclick: showDialog
            });
        }
    });

    tinymce.PluginManager.add('uploadimage', tinymce.plugins.UploadImage);


})();
