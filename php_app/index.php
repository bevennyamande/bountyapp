<?php

//check is POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {

$api = 'http://127.0.0.1:8000/postimage/';


//check image upload,
//your want to check for other things too like: is it an image?
//image size etc



if(isset($_FILES['image']['name'])){

        //make filename for new file
        $uploadfile = basename($_FILES['image']['name']);

        //move the upload
        if (move_uploaded_file($_FILES['image']['tmp_name'], $uploadfile)) {

            /* HttpRequest - I dont use it, it should work but if like me, 
              its class not found, then this condition will revert to curl */           
                $ch = curl_init($api);
                curl_setopt($ch, CURLOPT_HEADER, 0);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                curl_setopt($ch, CURLOPT_POST, true);
                curl_setopt($ch, CURLOPT_TIMEOUT, 30);
                curl_setopt($ch, CURLOPT_POSTFIELDS, array(
                    'image'=>'@'.$_SERVER['DOCUMENT_ROOT'].'/'.$uploadfile,
                ));

                $resp = curl_exec($ch);

            //decode the json response
            $resp = json_decode($resp, true);
        }
    }

}

//output the image from deviantsart
if ($resp){
    echo "<pre>";
    var_dump($resp);
    echo "</pre>";
}

?>
<form enctype="multipart/form-data" action="" method="POST">
    <!-- Name of input element determines name in $_FILES array -->
    Send this file: <input name="image" type="file" />
    <input type="submit" value="Send File" />
</form>
