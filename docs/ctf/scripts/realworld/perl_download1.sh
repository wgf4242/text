perl -MIO::Socket::INET -e '
    my $sock = IO::Socket::INET->new(PeerAddr => "124.1.2.192:2127");
    print $sock "GET /qeY6J3nIfR0fc HTTP/1.0\r\n\r\n";
    my $response = join "", <$sock>;
    close $sock;

    open my $file, ">", "/tmp/save" or die "Could not open file: $!\n";
    (my $headers, my $content) = split "\r\n\r\n", $response, 2;
    print $file $content;
    close $file;
'
