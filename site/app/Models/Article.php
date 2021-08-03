<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Jenssegers\Mongodb\Eloquent\Model;

class Article extends Model
{
    use HasFactory;

    protected $collection = "";

    public function __construct(){
        $this->collection = env('MONGO_COLLECTION');
        parent::__construct();
    }

}
