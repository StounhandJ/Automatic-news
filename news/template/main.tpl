<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="js/article.js"></script>
    <link rel="stylesheet" href="css/article.css">
</head>

<body>
{foreach $articles as $article}
    <div class="self">
        <img width="200" height="120" src="{$article->getImgSrc()}" alt="#">
        <div class="info">
            <h1><a href="{$article->getSrc()}">{$article->getTitle()}</a></h1>
        </div>
    </div>
{/foreach}
{for $i=0; $i<$countPages; $i++}
    <li><a href='/?p={$i+1}'>{$i+1}</a></li>
{/for}
</body>
</html>