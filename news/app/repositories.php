<?php
declare(strict_types=1);

use App\Domain\Article\ArticleRepository;
use App\Infrastructure\Persistence\Article\MongoArticleRepository;
use DI\ContainerBuilder;

return function (ContainerBuilder $containerBuilder) {
    // Here we map our UserRepository interface to its in memory implementation
    $containerBuilder->addDefinitions([
        ArticleRepository::class => \DI\autowire(MongoArticleRepository::class),
    ]);
};
