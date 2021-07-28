<?php


namespace App\Domain\Article;

use App\Domain\DomainException\DomainRecordNotFoundException;

class ArticlesNotFoundException extends DomainRecordNotFoundException
{
    public $message = 'No articles found.';
}