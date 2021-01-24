tinyMCE.init({
  selector : 'textarea',
  plugins: 'quickbars wordcount codesample image imagetools hr link lists media fullscreen autosave powerpaste nonbreaking',
  powerpaste_allow_local_images : false,
  theme: 'silver',
  mobile: {
      theme: 'mobile',
      plugins: ['autosave', 'lists', 'autolink'],
      toolbar: ['undo', 'redo', 'bold', 'link', 'bullist', 'numlist', 'styleselect',]
  },
  toolbar: 'undo redo | fullscreen',
  menubar: 'false',
  // 'quickimage' will be integrated for local image/file upload
  quickbars_insert_toolbar: 'media image | bullist numlist | hr',
  quickbars_selection_toolbar: 'bold italic underline strikethrough | fontsizeselect | alignleft aligncenter alignright | blockquote codesample | link',
  quickbars_image_toolbar: 'alignleft aligncenter alignright | blockquote',
  height: '500',
  branding: false,
  elementpath: false,
  language: 'tr_TR',
  placeholder: "İçerik buradan başlar...",
  content_style: "body {font-family:'Inter', sans-serif; font-size:14pt; line-height:1; } img {max-width: 100%; height: auto;}",
  fontsize_formats: "14pt 20pt",
  nonbreaking_force_tab: true,
  image_title: true,
  /* enable automatic uploads of images represented by blob or data URIs*/
  // automatic_uploads: true,
  // images_upload_url: 'postAcceptor.php/',
  // images_upload_base_path: '/media/uploads/',
  // images_upload_credentials : true,
  // file_picker_types: 'image file',
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
  // },
});
