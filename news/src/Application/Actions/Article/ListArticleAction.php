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
        $articles = $this->articleRepository->findAll();

        $this->logger->info("Users list was viewed.");

        return $this->respondWithPage("main",["articles"=>$articles, "countPages"=>3]);
    }
}