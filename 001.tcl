set val(chan) Channel/WirelessChannel
set val(prop) Propagation/TwoRayGround
set val(netif) Phy/WirelessPhy
set val(ifq) Queue/DropTail/PriQueue
set val(ifqLen) 50
set val(mac) Mac/802_11
set val(ll) LL
set val(ant) Antenna/OmniAntenna
set val(x) 500
set val(y) 500
set val(nn) 2
set val(stop) 20.0
set val(rp) DSDV

set ns_ [new Simulator]
set tf [open lab6.tr w]
$ns_ trace-all $tf

set nf [open lab6.nam w]
$ns_ namtrace-all-wireless $nf $val(x) $val(y)

set topo [new Topography]
$topo load_flatgrid $val(x) $val(y)

set god_ [create-god $val(nn)]

$ns_ node-config -adhocRouting $val(rp)\
              -llType $val(ll)\
              -macType $val(mac)\
              -ifqType $val(ifq)\
              -ifqLen $val(ifqLen)\
              -antType $val(ant)\
              -propType $val(prop)\
              -phyType $val(netif)\
              -channelType $val(chan)\
              -topoInstance $topo\
              -agentTrace ON\
              -routerTrace ON\
              -macTrace ON

for {set i 0} {$i < $val(nn) } {incr i} {
  set node_($i) [$ns_ node]
  $node_($i) random-motion 0
}

#Initial positions of nodes
for {set i 0} {$i < $val(nn)} {incr i} {
   $ns_ initial_node_pos $node_($i) 40
}

#Topology Design
$ns_ at 1.1 "$node_(0) setdest 310.0 10.0 20.0"
$ns_ at 1.1 "$node_(1) setdest 10.0 310.0 20.0"

#Generating traffic
set tcp0 [new Agent/TCP]
set sink0 [new Agent/TCPSink]
$ns_ attach-agent $node_(0) $tcp0
$ns_ attach-agent $node_(1) $sink0
$ns_ connect $tcp0 $sink0
set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0
$ns_ at 1.0 "$ftp0 start"
$ns_ at 18.0 "$ftp0 stop"


#Simulation termination
for {set i 0} {$i < $val(nn)} {incr i} {
  $ns_ at $val(stop) "$node_($i) reset" ;
  }

$ns_ at $val(stop) "puts \"NS EXITING...\"; $ns_ halt"
puts "Starting simulation"

$ns_ run
