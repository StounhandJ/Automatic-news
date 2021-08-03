<?php

namespace App\Http\Controllers;

use App\Models\Article;
use Illuminate\Http\Request;
use Illuminate\Routing\Controller;


class ArticleController extends Controller
{
    public function showAll(Request $request)
    {
        $p = 1;
        $validator = validator($request->all(), [
            "p"=>"required|integer|min:1"
        ]);
        if (!$validator->fails()) {
            $p = $request->all()["p"];
        }
        return view("welcome", ["articles"=>Article::all()->skip(($p-1)*30)->take(30), "pages"=>(int)ceil(Article::count()/30)]);
    }
}
