set ns [new Simulator]
set tf [open prg2.tr w]
$ns trace-all $tf
set nf [open prg2.nam w]
$ns namtrace-all $nf
set cwind [open win2.tr w]
set cwind1 [open win3.tr w]

$ns color 0 red
$ns color 1 blue    

set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]

$ns duplex-link $n3 $n1 2Mb 2ms DropTail 
$ns duplex-link $n3 $n2  2Mb 2ms DropTail
$ns duplex-link $n3 $n4  2Mb 2ms DropTail
$ns duplex-link $n4 $n5  2Mb 2ms DropTail
$ns duplex-link $n4 $n6   2Mb 2ms DropTail


$ns duplex-link-op $n3 $n1 orient left-up 
$ns duplex-link-op $n3 $n2 orient down-left
$ns duplex-link-op $n3 $n4 orient right 
$ns duplex-link-op $n4 $n5 orient right-up 
$ns duplex-link-op $n4 $n6 orient right-down 

#Tcp connection creating
set tcp0 [new Agent/TCP]
$ns attach-agent $n1 $tcp0
#Tcp sink is set
set sink0 [new Agent/TCPSink]
$ns attach-agent $n6 $sink0
$ns connect $tcp0 $sink0
set ftp [new Application/FTP]
$ftp attach-agent $tcp0
$tcp0 set fid_ 1
$ns at 0.1 "$ftp start"


#Tcp connection creating
set tcp1 [new Agent/TCP]
$ns attach-agent $n2 $tcp1
#Tcp sink is set
set sink1 [new Agent/TCPSink]
$ns attach-agent $n5 $sink1
$ns connect $tcp1 $sink1
set telnet [new Application/Telnet]
$telnet attach-agent $tcp1
$tcp1 set fid_ 0
$ns at 0.1 "$telnet start"


proc plotWindow {tcpSource file} {
global ns
set time 0.01
set now [$ns now]
set cwnd [$tcpSource set cwnd_]
puts $file "$now $cwnd"
$ns at [expr $now+$time] "plotWindow  $tcpSource $file"}  

$ns at 2.0 "plotWindow  $tcp0 $cwind"
$ns at 5.5 "plotWindow  $tcp1 $cwind1"

#Proc to finish
proc finish {} {
global ns tf nf cwind
$ns flush-trace
close $tf
close $nf

puts "Running nam... "
puts "FTP PACKETS"
puts "Telnet packets "
exec nam prg2.nam &
exec xgraph win2.tr &
exit 0
}

$ns run






