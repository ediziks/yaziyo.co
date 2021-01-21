tinyMCE.init({
    selector: 'textarea',
    plugins: 'quickbars wordcount preview codesample image imagetools hr link lists media fullscreen autosave powerpaste nonbreaking',
    powerpaste_allow_local_images: false,
    theme: 'silver',
    mobile: {
        theme: 'mobile',
        plugins: ['autosave', 'lists', 'autolink'],
        toolbar: ['undo', 'redo', 'bold', 'link', 'bullist', 'numlist', 'styleselect',],
    },
    toolbar: 'undo redo | preview fullscreen',
    menubar: 'false',
    // 'quickimage' or file_picker_callback will be integrated for local image/file upload
    quickbars_insert_toolbar: 'media image | bullist numlist | hr',
    quickbars_selection_toolbar: 'bold italic underline strikethrough | fontsizeselect | alignleft aligncenter alignright | blockquote codesample | link',
    quickbars_image_toolbar: 'imagetools | alignleft aligncenter alignright | blockquote',
    height: '500',
    branding: false,
    elementpath: false,
    language: 'tr_TR',
    placeholder: "İçerik buradan başlar...",
    content_style: 'body {font-family:Inter,Arial,sans-serif; font-size:14pt; line-height:1; }',
    fontsize_formats: "14pt 20pt",
    nonbreaking_force_tab: true,
    image_title: true,
    image_caption: true,
    // paste_data_images: true,
    automatic_uploads: true,
    // images_upload_url: "/static/js/postAcceptor.php",
    // images_upload_base_path: "/static/js",
    // images_upload_credentials: true,
    // convert_urls: false,
    // relative_urls : false,

    // images_upload_handler : function handler(blobInfo, success, failure, progress) {
    //     {
    //             var valid_extensions = ['png','jpg']
    //             var ext, extensions;
        
    //             extensions = {
    //               'image/jpeg': 'jpg',
    //               'image/jpg': 'jpg',
    //               'image/gif': 'gif',
    //               'image/png': 'png'
    //             };
    //             ext = extensions[blobInfo.blob().type.toLowerCase()] || 'dat';
    //             //add your extension test here.
    //             if( valid_extensions.indexOf(ext) == -1){
    //                  failure("Invalid extension");
    //                     return;
    //             }
        
    //             var xhr, formData;
        
    //             xhr = new XMLHttpRequest();
    //             xhr.open('POST', '/static/js/postAcceptor.php');
    //             // xhr.withCredentials = settings.credentials;
        
    //             xhr.upload.onprogress = function(e) {
    //                 progress(e.loaded / e.total * 100);
    //             };
        
    //             xhr.onerror = function() {
    //                 failure("Image upload failed due to a XHR Transport error. Code: " + xhr.status);
    //             };
        
    //             xhr.onload = function() {
    //                 var json;
        
    //                 if (xhr.status != 200) {
    //                     failure("HTTP Error: " + xhr.status);
    //                     return;
    //                 }
        
    //                 json = JSON.parse(xhr.responseText);
        
    //                 if (!json || typeof json.location != "string") {
    //                     failure("Invalid JSON: " + xhr.responseText);
    //                     return;
    //                 }
        
    //                 success(pathJoin(settings.basePath, json.location));
    //             };
        
    //             formData = new FormData();
    //             formData.append('file', blobInfo.blob(), blobInfo.filename());
        
    //             xhr.send(formData);
    //         }
    //     },
        



   //  images_upload_handler: function (blobInfo, success, failure) {
   //      var xhr, formData;

   //      xhr = new XMLHttpRequest();
   //      xhr.withCredentials = false;
   //      xhr.open('POST', '/static/js/postAcceptor');

   //      xhr.onload = function() {
   //        var json; 

   //        if (xhr.status != 200) {
   //          failure('HTTP Error: ' + xhr.status);
   //          return;
   //        }

   //        console.log(xhr.response);
   //        //your validation with the responce goes here

   //        success(xhr.response);
   //      };

   //      formData = new FormData();
   //      formData.append('file', blobInfo.blob(), blobInfo.filename());

   //      xhr.send(formData);
   // }    

    // images_upload_handler: function(blobInfo, success, failure) {
    //   var xhr, formData
    //   xhr = new XMLHttpRequest();
    //   xhr.withCredentials = false;
    //   xhr.open("POST", "/static/js/postAcceptor.php");
    //   xhr.onload = function() {
    //     var json
    //     if (xhr.status != 200) {
    //       failure("HTTP Error: " + xhr.status);
    //       return;
    //     }
    //     console.log(xhr);
    //     json = JSON.parse(xhr.responseText);
    //     // console.log(json);
    //     if (!json || typeof json.location != 'string') {
    //       failure("Invalid JSON: " + xhr.responseText);
    //       return;
    //     }
    //     success(json.location);
    //   }
    //   formData = new FormData();
    //   formData.append('file', blobInfo.blob(), blobInfo.filename());
    //   xhr.send(formData);
    // },

    // images_upload_handler: function (blobInfo, success, failure, progress) {
    //     var xhr, formData;

    //     xhr = new XMLHttpRequest();
    //     //xhr.withCredentials = true;
    //     xhr.open('POST', '/static/js/postAcceptor.php');
    //     xhr.upload.onprogress = function (e) {
    //         progress(e.loaded / e.total * 100);
    //     };

    //     xhr.onload = function () {
    //         var json;

    //         if (xhr.status < 200 || xhr.status >= 300) {
    //             failure('HTTP Error: ' + xhr.status);
    //             return;
    //         }
    //         console.log(xhr);
    //         json = JSON.parse(xhr.responseText);

    //         if (!json || typeof json.location != 'string') {
    //             failure('Invalid JSON: ' + xhr.responseText);
    //             return;
    //         }

    //         success(json.location);
    //     };

    //     xhr.onerror = function () {
    //         failure('Image upload failed due to a XHR Transport error. Code: ' + xhr.status +
    //             ' Message:' + xhr.responseText);
    //     };

    //     formData = new FormData();
    //     formData.append('file', blobInfo.blob(), blobInfo.filename());
    //     xhr.send(formData);
    // }


    // file_picker_types: 'image file media',
    // /* and here's the custom image picker */
    // file_picker_callback: function (cb, value, meta) {
    //   var input = document.createElement('input');
    //   input.setAttribute('type', 'file');
    //   input.setAttribute('accept', 'image/*');

    //   /*
    //     Note: In modern browsers input[type="file"] is functional without
    //     even adding it to the DOM, but that might not be the case in some older
    //     or quirky browsers like IE, so you might want to add it to the DOM
    //     just in case, and visually hide it. And do not forget do remove it
    //     once you do not need it anymore.
    //   */

    //   input.onchange = function () {
    //     var file = this.files[0];

    //     var reader = new FileReader();
    //     reader.onload = function () {
    //       /*
    //         Note: Now we need to register the blob in TinyMCEs image blob
    //         registry. In the next release this part hopefully won't be
    //         necessary, as we are looking to handle it internally.
    //       */
    //       var id = 'blobid' + (new Date()).getTime();
    //       var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
    //       var base64 = reader.result.split(',')[1];
    //       var blobInfo = blobCache.create(id, file, base64);
    //       blobCache.add(blobInfo);

    //       /* call the callback and populate the Title field with the file name */
    //       cb(blobInfo.blobUri(), { title: file.name });
    //     };
    //     reader.readAsDataURL(file);
    //   };

    //   input.click();
    // }
});