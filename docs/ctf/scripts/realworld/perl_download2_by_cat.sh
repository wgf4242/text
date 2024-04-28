# need install the LWP::Simple module

cat > run.sh << EOF
#!/usr/bin/perl
use strict;
use warnings;
use LWP::Simple;

my $url = 'http://124.2.3.4:2127/qeY6J3nIfR0fc';
my $output_file = 'downloaded_file';

unless (head($url)) {
    die "failed  URL: $url";
}

# download file
my $response = getstore($url, $output_file);

if ($response->is_success) {
    print "success $output_file\n";
} else {
    print "error: ", $response->status_line, "\n";
}
EOF

chmod +x ./run.sh
ls -la
