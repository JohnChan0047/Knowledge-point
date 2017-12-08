# 图片文件上传与即时显示
原理：创建一个指向该图片的URL覆盖原图片的URL
```
<!DOCTYPE html>
<html>
<head>
    <title>立即显示上传的图片</title>
    <meta charset="utf-8">
    <style>
        img{
            width: 100px;
            height: 100px;
        }
    </style>

</head>
<body>
<div class="image">
    <input id="fileupload" type="file">
    <img id="imageview" >
</div>

<script type="text/javascript" src="static/js/jquery-3.2.1.min.js"></script>
<script type="text/javascript">
    $(function() {
        var $file_input = $('#fileupload');
        $file_input.change(function () {
            var file = $file_input.val();
            /*判断格式*/
            if(!/.(gif|jpg|jpeg|png|gif|jpg|png)$/.test(file)){
                alert('格式错误')
            }else {
                /*创建指向图片的url*/
                var file_url = $file_input[0].files[0];
                var windowsURL = window.URL || window.webkit;
                var url = windowsURL.createObjectURL(file_url);
                $('img').attr('src', url);
            }
        })

    });
</script>
</body>
</html>
```