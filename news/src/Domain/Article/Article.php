<?php
declare(strict_types=1);

namespace App\Domain\Article;

use JsonSerializable;

class Article implements JsonSerializable
{
    /**
     * @var string
     */
    private $title;

    /**
     * @var string
     */
    private $text;

    /**
     * @var string
     */
    private $src;

    /**
     * @var string
     */
    private $img_src;

    /**
     * @param string  $title
     * @param string    $text
     * @param string    $src
     * @param string    $img_src
     */
    public function __construct(string $title, string $text, string $src, string $img_src)
    {
        $this->title = $title;
        $this->text = $text;
        $this->src = $src;
        $this->img_src = $img_src;
    }


    /**
     * @return string
     */
    public function getTitle(): string
    {
        return $this->title;
    }

    /**
     * @return string
     */
    public function getText(): string
    {
        return $this->text;
    }

    /**
     * @return string
     */
    public function getSrc(): string
    {
        return $this->src;
    }

    /**
     * @return string
     */
    public function getImgSrc(): string
    {
        return $this->img_src;
    }

    /**
     * @return array
     */
    public function jsonSerialize()
    {
        return [
            'title' => $this->title,
            'text' => $this->text,
            'src' => $this->src,
            'img_src' => $this->img_src,
        ];
    }
}
