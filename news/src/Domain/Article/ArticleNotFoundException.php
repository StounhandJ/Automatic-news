<?php


namespace App\Domain\Article;

use App\Domain\DomainException\DomainRecordNotFoundException;

class ArticleNotFoundException extends DomainRecordNotFoundException
{
    public $message = 'The game you requested does not exist.';
}