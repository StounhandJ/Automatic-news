<?php

namespace App\Application\Actions\Article;

use App\Application\Actions\Action;
use App\Domain\Article\ArticleRepository;
use Psr\Log\LoggerInterface;

abstract class ArticleAction extends Action
{
    /**
     * @var ArticleRepository
     */
    protected $articleRepository;

    /**
     * @param LoggerInterface $logger
     * @param ArticleRepository $articleRepository
     */
    public function __construct(LoggerInterface $logger,
                                ArticleRepository $articleRepository
    ) {
        parent::__construct($logger);
        $this->articleRepository = $articleRepository;
    }
}