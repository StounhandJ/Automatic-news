<?php

namespace App\Application\Actions\Article;

use App\Application\Actions\Article\ArticleAction;
use Psr\Http\Message\ResponseInterface as Response;

class ListArticleAction extends ArticleAction
{
    /**
     * {@inheritdoc}
     */
    protected function action(): Response
    {
        $page = $this->queryParam("p")-1;
        $articles = $this->articleRepository->findAll(30, $page*30);
        $this->logger->info("Users list was viewed.");

        return $this->respondWithPage("main",["articles"=>$articles, "countPages"=>$this->articleRepository->count()/30]);
    }
}