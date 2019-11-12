BEGIN{
tcp_countr=0;
udp_countr=0;
tcp_countd=0;
udp_countd=0;
total_r=0;
total_d=0;
}
{
if($1=="r" && $5=="tcp")
tcp_countr++;
if($1=="d" && $5=="tcp")
tcp_countd++;
if($1=="r" && $5=="cbr")
udp_countr++;
if($1=="d" && $5=="cbr")
udp_countd++;
total_r=tcp_countr+udp_countr;
total_d=tcp_countd+udp_countd;
}
END{
printf("The number of packets received in tcp is %d\n",tcp_countr);
printf("The number of packets dropped in tcp is %d\n",tcp_countd);
printf("The number of packets received in udp is %d\n",udp_countr); 
printf("The number of packets dropped in udp is %d\n",udp_countd);
printf("The number of packets received is %d\n",total_r);
printf("The number of packets dropped is %d\n",total_d);
}





