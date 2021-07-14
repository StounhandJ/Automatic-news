<?php
declare(strict_types=1);

use App\Application\Settings\SettingsInterface;
use App\Domain\Article\ArticleRepository;
use App\Infrastructure\Persistence\Article\MongoArticleRepository;
use DI\ContainerBuilder;
use Psr\Container\ContainerInterface;

return function (ContainerBuilder $containerBuilder) {
    // Here we map our UserRepository interface to its in memory implementation
    $containerBuilder->addDefinitions(array(
        ArticleRepository::class => function(ContainerInterface $c){
            $mongoConfig = $c->get(SettingsInterface::class)->get("databaseMongo");
            return new MongoArticleRepository($mongoConfig["host"], $mongoConfig["dataBase"], $mongoConfig["articles_collection"]);
        },
//        ArticleRepository::class => \DI\autowire(MongoArticleRepository::class),
    ));
};
