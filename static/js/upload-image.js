$(document).ready(function(){
    var list_of_files = new Array();
    Dropzone.autoDiscover = false;  //prevent dropzone to automatically discover the dropzone object in your html
    $("div#dropzone").dropzone({
          uploadMultiple: true, // allow multiple upload
          autoProcessQueue: false, // prevent dropzone from uploading automatically
          url: "/", //dropzone needs a url attribute or it complains, what value you put here does not really matter. It is only purpose is to prevent a javascript error message from chrome console
          maxFiles: 5, //set max uploads to 5 since you only have 5 image files in your model
          init: function(){
              //everytime a file is uploaded, save the file object
              //for later use
              this.on("addedfile", function(file)
              {
                  if (list_of_files.length < 5)
                  {
                      list_of_files.push(file)
                      console.log("file added");
                  }
              });
          }
      });

    // the following function override the "submit" button in the form
    $(document).on("click", "button", function(e){
          e.preventDefault() //prevent the form from submitting 
          console.log('num of files: ' + list_of_files.length);
          var formData = new FormData(); // construct our own upload data
          var inputs = $("#newUserForm input");

          //get all of the data from textboxes
          $.each(inputs, function(obj, v){
              var name = $(v).attr("name")
              var val = $(v).val();
              console.log('name: ' + name + ' value: ' + val);
              formData.append(name, val);
          });

          //get the file object from dropzone and put it into our formdata
          for(i=0;i<list_of_files.length;i++)
          {
              formData.append('user_image'+(i+1), list_of_files[i]);
          }

          var request = new XMLHttpRequest();
          request.open("POST", "/"); //config your post url here
          request.send(formData);  //send the post request to server
      });
});