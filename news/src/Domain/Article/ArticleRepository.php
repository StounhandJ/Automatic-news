<?php


namespace App\Domain\Article;


interface ArticleRepository
{
    /**
     * @param int $limit
     * @param int $offset
     * @return \App\Domain\Article\Article[]
     */
    public function findAll(int $limit=30, int $offset=0): array;
}