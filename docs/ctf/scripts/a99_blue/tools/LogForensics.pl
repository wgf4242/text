#!/usr/bin/perl -w

use Getopt::Long;
use Tie::File;

my $version=2014102301;
print "\t\t\tWeb log forensics\n";
print "\t\t\tver2014102301 by xti9er\n";
$|=1;
my $file;
my @logs;
my $input_ip;
my $input_url;
my $websvr='';
my $ip_flag=0;
my $url_flag=0;
my @ips;
my @urls;
my $time;
my $process;
my %result;
my $stime=time;
my $regex;
my $fast;

my %asctimes=qw(
Jan 1
Feb 2
Mar 3
Apr 4
May 5
Jun 6
Jul 7
Aug 8
Sep 9
Oct 10
Nov 11
Dec 12
);	

my $result = GetOptions (
					  "ip=s" => \$input_ip,
                      "file=s"   => \$file, 
                      "url=s"  => \$input_url,
					  "websvr=s"  => \$websvr,
					  "fast"  => sub{$fast=1},
					  "help"  => sub{usage()}
                     );                   


my $tregex=qr/(\d+)\/(\w+)\/(\d+):(\d+):(\d+):(\d+)/;

if($websvr eq 'nginx'){
	$regex=qr/(\d+\.\d+\.\d+\.\d+) - - \[(\d+\/\w+\/\d+:\d+:\d+:\d+) \+\d+\].*?(GET|POST)\s(.*?)\sHTTP.*?"\s(\d+)/;
}
elsif($websvr eq 'httpd'){
	$regex=qr/(\d+\.\d+\.\d+\.\d+) - - \[(\d+\/\w+\/\d+:\d+:\d+:\d+) \+\d+\] "(GET|POST)\s(.*?)\sHTTP.*?"\s(\d+)?/;
}
elsif($websvr eq 'iis'){
	$regex=qr/(\d+-\d+-\d+ \d+:\d+:\d+) .*?\s(GET|POST) (.*?) \d+ - (\d+.\d+.\d+.\d+) .*? (\d+)\s/;
}
else{usage();}
usage() until defined($file);
#ip   1.2.3.4,5.6.7.8
if(defined $input_ip){
	if($input_ip=~/\,/){
		@ips=split(/\,/,$input_ip);
	}
	else{
		push(@ips,$input_ip);
	}
	$ip_flag=1;
}

if(defined $input_url){
	if($input_url=~/\,/){
		@urls=split(/\,/,$input_url);
	}
	else{
		push(@urls,$input_url);
	}
	$url_flag=1;
}

print "[*] ip=",$input_ip?$input_ip:'NULL'," \t url=",$input_url?$input_url:'NULL',"\n";
	
PRELOADED:
if(-e "$file.db"){
	print "[*] LOAD $file.db\n";
	
	if($fast){
		my @tmp_logs;
		tie @tmp_logs, 'Tie::File', "$file.db" or die $!;
		foreach my $line(@tmp_logs){
			push(@logs,$line);
		}
	}
	else{
		tie @logs, 'Tie::File', "$file.db" or die $!;
	}	
	
	my $oldip=scalar(@ips);
	my $oldurl=scalar(@urls);
	OTHERIP:
	# print "ips:@ips\n";
	# print "url:@urls\n";
	#preload regex
	for(1..$#urls){$urls[$_]=qr/$urls[$_]/}
	
	foreach my $line(@logs){
		my @info=split(/\t/,$line);
		my $tmp_ip_flag=0;
		my $tmp_url_flag=0;
		if(scalar(@ips)>0){
			
			for(@ips){
				$tmp_ip_flag=1 if $info[0] eq $_;
			}
		}

		#有url参数则从Url查起，否则全量
		if(scalar(@urls)>0){
			
			for my $now_url(@urls){
				$tmp_url_flag=1 if $info[3]=~/$now_url/;
			}
		}
				
		my @cgi=split(/\?/,$info[3]);
		if($tmp_url_flag==1 or $tmp_ip_flag==1){
			$result{$info[0]}{@cgi?$cgi[0]:$info[3]}{$info[1]}++;
		}
		elsif(scalar(@ips)==0 and scalar(@urls)==0){
			$result{$info[0]}{@cgi?$cgi[0]:$info[3]}{$info[1]}++;
		}

	}
	
	my %tmp_ip_url;
	my %tmp_url_ip;
	my $tmp_url_minus;
	foreach my $ip(keys %result){
		foreach my $url(keys %{$result{$ip}}){
			foreach my $time(keys %{$result{$ip}{$url}}){
				$tmp_ip_url{$ip}{$url}+=$result{$ip}{$url}{$time};
				$tmp_url_ip{$url}{$ip}=0;
			}
			#删除访问次数大于XX次的 url
			delete $result{$ip}{$url} if $tmp_ip_url{$ip}{$url}>50;
			$tmp_url_minus++;
		}
	}

	foreach my $tmp_url(keys %tmp_url_ip){
		#删除访问IP数大于XX次的URL	
		if(scalar(keys %{$tmp_url_ip{$tmp_url}})>10){
			foreach my $ip(keys %result){
				delete $result{$ip}{$tmp_url};
				$tmp_url_minus++;
			}
		}	
	}

	################
	my $newip=scalar(keys %result);
	
	my %tmp_url;
	foreach my $ip(keys %result){
		foreach my $url(keys %{$result{$ip}}){
			$tmp_url{$url}++;
		}
	}
		
	my $newurl=scalar(keys %tmp_url);
	
		#循环查找根据条件查到的所有IP的线索		???
	if($newip>$oldip or $newurl>$oldurl){
	
		#####更新IP条件
		undef @ips;
		foreach my $ip(keys %result){push(@ips,$ip);}
		
		#####更新url条件
		undef @urls;
		for(keys %tmp_url){push(@urls,$_)}
		
		################
		undef @ips if $ip_flag==1;
		undef @urls if $url_flag==1;
		#print "@ips\n";
		print "[!] ip + ",$newip-$oldip," & url + ",$newurl-$oldurl," and go on\n";
		$oldip=$newip;
		$oldurl=$newurl;
		sleep 2;
		goto OTHERIP;
	}
	
	print "[*] Export report... Plz wait\n";
	report();
}
else{
	print "[*] PRELOAD $file Plz wait\n";
	open(LOG,"$file") or die $!; 
	open(DB,"+>$file.db") or die $!; 
	while(my $line=<LOG>){

		# $process++;
		# print $process%2?'+':'x';print "\b";
		chomp($line);
	
		#print "$line\n";
		if($line=~/$regex/){
			my $ip;
			my $time;
			my $method;
			my $url;
			my $status_code;
			my $cgi;
			
			if($websvr eq 'iis'){
				$time=$1;
				$method=$2;
				$url=$3;
				$ip=$4;
				$status_code=$5;
			}
			else{
				$ip=$1;
				$time=logt2timestamp($2);
				$method=$3;
				$url=$4;
				$status_code=$5;				
			}
			
			####方便URL去重
			if($url=~/(.*?)\?/){
				$cgi=$1;
			}
			else{
				$cgi=$url;
			}
			##############
			#print "$ip\t$time\t$method\t$url\t$status_code\t$cgi\n";
			if($status_code!=200){next;}
#			if($method eq 'GET' and $cgi=~/.html$|.htm$|.jpg$|.png$|.js$|.gif$|.jpeg$|.swf$|\/$|.css$|.ico$|.txt$/i){next;}
			if(($method eq 'GET' and $cgi=~/.php$|.jsp$|.asp$|.aspx$/i) or ($method eq 'POST')){
				print DB "$ip\t$time\t$method\t$url\t$status_code\t\n";
			}			
		}			
	}
	
	close DB;
	close LOG;	
	goto PRELOADED;
} 

sub usage{
	print "
	usage:
	LogForensics.pl -file logfile -websvr (nginx|httpd) [-ip ip(ip,ip,ip)|-url url(url,url,url)]
	";
	exit;
}

sub logt2timestamp{
	#21/Sep/2014:00:09:55
	my @atime;
	my $logt=shift;

	if(@atime=$logt=~/$tregex/){	
		return "$atime[2]-$asctimes{$atime[1]}-$atime[0] $atime[3]:$atime[4]:$atime[5]";
	}
}

sub report{
	
	open(RE,"+>$file.log");
	my $allurl=0;
	my $allip=0;
	foreach my $ip(keys %result){
		if(scalar(keys %{$result{$ip}})>0){
			#print "[ip] $ip\n";
			$allip++;
			print RE "[ip] $ip\n";
		}
		foreach my $url(keys %{$result{$ip}}){
			my @tmp_result=keys %{$result{$ip}{$url}};
			#[first time ~ last time] + url + (count)
			print RE "	|__\t[$tmp_result[0] ~ $tmp_result[$#tmp_result]] $url	(".scalar(keys %{$result{$ip}{$url}}).")\n";
		}
		$allurl+=scalar(keys %{$result{$ip}});
	}
	
	my $etime=time;
	print "[*] All Done in ",$etime-$stime," s , ip[$allip] url[$allurl]\n";
	print RE "[*] All Done in ",$etime-$stime," s , ip[$allip] url[$allurl]\n";
	close RE;
}