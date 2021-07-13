<?php

namespace App\Infrastructure\Persistence\Article;

use App\Domain\Article\Article;
use App\Domain\Article\ArticleRepository;
use MongoDB\Model\BSONDocument;

class MongoArticleRepository implements ArticleRepository
{
    /**
     * @var \MongoDB\Database
     */
    private $db;

    /**
     * @var \MongoDB\Collection
     */
    private $articles;

    public function __construct()
    {
        $host = $_ENV['MONGO_HOST'];
        $dataBase = $_ENV['MONGO_DATABASE'];
        $collection = $_ENV['MONGO_COLLECTION'];
        $client = new \MongoDB\Client("mongodb://{$host}");
        $this->db = $client->selectDatabase($dataBase);
        $this->articles = $this->db->selectCollection($collection);
    }


    public function findAll(int $limit=30, int $offset=0): array
    {
        $documentList = $this->articles->find([],["limit"=>$limit, "offset"=>$offset]);
        $arrayArticle = [];
        /** @var $document BSONDocument */
        foreach ($documentList as $document)
        {
            $arrayArticle[] = $this->DocumentToArticle($document);
        }
        return $arrayArticle;
    }

    private function DocumentToArticle(BSONDocument $document): Article
    {
        return new Article($document->offsetGet("title"), $document->offsetGet("text"), $document->offsetGet("src"), $document->offsetGet("img_src"));
    }
}