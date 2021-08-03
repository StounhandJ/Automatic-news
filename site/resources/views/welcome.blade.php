<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Автоматические новости</title>
    <link rel="stylesheet" href="css/article.css">
</head>

<body>
@foreach ($articles as $article)
    <div class="self">
        <img width="200" height="120" src="{{ $article->img_src }}" alt="#">
        <div class="info">
            <h1><a href="{{ $article->src }}">{{ $article->title }}</a></h1>
        </div>
    </div>
@endforeach
@for( $i=1; $i<=$pages; $i++)
    <li><a href='/?p={{ $i }}'>{{ $i }}</a></li>
@endfor
{{--{for $i=0; $i<$countPages; $i++}--}}
{{--    <li><a href='/?p={$i+1}'>{$i+1}</a></li>--}}
{{--{/for}--}}
</body>
</html>
