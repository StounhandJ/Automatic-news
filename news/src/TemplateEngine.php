<?php


namespace App;

use Smarty;

class TemplateEngine
{
    /**
     * @param string $name
     * @param array $data
     * @return false|string
     * @throws \SmartyException
     */
    static function respond(string $name, array $data)
    {
        $smarty = new Smarty;
        $smarty->setTemplateDir(__DIR__ . "/../template");
        $smarty->setCompileDir(__DIR__ . "/../template/compile");

        foreach ($data as $key => $value) {
            $smarty->assign($key, $value);
        }

        return $smarty->fetch($name . '.tpl');
    }
}