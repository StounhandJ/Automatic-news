<?php

namespace App\Http\Controllers;

use App\Models\Article;
use Illuminate\Http\Request;
use Illuminate\Routing\Controller;


class ArticleController extends Controller
{
    public function showAll(Request $request)
    {
        $paginator = Article::orderBy("_id","desc")->paginate(30);
        return view("welcome", compact("paginator"));
    }
}
