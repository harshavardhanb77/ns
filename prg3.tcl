set ns [new Simulator]
set tf [open prg3.tr w]
$ns trace-all $tf
set nf [open prg3.nam w]
$ns namtrace-all $nf
set cwind [open win4.tr w]

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

$ns duplex-link $n0 $n1 2Mb 2ms DropTail
$ns duplex-link $n1 $n4 2Mb 2ms DropTail
$ns duplex-link $n0 $n2 2Mb 2ms DropTail
$ns duplex-link $n2 $n3 2Mb 2ms DropTail
$ns duplex-link $n3 $n5 2Mb 2ms DropTail
$ns duplex-link $n4 $n5 2Mb 2ms DropTail

$ns duplex-link-op $n0 $n1 orient up-right
$ns duplex-link-op $n4 $n5 orient down-right
$ns duplex-link-op $n2 $n3 orient right 
$ns duplex-link-op $n1 $n4 orient right 
$ns duplex-link-op $n0 $n2 orient down-right
$ns duplex-link-op $n3 $n5 orient up-right

$ns rtproto DV
$ns rtmodel-at 1.0ms down $n1 $n4
$ns rtmodel-at 3.0ms up $n1 $n4 


set tcp0 [new Agent/TCP]
$ns attach-agent $n0 $tcp0
#Tcp sink is set
set sink0 [new Agent/TCPSink]
$ns attach-agent $n4 $sink0
$ns connect $tcp0 $sink0
set ftp [new Application/FTP]
$ftp attach-agent $tcp0
$tcp0 set fid_ 1
$ns at 0.1 "$ftp start"
$ns at 10.0 "finish"



proc plotWindow {tcpSource file} {
global ns
set time 0.01
set now [$ns now]
set cwnd [$tcpSource set cwnd_]
puts $file "$now $cwnd"
$ns at [expr $now+$time] "plotWindow  $tcpSource $file"}  

$ns at 2.0 "plotWindow  $tcp0 $cwind"

#Proc to finish
proc finish {} {
global ns tf nf cwind
$ns flush-trace
close $tf
close $nf

puts "Running nam... "
puts "FTP PACKETS"
puts "Telnet packets "
exec nam prg3.nam &
exec xgraph win4.tr &
exit 0
}

$ns run

