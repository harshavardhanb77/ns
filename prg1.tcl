#Creating a simulator object
set ns [new Simulator] 
#Creating a trace file in write mode
set tf [open prg1.tr w]
 #opening the trace file 
$ns trace-all $tf
#Creating the nam file
set nf [open prg1.nam w]
 #Tracing the Nam file 
$ns namtrace-all $nf
#Creating a node
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node] 
$ns color 0 red
$ns color 1 blue

#Setting up the duplex link between nodes with 2mbs and 2ms-band width
#Drop tail is a queue type where the packets are stoped till all the packets are processed 
$ns duplex-link $n0  $n2 2Mb 2ms DropTail 
$ns duplex-link $n1  $n2 2Mb 2ms DropTail
$ns duplex-link $n2  $n3 4Mb 10ms DropTail
#Setting the the queue limit between nodes 0 and 1
$ns set queue-limit $n0 $n1 5
#Setting up an udp agent to node0
set udp1 [new Agent/UDP]
#Attaching the udp to source node
$ns attach-agent $n1 $udp1 
#Setting up udp and attaching sink to node 
set null1 [new Agent/Null]
$ns attach-agent $n3 $null1
#Connecting the two nodes
$ns connect $udp1 $null1
#Setting up a traffic between the line 
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp1
$cbr1 set fid_ 0
#Starting the transmition at 1.1 sec
$ns at 1.1 "$cbr1 start"

#Tcp connection creating
set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
#Tcp sink is set
set sink [new Agent/TCPSink]
$ns attach-agent $n3 $sink
$ns connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$tcp set fid_ 1
$ns at 0.1 "$ftp start"

$ns at 2.1 "$cbr1 stop"
$ns at 8.0 "finish"

#Proc to finish
proc finish {} {
global ns tf nf
$ns flush-trace
close $tf
close $nf
exec nam prg1.nam &
exit 0
}
$ns run



