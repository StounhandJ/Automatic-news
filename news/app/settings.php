<?php
declare(strict_types=1);

use App\Application\Settings\Settings;
use App\Application\Settings\SettingsInterface;
use DI\ContainerBuilder;
use Monolog\Logger;

return function (ContainerBuilder $containerBuilder) {

    // Global Settings Object
    $containerBuilder->addDefinitions([
        SettingsInterface::class => function () {
            $docker = $_ENV['docker']??false;
            return new Settings([
                'displayErrorDetails' => true, // Should be set to false in production
                'logError'            => false,
                'logErrorDetails'     => false,
                'docker'=>$docker,
                'logger' => [
                    'name' => 'slim-app',
                    'path' => $docker ? 'php://stdout' : __DIR__ . '/../logs/app.log',
                    'level' => Logger::DEBUG,
                ],
                'databaseMongo' => [
                    "host" => $docker ? $_ENV['MONGO_HOST'] : "localhost",
                    "dataBase"=>$docker ? $_ENV['MONGO_DATABASE'] : "testDB",
                    "articles_collection"=> $docker ? $_ENV['MONGO_COLLECTION'] : "testArticles"
                ]
            ]);
        }
    ]);
};
